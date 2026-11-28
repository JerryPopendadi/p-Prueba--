/**
 * THE FACES INVEST · enquiries → Google Sheet + instant email.
 *
 * Setup (5 minutes, see GUIA_CONVERSIONES_INVEST.md):
 *  1. Create a Google Sheet "THE FACES INVEST · Leads" with the Google account that should own the data.
 *  2. In the Sheet: Extensions → Apps Script. Delete the sample code, paste this file, Save.
 *  3. Deploy → New deployment → type "Web app" → Execute as: Me · Who has access: Anyone → Deploy → allow permissions.
 *  4. Copy the Web app URL (ends with /exec) into CONFIG.sheetUrl in the-faces-invest-v04.html (Elementor HTML widget).
 *
 * Every valid enquiry adds one row to the "Leads" tab and sends an email to NOTIFY.
 * Empty or invalid submissions (bots) are rejected here too, not only in the browser.
 */
var NOTIFY = 'info@thefacespeace.com';   // who receives the email for every new enquiry (comma-separate several addresses)
var SHEET_NAME = 'Leads';
var FIELDS = ['received_at', 'lead_id', 'name', 'email', 'phone', 'country', 'profile', 'interest', 'interest_label', 'budget', 'contact_pref', 'message', 'marketing', 'consent',
              'language', 'placement', 'page', 'referrer', 'utm_source', 'utm_medium', 'utm_campaign', 'utm_term', 'utm_content',
              'gclid', 'gbraid', 'wbraid', 'user_agent', 'status'];

function doPost(e) {
  var p = (e && e.parameter) || {};
  if (p.website) return out_({ ok: true });                                   // honeypot filled → bot, ignore silently
  var name = clean_(p.name, 100), email = clean_(p.email, 150).toLowerCase();
  var valid = name.length >= 2 && /^[^\s@<>"'()]+@[^\s@<>"'()]+\.[a-z]{2,}$/i.test(email) &&
              clean_(p.country, 80).length >= 2 && clean_(p.interest, 80) && clean_(p.profile, 60) && p.consent === 'yes';
  if (!valid) return out_({ ok: false, error: 'invalid' });                   // never store empty enquiries

  var cache = CacheService.getScriptCache();                                   // same email: at most once every 2 minutes
  if (cache.get('e:' + email)) return out_({ ok: true, duplicate: true });
  cache.put('e:' + email, '1', 120);

  var lock = LockService.getScriptLock();
  lock.waitLock(10000);
  try {
    sheet_().appendRow(FIELDS.map(function (f) {
      if (f === 'received_at') return new Date();
      if (f === 'status') return 'new';
      return safe_(p[f]);
    }));
  } finally {
    lock.releaseLock();
  }

  var lines = [
    'New partnership enquiry — THE FACES INVEST', '',
    'Name: ' + name, 'Email: ' + email, 'Phone / WhatsApp: ' + (clean_(p.phone, 40) || '—'),
    'Country: ' + clean_(p.country, 80), 'Profile: ' + clean_(p.profile, 60),
    'Interested in: ' + (clean_(p.interest_label, 80) || clean_(p.interest, 80)),
    'Indicative budget: ' + (clean_(p.budget, 40) || 'prefers to discuss'), 'Preferred contact: ' + (clean_(p.contact_pref, 20) || 'email'),
    'Message: ' + (clean_(p.message, 2000) || '—'), 'News opt-in: ' + (p.marketing === 'yes' ? 'yes' : 'no'), '',
    'Language: ' + clean_(p.language, 5) + ' · Clicked: ' + clean_(p.placement, 40) + ' · Page: ' + clean_(p.page, 300),
    'Campaign: ' + ['utm_source', 'utm_medium', 'utm_campaign', 'gclid'].map(function (k) { return p[k] ? k + '=' + clean_(p[k], 150) : ''; }).filter(String).join(' · '),
    'Lead ID: ' + clean_(p.lead_id, 60), '',
    'All enquiries: ' + SpreadsheetApp.getActive().getUrl()
  ];
  MailApp.sendEmail({ to: NOTIFY, replyTo: email,
    subject: 'New enquiry · ' + name + ' · ' + (clean_(p.interest_label, 60) || clean_(p.interest, 60)),
    body: lines.join('\n') });
  return out_({ ok: true });
}

function doGet() { return out_({ ok: true, service: 'THE FACES INVEST leads' }); }

function sheet_() {
  var ss = SpreadsheetApp.getActive(), sh = ss.getSheetByName(SHEET_NAME);
  if (!sh) { sh = ss.insertSheet(SHEET_NAME); sh.appendRow(FIELDS); sh.setFrozenRows(1); }
  else if (sh.getRange(1, 1, 1, FIELDS.length).getValues()[0].join('|') !== FIELDS.join('|')) {
    if (sh.getLastRow() > 1) {                                                 // old columns with data: keep them in a renamed tab
      sh.setName(SHEET_NAME + ' (old ' + Utilities.formatDate(new Date(), 'UTC', 'yyyy-MM-dd HH:mm') + ')');
      sh = ss.insertSheet(SHEET_NAME, 0); sh.appendRow(FIELDS);
    } else {
      sh.getRange(1, 1, 1, FIELDS.length).setValues([FIELDS]);
    }
    sh.setFrozenRows(1);
  }
  return sh;
}
function clean_(v, n) { return String(v == null ? '' : v).replace(/[\u0000-\u001F\u007F]/g, ' ').replace(/\s+/g, ' ').trim().slice(0, n || 200); }
function safe_(v) { v = clean_(v, 2000); return /^[=+\-@]/.test(v) ? "'" + v : v; }  // no spreadsheet formulas from the web
function out_(o) { return ContentService.createTextOutput(JSON.stringify(o)).setMimeType(ContentService.MimeType.JSON); }
