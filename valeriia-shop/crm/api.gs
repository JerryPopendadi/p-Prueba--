/**
 * VALERIIA CRM — PUBLIC API  (проект №1, привязан к Google-таблице)
 * -----------------------------------------------------------------
 * Принимает заявки с сайта и продажи PDF из Payhip, отдаёт сайту
 * количество свободных мест в группах. Больше ничего не умеет —
 * личные данные клиентов наружу НЕ отдаёт.
 *
 * Развёртывание: Deploy → New deployment → Web app
 *   Execute as: Me   ·   Who has access: Anyone
 * Полученный URL вставить в index.html → CONFIG.apiUrl
 * и в Payhip → Settings → Developer → Webhooks.
 * PayPal: сайт сам передаёт этот URL как notify_url (IPN) — в PayPal ничего настраивать не нужно.
 *
 * Свойства скрипта (Project Settings → Script properties):
 *   PAYHIP_API_KEY — ключ из Payhip (для проверки подписи вебхука)
 */

var SH = { LEADS: 'Заявки', GROUPS: 'Группы', PAYMENTS: 'Оплаты', SETTINGS: 'Настройки' };
var PROGRAMS = { single: 'Разовая тренировка', pack8: 'Пакет 8 тренировок', transform: 'Трансформация 12 недель',
                 group: 'Jungle Group · 4 недели', nutrition: 'Консультация по питанию' };
var LEAD_HEADERS = ['ID','Дата','Программа','Сумма','Имя','Email','Телефон','Instagram','Цель','Уровень','Поток','Дни','Время',
                    'Часовой пояс','Заметки','Язык','Статус','Оплачено','Комментарий'];
var PAY_HEADERS = ['ID','Дата','Источник','Email','Имя','Продукт','Сумма','Валюта','Заявка','Внешний ID','Обработано'];
var LANGS = ['ru','en','uk','fr','de'];

/* ---------- GET: свободные места ---------- */
function doGet(e) {
  if (e && e.parameter && e.parameter.page === 'app') return studentPage_(); // приложение клиентки
  var action = (e && e.parameter && e.parameter.action) || '';
  if (action !== 'public') return json_({ ok: true });
  var cache = CacheService.getScriptCache();
  var hit = cache.get('public');
  if (hit) return ContentService.createTextOutput(hit).setMimeType(ContentService.MimeType.JSON);
  var sh = ss_().getSheetByName(SH.GROUPS), groups = [];
  if (sh && sh.getLastRow() > 1) {
    sh.getRange(2, 1, sh.getLastRow() - 1, 9).getValues().forEach(function (r) {
      if (!r[0] || String(r[8]).toLowerCase() === 'нет') return;
      groups.push({ id: String(r[0]), left: Math.max(0, (Number(r[5]) || 0) - (Number(r[6]) || 0)) });
    });
  }
  var out = JSON.stringify({ ok: true, groups: groups });
  cache.put('public', out, 120);
  return ContentService.createTextOutput(out).setMimeType(ContentService.MimeType.JSON);
}

/* ---------- POST: заявки и вебхуки ---------- */
function doPost(e) {
  var raw = (e && e.postData && e.postData.contents) || '';
  // PayPal IPN приходит как form-urlencoded
  if (/(^|&)txn_id=/.test(raw) || (e.postData && /x-www-form-urlencoded/.test(e.postData.type) && /(^|&)payment_status=/.test(raw))) {
    var l0 = LockService.getScriptLock(); l0.waitLock(20000);
    try { return handlePayPal_(raw); } catch (err) { console.error(err); return ContentService.createTextOutput('ERR'); } finally { l0.releaseLock(); }
  }
  var body;
  try { body = JSON.parse(raw); } catch (err) { return json_({ ok: false, error: 'bad json' }); }
  var lock = LockService.getScriptLock();
  if (!lock.tryLock(20000)) return json_({ ok: false, error: 'busy' });
  try {
    if (body && body.kind === 'lead') return handleLead_(body);
    if (body && body.type && ('signature' in body)) return handlePayhip_(body);
    return json_({ ok: false, error: 'unknown' });
  } catch (err) {
    console.error(err);
    return json_({ ok: false, error: 'server' });
  } finally {
    lock.releaseLock();
  }
}

function handleLead_(b) {
  var email = clean_(b.email, 120).toLowerCase();
  var name = clean_(b.name, 80);
  var phone = clean_(b.phone, 40);
  var program = String(b.program || '');
  if (!name || !phone || !/^[^@\s]+@[^@\s]+\.[^@\s]+$/.test(email) || !PROGRAMS[program]) return json_({ ok: false, error: 'invalid' });
  var id = /^L[A-Z0-9]{6,20}$/.test(String(b.id)) ? String(b.id) : 'L' + Date.now().toString(36).toUpperCase();

  // защита от спама: не чаще 1 заявки в минуту с одного email, не больше 60 в час всего
  var cache = CacheService.getScriptCache();
  if (cache.get('rl:' + email)) return json_({ ok: true, id: id, dup: true });
  var n = Number(cache.get('rl:all') || 0);
  if (n > 60) return json_({ ok: false, error: 'rate' });
  cache.put('rl:' + email, '1', 60); cache.put('rl:all', String(n + 1), 3600);

  var sh = sheet_(SH.LEADS, LEAD_HEADERS);
  sh.appendRow([id, new Date(), PROGRAMS[program], Number(b.price) || '', name, email, phone,
    clean_(b.instagram, 60), clean_(b.goal, 40), clean_(b.level, 40), clean_(b.group, 10), clean_(b.days, 80),
    clean_(b.times, 60), clean_(b.tz, 60), clean_(b.notes, 1500), (LANGS.indexOf(b.lang) > -1 ? b.lang : 'en').toUpperCase(), 'Новая', '', '']);

  var owner = setting_('OWNER_EMAIL');
  try { if (PropertiesService.getScriptProperties().getProperty('TELEGRAM_BOT_TOKEN')) notifyLera_('🌿 Новая заявка: ' + PROGRAMS[program] + ' — ' + name + ' · ' + phone); } catch (err) {}
  if (owner) {
    MailApp.sendEmail({
      to: owner, replyTo: email,
      subject: '🌿 Новая заявка: ' + PROGRAMS[program] + ' — ' + name,
      htmlBody: '<p><b>' + esc_(name) + '</b> · ' + esc_(email) + ' · ' + esc_(phone) + '</p>' +
        '<p>Программа: <b>' + esc_(PROGRAMS[program]) + '</b>' + (b.group ? ' · поток ' + esc_(b.group) : '') + '</p>' +
        '<p>Цель: ' + esc_(b.goal) + ' · Уровень: ' + esc_(b.level) + '<br>Дни: ' + esc_(b.days) + ' · Время: ' + esc_(b.times) +
        ' · Пояс: ' + esc_(b.tz) + '</p><p>Заметки: ' + esc_(b.notes) + '</p>' +
        '<p style="color:#888">Если программа с оплатой сразу — клиент сейчас на странице оплаты. Оплата появится в панели автоматически.</p>'
    });
  }
  var L = LANGS.indexOf(b.lang) > -1 ? b.lang : 'en';
  var M = {
    ru: ['Заявка получена 🌿', 'Привет, {n}!', 'Я получила твою заявку на «{p}». Свяжусь с тобой в течение 24 часов, чтобы согласовать расписание.'],
    uk: ['Заявку отримано 🌿', 'Привіт, {n}!', 'Я отримала твою заявку на «{p}». Зв’яжуся з тобою протягом 24 годин, щоб узгодити розклад.'],
    en: ['Request received 🌿', 'Hi {n}!', 'I received your request for “{p}”. I will contact you within 24 hours to set up the schedule.'],
    fr: ['Demande reçue 🌿', 'Salut {n} !', 'J’ai bien reçu ta demande pour « {p} ». Je te contacte sous 24 heures pour organiser le planning.'],
    de: ['Anfrage erhalten 🌿', 'Hi {n}!', 'Ich habe deine Anfrage für „{p}“ erhalten. Ich melde mich innerhalb von 24 Stunden, um den Zeitplan abzustimmen.']
  }[L];
  MailApp.sendEmail({
    to: email, name: setting_('BRAND') || 'Lera', replyTo: owner || undefined, subject: M[0],
    htmlBody: '<p>' + esc_(M[1].replace('{n}', name)) + '</p><p>' + esc_(M[2].replace('{p}', PROGRAMS[program])) + '</p><p>Lera</p>'
  });
  return json_({ ok: true, id: id });
}

function handlePayhip_(b) {
  var key = PropertiesService.getScriptProperties().getProperty('PAYHIP_API_KEY');
  if (key) {
    var expected = hex_(Utilities.computeDigest(Utilities.DigestAlgorithm.SHA_256, key, Utilities.Charset.UTF_8));
    if (String(b.signature) !== expected) return json_({ ok: false, error: 'signature' });
  }
  if (b.type !== 'paid') return json_({ ok: true, ignored: b.type });
  var sh = sheet_(SH.PAYMENTS, PAY_HEADERS);
  var ext = String(b.id || '');
  if (ext && sh.getLastRow() > 1) {
    var ids = sh.getRange(2, 10, sh.getLastRow() - 1, 1).getValues().map(function (r) { return String(r[0]); });
    if (ids.indexOf(ext) > -1) return json_({ ok: true, dup: true });
  }
  var items = Array.isArray(b.items) ? b.items : [];
  var product = items.map(function (i) { return i.product_name || i.name || i.product_key || ''; }).filter(String).join(' + ') || 'PDF';
  var amount = Number(b.price);
  if (setting_('PAYHIP_PRICE_IN_CENTS') !== 'нет' && isFinite(amount)) amount = amount / 100;
  sh.appendRow(['P' + Date.now().toString(36).toUpperCase(), new Date(), 'Payhip', clean_(b.email, 120), clean_(b.customer_name || '', 80),
    clean_(product, 200), isFinite(amount) ? amount : '', String(b.currency || 'USD').toUpperCase(), '', ext]);
  return json_({ ok: true });
}

/* ---------- PayPal IPN ---------- */
function handlePayPal_(raw) {
  // 1) проверяем у PayPal, что уведомление настоящее
  var v = UrlFetchApp.fetch('https://ipnpb.paypal.com/cgi-bin/webscr', {
    method: 'post', payload: 'cmd=_notify-validate&' + raw, contentType: 'application/x-www-form-urlencoded', muteHttpExceptions: true });
  if (v.getContentText().trim() !== 'VERIFIED') { console.warn('IPN not verified'); return ContentService.createTextOutput('IGNORED'); }
  var q = {};
  raw.split('&').forEach(function (kv) { var i = kv.indexOf('='); if (i > 0) q[decodeURIComponent(kv.slice(0, i))] = decodeURIComponent(kv.slice(i + 1).replace(/\+/g, ' ')); });
  if (q.payment_status !== 'Completed') return ContentService.createTextOutput('OK');
  var mine = setting_('PAYPAL_EMAIL').toLowerCase();
  if (mine && String(q.receiver_email || q.business || '').toLowerCase() !== mine) { console.warn('IPN receiver mismatch'); return ContentService.createTextOutput('IGNORED'); }
  var sh = sheet_(SH.PAYMENTS, PAY_HEADERS), txn = String(q.txn_id || '');
  if (txn && sh.getLastRow() > 1) {
    var ids = sh.getRange(2, 10, sh.getLastRow() - 1, 1).getValues().map(function (r) { return String(r[0]); });
    if (ids.indexOf(txn) > -1) return ContentService.createTextOutput('OK'); // PayPal шлёт повторы
  }
  var ref = /^L[A-Z0-9]{6,20}$/.test(q.custom || '') ? q.custom : '';
  sh.appendRow(['PP' + Date.now().toString(36).toUpperCase(), new Date(), 'PayPal', clean_(String(q.payer_email || '').toLowerCase(), 120),
    clean_(((q.first_name || '') + ' ' + (q.last_name || '')).trim(), 80), PROGRAMS[q.item_number] || clean_(q.item_name, 120),
    Number(q.mc_gross) || '', String(q.mc_currency || 'USD'), ref, txn, '']);
  if (ref) {
    var ls = ss_().getSheetByName(SH.LEADS);
    if (ls && ls.getLastRow() > 1) {
      var ids2 = ls.getRange(2, 1, ls.getLastRow() - 1, 1).getValues();
      for (var i = 0; i < ids2.length; i++) if (String(ids2[i][0]) === ref) {
        ls.getRange(i + 2, LEAD_HEADERS.indexOf('Статус') + 1).setValue('Оплачено');
        ls.getRange(i + 2, LEAD_HEADERS.indexOf('Оплачено') + 1).setValue((q.mc_gross || '') + ' ' + (q.mc_currency || '') + ' PayPal');
        break;
      }
    }
  }
  return ContentService.createTextOutput('OK');
}

/* ---------- helpers ---------- */
function ss_() { return SpreadsheetApp.getActiveSpreadsheet(); }
function sheet_(name, headers) {
  var ss = ss_(), sh = ss.getSheetByName(name);
  if (!sh) { sh = ss.insertSheet(name); sh.appendRow(headers); sh.setFrozenRows(1); }
  return sh;
}
function setting_(k) {
  var sh = ss_().getSheetByName(SH.SETTINGS);
  if (!sh || sh.getLastRow() < 2) return '';
  var v = sh.getRange(2, 1, sh.getLastRow() - 1, 2).getValues();
  for (var i = 0; i < v.length; i++) if (String(v[i][0]).trim() === k) return String(v[i][1]).trim();
  return '';
}
// Обрезает длину и защищает таблицу от «формул» во вводе (= + - @ в начале)
function clean_(v, max) {
  var s = String(v == null ? '' : v).replace(/[\u0000-\u0008\u000B\u000C\u000E-\u001F]/g, '').trim().slice(0, max || 200);
  return /^[=+\-@\t\r]/.test(s) ? "'" + s : s;
}
function esc_(s) { return String(s == null ? '' : s).replace(/[&<>"']/g, function (c) { return { '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;' }[c]; }); }
function hex_(bytes) { return bytes.map(function (b) { return ('0' + (b & 0xff).toString(16)).slice(-2); }).join(''); }
function json_(o) { return ContentService.createTextOutput(JSON.stringify(o)).setMimeType(ContentService.MimeType.JSON); }
