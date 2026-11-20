/**
 * VALERIIA CRM — ПРИЛОЖЕНИЕ КЛИЕНТКИ  (файл в проекте №1 «API», рядом с api.gs)
 * -----------------------------------------------------------------
 * Открывается по адресу  <URL веб-приложения API>?page=app
 * Вход: email → код из письма (6 цифр) → доступ на этом устройстве.
 *   • Войти может только клиентка со статусом «Активен» в листе «Клиенты».
 *   • Одновременно не больше 2 устройств: при входе на 3-м самое старое выходит.
 *   • Пароля нет — его нельзя «передать подруге»; код приходит только на почту владелицы.
 * Внутри: ближайшие занятия и Zoom, остаток пакета, чат с Лерой, материалы.
 */

var ST = { MSG: 'Сообщения', ACCESS: 'Доступ', CLIENTS: 'Клиенты', SESSIONS: 'Занятия', MATERIALS: 'Материалы' };
var ST_HEAD = {
  'Сообщения': ['ID', 'Дата', 'Email', 'От', 'Текст', 'Прочитано'],
  'Доступ':    ['Email', 'Тип', 'Хеш', 'До', 'Создан', 'Попыток', 'Устройство'],
  'Материалы': ['Название', 'Ссылка', 'Программы', 'Описание']
};
var MAX_DEVICES = 2;

/** Отдаёт HTML приложения (вызывается из doGet при ?page=app). */
function studentPage_() {
  return HtmlService.createHtmlOutputFromFile('student')
    .setTitle((setting_('BRAND') || 'Lera') + ' · App')
    .addMetaTag('viewport', 'width=device-width, initial-scale=1, viewport-fit=cover')
    .setXFrameOptionsMode(HtmlService.XFrameOptionsMode.ALLOWALL); // можно встроить на сайт (iframe)
}

/* ---------------- вход ---------------- */
function stRequestCode(email, lang) {
  email = String(email || '').trim().toLowerCase();
  if (!/^[^@\s]+@[^@\s]+\.[^@\s]+$/.test(email)) return { ok: false, error: 'email' };
  var cache = CacheService.getScriptCache();
  if (cache.get('code:' + email)) return { ok: true }; // не чаще раза в минуту
  cache.put('code:' + email, '1', 60);
  var client = stClient_(email);
  if (!client || client['Статус'] !== 'Активен') return { ok: true }; // не раскрываем, есть ли такой email
  var code = String(Math.floor(100000 + Math.random() * 900000));
  withLock_(function () {
    var sh = stSheet_(ST.ACCESS);
    stDeleteRows_(sh, function (r) { return r[0] === email && r[1] === 'code'; });
    sh.appendRow([email, 'code', sha_(code + email), new Date(Date.now() + 10 * 60000), new Date(), 0, '']);
  });
  var T = {
    ru: ['Код для входа', 'Твой код для входа в приложение Леры:', 'Код действует 10 минут. Если это была не ты — просто проигнорируй письмо.'],
    uk: ['Код для входу', 'Твій код для входу в застосунок Лери:', 'Код дійсний 10 хвилин. Якщо це була не ти — просто проігноруй лист.'],
    en: ['Your login code', 'Your code for Lera’s app:', 'The code is valid for 10 minutes. If this wasn’t you, just ignore this email.'],
    fr: ['Ton code de connexion', 'Ton code pour l’app de Lera :', 'Le code est valable 10 minutes. Si ce n’était pas toi, ignore cet e-mail.'],
    de: ['Dein Login-Code', 'Dein Code für Leras App:', 'Der Code ist 10 Minuten gültig. Wenn du das nicht warst, ignoriere diese E-Mail.']
  }[lang] || ['Code / Код', 'Your code / Твой код:', '10 min.'];
  MailApp.sendEmail({ to: email, name: setting_('BRAND') || 'Lera', subject: T[0] + ': ' + code,
    htmlBody: '<div style="font-family:Arial,sans-serif"><p>' + T[1] + '</p><p style="font-size:32px;letter-spacing:6px;font-weight:bold">' + code + '</p><p style="color:#777">' + T[2] + '</p></div>' });
  return { ok: true };
}

function stVerify(email, code, device) {
  email = String(email || '').trim().toLowerCase(); code = String(code || '').replace(/\D/g, '');
  var result = { ok: false, error: 'code' };
  withLock_(function () {
    var sh = stSheet_(ST.ACCESS), n = sh.getLastRow() - 1; if (n < 1) return;
    var data = sh.getRange(2, 1, n, 7).getValues();
    for (var i = 0; i < data.length; i++) {
      var r = data[i]; if (r[0] !== email || r[1] !== 'code') continue;
      if (new Date(r[3]) < new Date() || Number(r[5]) >= 5) { sh.deleteRow(i + 2); result.error = 'expired'; return; }
      if (r[2] !== sha_(code + email)) { sh.getRange(i + 2, 6).setValue(Number(r[5]) + 1); return; }
      sh.deleteRow(i + 2);
      // лимит устройств
      var tokens = sh.getLastRow() > 1 ? sh.getRange(2, 1, sh.getLastRow() - 1, 7).getValues()
        .map(function (x, j) { return { row: j + 2, email: x[0], type: x[1], created: new Date(x[4]) }; })
        .filter(function (x) { return x.email === email && x.type === 'token'; })
        .sort(function (a, b) { return a.created - b.created; }) : [];
      while (tokens.length >= MAX_DEVICES) { var old = tokens.shift(); sh.deleteRow(old.row); tokens.forEach(function (t) { if (t.row > old.row) t.row--; }); }
      var token = Utilities.getUuid().replace(/-/g, '') + Utilities.getUuid().replace(/-/g, '');
      sh.appendRow([email, 'token', sha_(token), new Date(Date.now() + 90 * 864e5), new Date(), 0, clean_(device, 120)]);
      result = { ok: true, token: token };
      return;
    }
  });
  return result;
}

function stLogout(token) {
  var h = sha_(String(token || ''));
  withLock_(function () { stDeleteRows_(stSheet_(ST.ACCESS), function (r) { return r[1] === 'token' && r[2] === h; }); });
  return { ok: true };
}

/* ---------------- данные ---------------- */
function stData(token) {
  var email = stAuth_(token); if (!email) return { ok: false, error: 'auth' };
  var c = stClient_(email) || {};
  var tz = Session.getScriptTimeZone(), today = Utilities.formatDate(new Date(), tz, 'yyyy-MM-dd');
  var sessions = stRows_(ST.SESSIONS).filter(function (s) { return String(s.Email).toLowerCase() === email && s['Статус'] === 'Запланировано'; })
    .map(function (s) { return { date: fmt_(s['Дата'], 'yyyy-MM-dd'), time: s['Время'] instanceof Date ? fmt_(s['Время'], 'HH:mm') : String(s['Время']).slice(0, 5),
      min: +s['Мин'] || 60, type: s['Тип'], link: s['Ссылка'] || setting_('ZOOM_LINK') }; })
    .filter(function (s) { return s.date >= today; })
    .sort(function (a, b) { return (a.date + a.time).localeCompare(b.date + b.time); }).slice(0, 20);
  var prog = String(c['Программа'] || '');
  var materials = stRows_(ST.MATERIALS).filter(function (m) {
    var p = String(m['Программы'] || 'все').toLowerCase(); return p === 'все' || p === 'all' || p.indexOf(prog.toLowerCase()) > -1;
  }).map(function (m) { return { title: m['Название'], url: m['Ссылка'], desc: m['Описание'] }; })
    .filter(function (m) { return /^https:\/\//.test(m.url); });
  var group = String(c['Поток'] || ''), groupInfo = null;
  if (group) {
    var g = stRows_('Группы').filter(function (x) { return x.ID === group; })[0];
    if (g) groupInfo = { name: g['Название'], days: g['Дни'], time: g['Время'] instanceof Date ? fmt_(g['Время'], 'HH:mm') : String(g['Время']), zoom: setting_('ZOOM_LINK') };
  }
  return { ok: true, me: { email: email, name: c['Имя'] || '', program: prog, total: +c['Занятий всего'] || 0, done: +c['Проведено'] || 0, left: +c['Осталось'] || 0, group: groupInfo },
    tz: tz, sessions: sessions, materials: materials, messages: stThread_(email, 0), coach: { name: setting_('BRAND') || 'Lera' } };
}

/** Новые сообщения после lastId (для обновления чата каждые несколько секунд). */
function stPoll(token, lastId) {
  var email = stAuth_(token, true); if (!email) return { ok: false, error: 'auth' };
  return { ok: true, messages: stThread_(email, Number(lastId) || 0) };
}

function stSend(token, text) {
  var email = stAuth_(token, true); if (!email) return { ok: false, error: 'auth' };
  text = clean_(String(text || ''), 2000); if (!text) return { ok: false, error: 'empty' };
  var cache = CacheService.getScriptCache(), k = 'msgrate:' + email, n = Number(cache.get(k) || 0);
  if (n > 20) return { ok: false, error: 'rate' }; cache.put(k, String(n + 1), 300);
  var id;
  withLock_(function () { id = Date.now(); stSheet_(ST.MSG).appendRow([id, new Date(), email, 'client', text, '']); });
  // уведомление Лере — не чаще раза в 10 минут на одну клиентку
  if (!cache.get('ntf:' + email)) {
    cache.put('ntf:' + email, '1', 600);
    var c = stClient_(email) || {};
    notifyLera_('💬 ' + (c['Имя'] || email) + ': ' + text.slice(0, 300));
  }
  return { ok: true, messages: stThread_(email, id - 1) };
}

/* ---------------- helpers ---------------- */
function stThread_(email, afterId) {
  var sh = stSheet_(ST.MSG), n = sh.getLastRow() - 1; if (n < 1) return [];
  var out = [], toMark = [];
  sh.getRange(2, 1, n, 6).getValues().forEach(function (r, i) {
    if (String(r[2]).toLowerCase() !== email || Number(r[0]) <= afterId) return;
    out.push({ id: Number(r[0]), at: fmt_(r[1], "yyyy-MM-dd'T'HH:mm"), from: r[3], text: String(r[4]) });
    if (r[3] === 'lera' && !r[5]) toMark.push(i + 2);
  });
  toMark.forEach(function (row) { sh.getRange(row, 6).setValue('да'); }); // клиентка прочитала ответы Леры
  return out.slice(-200);
}
function stAuth_(token, quick) {
  token = String(token || ''); if (token.length < 40) return null;
  var h = sha_(token), cache = CacheService.getScriptCache(), hit = cache.get('tok:' + h);
  if (hit) return hit;
  var sh = stSheet_(ST.ACCESS), n = sh.getLastRow() - 1; if (n < 1) return null;
  var data = sh.getRange(2, 1, n, 7).getValues();
  for (var i = 0; i < data.length; i++) {
    var r = data[i];
    if (r[1] === 'token' && r[2] === h) {
      if (new Date(r[3]) < new Date()) return null;
      var c = stClient_(r[0]); if (!c || (c['Статус'] !== 'Активен' && c['Статус'] !== 'Завершён')) return null;
      cache.put('tok:' + h, r[0], 300);
      return r[0];
    }
  }
  return null;
}
function stClient_(email) {
  return stRows_(ST.CLIENTS).filter(function (c) { return String(c.Email).toLowerCase() === email; })[0] || null;
}
function stSheet_(name) {
  var ss = ss_(), sh = ss.getSheetByName(name);
  if (!sh) { sh = ss.insertSheet(name); if (ST_HEAD[name]) { sh.appendRow(ST_HEAD[name]); sh.setFrozenRows(1); } }
  return sh;
}
function stRows_(name) {
  var sh = ss_().getSheetByName(name); if (!sh || sh.getLastRow() < 2) return [];
  var h = sh.getRange(1, 1, 1, sh.getLastColumn()).getValues()[0];
  return sh.getRange(2, 1, sh.getLastRow() - 1, h.length).getValues().filter(function (r) { return r[0] !== ''; })
    .map(function (r) { var o = {}; h.forEach(function (k, i) { o[k] = r[i]; }); return o; });
}
function stDeleteRows_(sh, pred) {
  var n = sh.getLastRow() - 1; if (n < 1) return;
  var data = sh.getRange(2, 1, n, sh.getLastColumn()).getValues();
  for (var i = data.length - 1; i >= 0; i--) if (pred(data[i])) sh.deleteRow(i + 2);
}
function withLock_(fn) { var l = LockService.getScriptLock(); l.waitLock(20000); try { fn(); } finally { l.releaseLock(); } }
function sha_(s) { return hex_(Utilities.computeDigest(Utilities.DigestAlgorithm.SHA_256, String(s), Utilities.Charset.UTF_8)); }
function fmt_(v, f) { return v instanceof Date ? Utilities.formatDate(v, Session.getScriptTimeZone(), f) : String(v || ''); }

/** Уведомление Лере: в Telegram (если настроен бот) и/или на email. */
function notifyLera_(text) {
  var tok = PropertiesService.getScriptProperties().getProperty('TELEGRAM_BOT_TOKEN'), chat = setting_('TELEGRAM_CHAT_ID');
  if (tok && chat) {
    try { UrlFetchApp.fetch('https://api.telegram.org/bot' + tok + '/sendMessage', { method: 'post', payload: { chat_id: chat, text: text }, muteHttpExceptions: true }); return; }
    catch (err) { console.warn(err); }
  }
  var owner = setting_('OWNER_EMAIL'); if (owner) MailApp.sendEmail(owner, text.slice(0, 80), text + '\n\nОткрой панель, чтобы ответить.');
}
