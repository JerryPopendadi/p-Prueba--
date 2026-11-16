/**
 * THE FACES INVEST · Forminator form 703 → Google Sheet + email, WITHOUT Google Cloud.
 * Uses Forminator's free "Webhook" integration and a Google Apps Script web app (only a Google account is needed).
 *
 * Setup:
 *  1. Open your Google Sheet → Extensions → Apps Script. Replace all code with this file → Save.
 *  2. Deploy → Manage deployments → pencil (edit) → Version: New version → Deploy
 *     (or, if you never deployed: Deploy → New deployment → Web app · Execute as: Me · Who has access: Anyone).
 *     Copy the Web app URL (ends with /exec).
 *  3. WordPress → Forminator → Integrations → Webhook → Activate.
 *     Then Forminator → Forms → 703 → Edit → Integrations → Webhook → Connect → paste the /exec URL → Save.
 *  4. Send a test enquiry: a row appears in the "Leads" tab and an email arrives.
 *
 * Columns are created automatically from the form fields, so new fields (hidden-1…hidden-8, etc.) just add columns.
 */
var NOTIFY = 'info@thefacespeace.com';   // email for every new enquiry ('' = no email; Forminator can email too)
var SHEET_NAME = 'Leads';
var LABELS = {                            // nicer column titles for the fields of form 703
  'name-1': 'Full name', 'email-1': 'Email', 'phone-1': 'Phone / WhatsApp', 'text-1': 'Country',
  'radio-1': 'Investment budget (USD)', 'hidden-1': 'Lead ID', 'hidden-2': 'Language', 'hidden-3': 'Clicked',
  'hidden-4': 'UTM source', 'hidden-5': 'UTM medium', 'hidden-6': 'UTM campaign', 'hidden-7': 'GCLID', 'hidden-8': 'Page'
};
var SKIP = /captcha|nonce|referer|^_|^action$|^page_id$|^form_id$|^current_url$|^render_id$|^forminator/i;

function doPost(e) {
  var data = parse_(e);
  debug_(e, data);                                                          // every call is logged in the "Debug" tab
  // email / name: by field id, or found by content if Forminator uses other keys
  var email = clean_(data['email-1'] || find_(data, function (k, v) { return /^[^\s@<>"'()]+@[^\s@<>"'()]+\.[a-z]{2,}$/i.test(v); })).toLowerCase();
  var name = clean_(data['name-1'] || [data['name-1-first-name'], data['name-1-last-name']].join(' ') || find_(data, function (k, v) { return /name|nombre|имя/i.test(k) && !/@/.test(v); }));
  if (!/^[^\s@<>"'()]+@[^\s@<>"'()]+\.[a-z]{2,}$/i.test(email) || name.replace(/\s/g, '').length < 2) {
    return out_({ ok: false, error: 'empty or invalid' });              // never store empty enquiries
  }
  var lock = LockService.getScriptLock(); lock.waitLock(10000);
  try {
    var sh = sheet_(), keys = Object.keys(data).filter(function (k) { return !SKIP.test(k); });
    var head = sh.getLastColumn() ? sh.getRange(1, 1, 1, sh.getLastColumn()).getValues()[0] : [];
    if (!head.length) { head = ['Received', 'Status']; sh.getRange(1, 1, 1, 2).setValues([head]); sh.setFrozenRows(1); }
    keys.forEach(function (k) {                                              // add a column for every new field
      var title = (LABELS[k] || k);
      if (head.indexOf(title) < 0) { head.push(title); sh.getRange(1, head.length).setValue(title); }
    });
    var row = head.map(function (title) {
      if (title === 'Received') return new Date();
      if (title === 'Status') return 'new';
      var k = keys.filter(function (x) { return (LABELS[x] || x) === title; })[0];
      return k ? safe_(data[k]) : '';
    });
    sh.appendRow(row);
  } finally { lock.releaseLock(); }

  if (NOTIFY) {
    var body = ['New investor enquiry — THE FACES INVEST', ''].concat(Object.keys(data).filter(function (k) { return !SKIP.test(k) && clean_(data[k]); })
      .map(function (k) { return (LABELS[k] || k) + ': ' + clean_(data[k]); })).concat(['', 'All enquiries: ' + SpreadsheetApp.getActive().getUrl()]);
    MailApp.sendEmail({ to: NOTIFY, replyTo: email, subject: 'New enquiry · ' + name + ' · ' + clean_(data['radio-1'] || ''), body: body.join('\n') });
  }
  return out_({ ok: true });
}

function doGet() { return out_({ ok: true, service: 'THE FACES INVEST · Forminator webhook v2' }); }

/** Forminator sends JSON; also accepts normal form posts. Arrays/objects are flattened to text. */
function parse_(e) {
  var d = {};
  try { if (e && e.postData && e.postData.contents) d = JSON.parse(e.postData.contents); } catch (x) { d = {}; }
  if (e && e.parameter) Object.keys(e.parameter).forEach(function (k) { if (d[k] === undefined) d[k] = e.parameter[k]; });
  Object.keys(d).forEach(function (k) {
    var v = d[k];
    if (v && typeof v === 'object') {
      if (!Array.isArray(v) && (v['first-name'] || v['last-name'])) d[k] = [v['prefix'], v['first-name'], v['middle-name'], v['last-name']].filter(Boolean).join(' ');
      else d[k] = Array.isArray(v) ? v.join(', ') : Object.keys(v).map(function (i) { return v[i]; }).filter(Boolean).join(' ');
    }
  });
  return d;
}
function find_(d, test) { for (var k in d) { var v = clean_(d[k]); if (v && !SKIP.test(k) && test(k, v)) return v; } return ''; }
function debug_(e, data) {
  try {
    var ss = SpreadsheetApp.getActive(), sh = ss.getSheetByName('Debug') || ss.insertSheet('Debug');
    if (!sh.getLastRow()) sh.appendRow(['Received', 'Content type', 'Raw body', 'Parsed keys']);
    sh.appendRow([new Date(), (e && e.postData && e.postData.type) || '', String((e && e.postData && e.postData.contents) || JSON.stringify((e && e.parameter) || {})).slice(0, 5000),
                  Object.keys(data).join(', ')]);
  } catch (x) {}
}
function sheet_() { var ss = SpreadsheetApp.getActive(); return ss.getSheetByName(SHEET_NAME) || ss.insertSheet(SHEET_NAME, 0); }
function clean_(v) { return String(v == null ? '' : v).replace(/[\u0000-\u001F\u007F]/g, ' ').replace(/\s+/g, ' ').trim().slice(0, 2000); }
function safe_(v) { v = clean_(v); return /^[=+\-@]/.test(v) ? "'" + v : v; }   // no spreadsheet formulas from the web
function out_(o) { return ContentService.createTextOutput(JSON.stringify(o)).setMimeType(ContentService.MimeType.JSON); }

/** Run once from the editor (select "testRow" → Run) to check the Sheet and email work. */
function testRow() {
  doPost({ postData: { contents: JSON.stringify({ 'name-1': 'Test Person', 'email-1': 'test@example.com', 'phone-1': '+34 600 000 000',
    'text-1': 'Spain', 'radio-1': 'US$250,000 – 500,000', 'hidden-3': 'proj_ub' }) } });
}
