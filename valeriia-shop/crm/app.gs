/**
 * VALERIIA CRM — ПАНЕЛЬ ЛЕРЫ  (проект №2, отдельный, приватный)
 * -----------------------------------------------------------------
 * • Приложение-панель (открывается с телефона): заявки, клиенты, занятия, деньги, группы.
 * • Каждые 15 минут забирает оплаты из Stripe и сама отмечает: кто оплатил, сколько занятий.
 * • Каждое утро в 08:00 присылает Лере письмо-сводку на день.
 * • Создаёт события в Google Календаре с приглашением клиенту (напоминания приходят сами).
 *
 * Развёртывание: Deploy → New deployment → Web app
 *   Execute as: Me   ·   Who has access: Only myself      ← панель видит только Лера
 *
 * Свойства скрипта (Project Settings → Script properties):
 *   SHEET_ID           — ID Google-таблицы (из её адреса)
 *   STRIPE_SECRET_KEY  — restricted key Stripe (только чтение Checkout Sessions)
 * Первый запуск: выбрать функцию setup → Run → разрешить доступ.
 */

var SH = { LEADS: 'Заявки', CLIENTS: 'Клиенты', SESSIONS: 'Занятия', PAYMENTS: 'Оплаты', GROUPS: 'Группы', PROGRAMS: 'Программы', SETTINGS: 'Настройки' };
var HEAD = {
  'Заявки':    ['ID','Дата','Программа','Сумма','Имя','Email','Телефон','Instagram','Цель','Уровень','Поток','Дни','Время','Часовой пояс','Заметки','Язык','Статус','Оплачено','Комментарий'],
  'Клиенты':   ['Email','Имя','Телефон','Программа','Поток','Занятий всего','Проведено','Осталось','Начало','Статус','Заметки'],
  'Занятия':   ['ID','Дата','Время','Мин','Email','Имя','Тип','Статус','Ссылка','Событие','Заметки'],
  'Оплаты':    ['ID','Дата','Источник','Email','Имя','Продукт','Сумма','Валюта','Заявка','Внешний ID','Обработано'],
  'Группы':    ['ID','Название','Дни','Время','Старт','Мест','Занято','Событие','Активна'],
  'Программы': ['ID','Название','Цена','Занятий','Минут','Тип','Stripe Link ID','Активна'],
  'Настройки': ['Ключ','Значение','Пояснение']
};
var LEAD_STATUSES = ['Новая','Связаться','Оплачено','В работе','Лист ожидания','Отказ','Архив'];

/* ================= УСТАНОВКА ================= */
function setup() {
  var ss = ss_();
  Object.keys(HEAD).forEach(function (name) {
    var sh = ss.getSheetByName(name) || ss.insertSheet(name);
    if (sh.getLastRow() === 0) sh.appendRow(HEAD[name]);
    sh.setFrozenRows(1);
    sh.getRange(1, 1, 1, HEAD[name].length).setFontWeight('bold').setBackground('#132017').setFontColor('#D7B98A');
    sh.setTabColor('#5E7F4F');
  });
  var leads = ss.getSheetByName(SH.LEADS);
  leads.getRange('Q2:Q').setDataValidation(SpreadsheetApp.newDataValidation().requireValueInList(LEAD_STATUSES, true).build());
  leads.getRange('B2:B').setNumberFormat('dd.mm.yyyy hh:mm');
  ss.getSheetByName(SH.PAYMENTS).getRange('B2:B').setNumberFormat('dd.mm.yyyy hh:mm');
  ss.getSheetByName(SH.SESSIONS).getRange('B2:B').setNumberFormat('dd.mm.yyyy');
  // время храним текстом, чтобы Таблицы не превращали «07:30» в дату 1899 года
  ss.getSheetByName(SH.SESSIONS).getRange('C2:C').setNumberFormat('@');
  ss.getSheetByName(SH.GROUPS).getRange('D2:D').setNumberFormat('@');
  ss.getSheetByName(SH.CLIENTS).getRange('C2:C').setNumberFormat('@');
  leads.getRange('G2:G').setNumberFormat('@');

  seed_(SH.PROGRAMS, [
    ['single', 'Разовая тренировка', 110, 1, 60, 'personal', '', 'да'],
    ['pack8', 'Пакет 8 тренировок', 800, 8, 60, 'personal', '', 'да'],
    ['transform', 'Трансформация 12 недель', 2400, 24, 60, 'personal', '', 'да'],
    ['group', 'Jungle Group · 4 недели', 169, 12, 45, 'group', '', 'да'],
    ['nutrition', 'Консультация по питанию', 180, 1, 75, 'nutrition', '', 'да']
  ]);
  seed_(SH.GROUPS, [
    ['G-AM', 'Дневной поток', 'Пн, Ср, Пт', '14:00', '', 8, 0, '', 'да'],
    ['G-PM', 'Вечерний поток', 'Пн, Ср, Пт', '19:00', '', 8, 0, '', 'да']
  ]);
  seed_(SH.SETTINGS, [
    ['OWNER_EMAIL', Session.getEffectiveUser().getEmail(), 'Куда присылать уведомления и сводку'],
    ['BRAND', 'Valeriia', 'Имя в письмах'],
    ['ZOOM_LINK', '', 'Постоянная ссылка Zoom для занятий'],
    ['PAYPAL_EMAIL', '', 'Email PayPal-аккаунта Леры (для проверки оплат)'],
    ['CALENDAR_ID', '', 'Пусто = основной календарь Леры'],
    ['DIGEST_HOUR', '8', 'Во сколько присылать утреннюю сводку'],
    ['PAYHIP_PRICE_IN_CENTS', 'да', 'Payhip присылает цену в центах? (проверить по первой продаже)'],
    ['LAST_STRIPE_SYNC', '', 'Служебное — не трогать']
  ]);
  // триггеры
  ScriptApp.getProjectTriggers().forEach(function (t) { ScriptApp.deleteTrigger(t); });
  ScriptApp.newTrigger('syncStripe').timeBased().everyMinutes(15).create();
  ScriptApp.newTrigger('dailyDigest').timeBased().atHour(Number(setting_('DIGEST_HOUR')) || 8).everyDays(1).create();
  return 'Готово';
}
function seed_(name, rows) {
  var sh = ss_().getSheetByName(name);
  if (sh.getLastRow() > 1) return;
  sh.getRange(2, 1, rows.length, rows[0].length).setValues(rows);
}

/* ================= ПАНЕЛЬ ================= */
function doGet() {
  return HtmlService.createHtmlOutputFromFile('app')
    .setTitle('Lera · Панель')
    .addMetaTag('viewport', 'width=device-width, initial-scale=1, viewport-fit=cover')
    .setFaviconUrl('https://fonts.gstatic.com/s/i/short-term/release/materialsymbolsoutlined/eco/default/24px.svg');
}

/** Все данные для панели одним запросом. */
function getDashboard() {
  var tz = Session.getScriptTimeZone(), now = new Date();
  var today = Utilities.formatDate(now, tz, 'yyyy-MM-dd'), month = today.slice(0, 7);
  var leads = rows_(SH.LEADS).map(function (r) { return {
    id: r.ID, date: iso_(r['Дата']), program: r['Программа'], price: r['Сумма'], name: r['Имя'], email: r.Email, phone: r['Телефон'],
    ig: r.Instagram, goal: r['Цель'], level: r['Уровень'], group: r['Поток'], days: r['Дни'], times: r['Время'], tz: r['Часовой пояс'],
    notes: r['Заметки'], lang: r['Язык'], status: r['Статус'], paid: r['Оплачено'], comment: r['Комментарий'] }; }).reverse();
  var clients = rows_(SH.CLIENTS).map(function (r) { return {
    email: r.Email, name: r['Имя'], phone: r['Телефон'], program: r['Программа'], group: r['Поток'], total: +r['Занятий всего'] || 0,
    done: +r['Проведено'] || 0, left: +r['Осталось'] || 0, start: iso_(r['Начало']), status: r['Статус'], notes: r['Заметки'] }; });
  var sessions = rows_(SH.SESSIONS).map(function (r) { return {
    id: r.ID, date: iso_(r['Дата']).slice(0, 10), time: hhmm_(r['Время']), min: +r['Мин'] || 60, email: r.Email, name: r['Имя'],
    type: r['Тип'], status: r['Статус'], link: r['Ссылка'], notes: r['Заметки'] }; })
    .filter(function (s) { return s.date >= today || s.status === 'Запланировано'; })
    .sort(function (a, b) { return (a.date + a.time).localeCompare(b.date + b.time); });
  var payments = rows_(SH.PAYMENTS).map(function (r) { return {
    id: r.ID, date: iso_(r['Дата']), source: r['Источник'], email: r.Email, name: r['Имя'], product: r['Продукт'], amount: +r['Сумма'] || 0, currency: r['Валюта'] }; }).reverse();
  var groups = rows_(SH.GROUPS).map(function (r) { return {
    id: r.ID, name: r['Название'], days: r['Дни'], time: hhmm_(r['Время']), start: iso_(r['Старт']).slice(0, 10), cap: +r['Мест'] || 0, taken: +r['Занято'] || 0, active: r['Активна'] }; });
  var monthSum = payments.filter(function (p) { return p.date.slice(0, 7) === month; }).reduce(function (s, p) { return s + p.amount; }, 0);
  return {
    today: today, tz: tz, leads: leads.slice(0, 200), clients: clients, sessions: sessions.slice(0, 200), payments: payments.slice(0, 200), groups: groups,
    kpi: {
      month: Math.round(monthSum), newLeads: leads.filter(function (l) { return l.status === 'Новая' || l.status === 'Связаться'; }).length,
      todaySessions: sessions.filter(function (s) { return s.date === today && s.status === 'Запланировано'; }).length,
      activeClients: clients.filter(function (c) { return c.status === 'Активен'; }).length,
      lowClients: clients.filter(function (c) { return c.status === 'Активен' && c.left <= 1; }).length
    },
    programs: rows_(SH.PROGRAMS).map(function (r) { return { id: r.ID, name: r['Название'], sessions: +r['Занятий'] || 1, min: +r['Минут'] || 60, type: r['Тип'] }; }),
    zoom: setting_('ZOOM_LINK')
  };
}

function setLeadStatus(id, status, comment) {
  if (LEAD_STATUSES.indexOf(status) < 0) throw new Error('Неизвестный статус');
  var f = find_(SH.LEADS, 'ID', id); if (!f) throw new Error('Заявка не найдена');
  f.sheet.getRange(f.row, col_(SH.LEADS, 'Статус')).setValue(status);
  if (comment != null) f.sheet.getRange(f.row, col_(SH.LEADS, 'Комментарий')).setValue(clean_(comment, 1000));
  return true;
}

/** Ручное добавление клиента из заявки (например, оплатила переводом). */
function activateLead(id) {
  var f = find_(SH.LEADS, 'ID', id); if (!f) throw new Error('Заявка не найдена');
  var l = f.obj, prog = programByName_(l['Программа']);
  upsertClient_(l.Email, l['Имя'], l['Телефон'], l['Программа'], l['Поток'], prog ? prog.sessions : 1);
  f.sheet.getRange(f.row, col_(SH.LEADS, 'Статус')).setValue('В работе');
  return true;
}

/** Новое занятие: строка в таблице + событие в календаре с приглашением клиенту. */
function addSession(o) {
  if (!o || !/^\d{4}-\d{2}-\d{2}$/.test(o.date) || !/^\d{2}:\d{2}$/.test(o.time)) throw new Error('Дата/время');
  var min = Math.max(15, Math.min(240, Number(o.min) || 60));
  var c = o.email ? find_(SH.CLIENTS, 'Email', String(o.email).toLowerCase()) : null;
  var name = clean_(o.name || (c && c.obj['Имя']) || '', 80);
  var start = parseLocal_(o.date, o.time), end = new Date(start.getTime() + min * 60000);
  var zoom = setting_('ZOOM_LINK'), eventId = '';
  try {
    var cal = setting_('CALENDAR_ID') ? CalendarApp.getCalendarById(setting_('CALENDAR_ID')) : CalendarApp.getDefaultCalendar();
    var ev = cal.createEvent((o.type || 'Тренировка') + ' · ' + name, start, end, {
      description: 'Тренировка с Лерой' + (zoom ? '\nZoom: ' + zoom : '') + (o.notes ? '\n\n' + o.notes : ''),
      location: zoom || 'Online', guests: o.email || '', sendInvites: !!o.email });
    ev.addPopupReminder(60); ev.addEmailReminder(24 * 60);
    eventId = ev.getId();
  } catch (err) { console.warn('calendar', err); }
  var id = 'S' + Date.now().toString(36).toUpperCase();
  sheet_(SH.SESSIONS).appendRow([id, start, o.time, min, String(o.email || '').toLowerCase(), name, clean_(o.type || 'Тренировка', 40), 'Запланировано', zoom, eventId, clean_(o.notes, 500)]);
  return id;
}

/** Статус занятия: Проведено / Отменено / Неявка. Проведено и Неявка списывают занятие из пакета. */
function setSessionStatus(id, status) {
  if (['Запланировано','Проведено','Отменено','Неявка'].indexOf(status) < 0) throw new Error('Статус');
  var f = find_(SH.SESSIONS, 'ID', id); if (!f) throw new Error('Занятие не найдено');
  var prev = f.obj['Статус'];
  f.sheet.getRange(f.row, col_(SH.SESSIONS, 'Статус')).setValue(status);
  var counts = function (s) { return s === 'Проведено' || s === 'Неявка'; };
  if (counts(status) !== counts(prev) && f.obj.Email) changeDone_(f.obj.Email, counts(status) ? 1 : -1);
  if (status === 'Отменено' && f.obj['Событие']) {
    try { CalendarApp.getEventById(f.obj['Событие']).deleteEvent(); } catch (err) { console.warn(err); }
  }
  return true;
}

/** Оплата вручную (наличные, перевод). */
function addPayment(o) {
  var amount = Number(o && o.amount);
  if (!isFinite(amount) || amount <= 0) throw new Error('Сумма');
  sheet_(SH.PAYMENTS).appendRow(['M' + Date.now().toString(36).toUpperCase(), new Date(), 'Вручную', clean_(String(o.email || '').toLowerCase(), 120),
    clean_(o.name, 80), clean_(o.product, 120), amount, clean_(o.currency || 'USD', 5), '', '', 'да']);
  return true;
}

/** Создаёт в календаре серию занятий группы (Пн/Ср/Пт, 4 недели) и приглашает всех участниц потока. */
function createGroupSeries(groupId, startDate) {
  var f = find_(SH.GROUPS, 'ID', groupId); if (!f) throw new Error('Группа не найдена');
  if (!/^\d{4}-\d{2}-\d{2}$/.test(startDate)) throw new Error('Дата старта');
  var g = f.obj, time = hhmm_(g['Время']), prog = programById_('group');
  var start = parseLocal_(startDate, time), end = new Date(start.getTime() + (prog ? prog.min : 45) * 60000);
  var until = new Date(start.getTime() + 28 * 864e5);
  var guests = rows_(SH.CLIENTS).filter(function (c) { return c['Поток'] === groupId && c['Статус'] === 'Активен'; }).map(function (c) { return c.Email; });
  var zoom = setting_('ZOOM_LINK');
  var cal = setting_('CALENDAR_ID') ? CalendarApp.getCalendarById(setting_('CALENDAR_ID')) : CalendarApp.getDefaultCalendar();
  var rec = CalendarApp.newRecurrence().addWeeklyRule().onlyOnWeekdays([CalendarApp.Weekday.MONDAY, CalendarApp.Weekday.WEDNESDAY, CalendarApp.Weekday.FRIDAY]).until(until);
  var series = cal.createEventSeries('Jungle Group · ' + g['Название'], start, end, rec,
    { description: 'Групповая тренировка с Лерой' + (zoom ? '\nZoom: ' + zoom : ''), location: zoom || 'Online', guests: guests.join(','), sendInvites: true });
  series.addPopupReminder(60);
  f.sheet.getRange(f.row, col_(SH.GROUPS, 'Событие')).setValue(series.getId());
  f.sheet.getRange(f.row, col_(SH.GROUPS, 'Старт')).setValue(parseLocal_(startDate, '00:00'));
  return guests.length;
}

/* ================= STRIPE (каждые 15 минут) ================= */
function syncStripe() {
  processPending_(); // оплаты PayPal, которые API записал в таблицу
  var key = PropertiesService.getScriptProperties().getProperty('STRIPE_SECRET_KEY');
  if (!key) return 'Нет STRIPE_SECRET_KEY';
  var lock = LockService.getScriptLock(); if (!lock.tryLock(30000)) return 'busy';
  try {
    var last = Number(setting_('LAST_STRIPE_SYNC')) || Math.floor(Date.now() / 1000) - 7 * 86400;
    var since = last - 3600, newest = last, after = null, added = 0;
    var pay = sheet_(SH.PAYMENTS);
    var known = {};
    if (pay.getLastRow() > 1) pay.getRange(2, 10, pay.getLastRow() - 1, 1).getValues().forEach(function (r) { known[r[0]] = 1; });
    var links = {};
    rows_(SH.PROGRAMS).forEach(function (p) { if (p['Stripe Link ID']) links[String(p['Stripe Link ID']).trim()] = p; });
    do {
      var url = 'https://api.stripe.com/v1/checkout/sessions?limit=100&status=complete&created[gte]=' + since + (after ? '&starting_after=' + after : '');
      var res = UrlFetchApp.fetch(url, { headers: { Authorization: 'Bearer ' + key }, muteHttpExceptions: true });
      if (res.getResponseCode() !== 200) throw new Error('Stripe ' + res.getResponseCode() + ': ' + res.getContentText().slice(0, 200));
      var data = JSON.parse(res.getContentText());
      data.data.forEach(function (s) {
        newest = Math.max(newest, s.created);
        if (known[s.id] || s.payment_status !== 'paid') return;
        var prog = links[s.payment_link] || null;
        var email = String((s.customer_details && s.customer_details.email) || s.customer_email || '').toLowerCase();
        var name = (s.customer_details && s.customer_details.name) || '';
        var ref = s.client_reference_id || '';
        pay.appendRow(['T' + Date.now().toString(36).toUpperCase() + added, new Date(s.created * 1000), 'Stripe', email, clean_(name, 80),
          prog ? prog['Название'] : (s.payment_link || 'Stripe'), (s.amount_total || 0) / 100, String(s.currency || '').toUpperCase(), ref, s.id, 'да']);
        known[s.id] = 1; added++;
        onPaid_(email, name, prog, ref, (s.amount_total || 0) / 100, String(s.currency || '').toUpperCase());
      });
      after = data.has_more && data.data.length ? data.data[data.data.length - 1].id : null;
    } while (after);
    setSetting_('LAST_STRIPE_SYNC', String(newest));
    return 'Новых оплат: ' + added;
  } finally { lock.releaseLock(); }
}

/** Оплаты PayPal: API только записывает строку, а здесь создаётся клиент, места в группе и т.д. */
function processPending_() {
  var sh = sheet_(SH.PAYMENTS), n = sh.getLastRow() - 1; if (n < 1) return;
  var data = sh.getRange(2, 1, n, HEAD['Оплаты'].length).getValues();
  var progs = rows_(SH.PROGRAMS), col = col_(SH.PAYMENTS, 'Обработано');
  data.forEach(function (r, i) {
    if (r[2] !== 'PayPal' || r[10]) return;
    var lead = r[8] ? find_(SH.LEADS, 'ID', r[8]) : null;
    var pname = (lead && lead.obj['Программа']) || r[5];
    var prog = progs.filter(function (p) { return p['Название'] === pname; })[0] || null;
    sh.getRange(i + 2, col).setValue('да');
    onPaid_(String(r[3]).toLowerCase(), r[4], prog, r[8], Number(r[6]) || 0, r[7]);
  });
}

function onPaid_(email, name, prog, ref, amount, cur) {
  var lead = ref ? find_(SH.LEADS, 'ID', ref) : null;
  var group = lead ? lead.obj['Поток'] : '';
  var phone = lead ? lead.obj['Телефон'] : '';
  if (lead) {
    lead.sheet.getRange(lead.row, col_(SH.LEADS, 'Статус')).setValue('Оплачено');
    lead.sheet.getRange(lead.row, col_(SH.LEADS, 'Оплачено')).setValue(amount + ' ' + cur);
    if (!name) name = lead.obj['Имя'];
  }
  if (prog) {
    upsertClient_(email, name, phone, prog['Название'], group, Number(prog['Занятий']) || 1);
    if (prog['Тип'] === 'group' && group) {
      var g = find_(SH.GROUPS, 'ID', group);
      if (g) {
        g.sheet.getRange(g.row, col_(SH.GROUPS, 'Занято')).setValue((Number(g.obj['Занято']) || 0) + 1);
        if (g.obj['Событие']) { try { CalendarApp.getEventSeriesById(g.obj['Событие']).addGuest(email); } catch (err) { console.warn(err); } }
      }
    }
  }
  var owner = setting_('OWNER_EMAIL');
  if (owner) MailApp.sendEmail(owner, '💰 Оплата ' + amount + ' ' + cur + ' — ' + (name || email),
    (prog ? prog['Название'] : 'Stripe') + '\n' + email + (group ? '\nПоток: ' + group : '') +
    '\n\nОткрой панель, чтобы поставить занятия в календарь.');
}

/* ================= УТРЕННЯЯ СВОДКА ================= */
function dailyDigest() {
  var d = getDashboard(), owner = setting_('OWNER_EMAIL'); if (!owner) return;
  var today = d.sessions.filter(function (s) { return s.date === d.today && s.status === 'Запланировано'; });
  var newLeads = d.leads.filter(function (l) { return l.status === 'Новая' || l.status === 'Связаться'; });
  var unscheduled = d.clients.filter(function (c) {
    return c.status === 'Активен' && !c.group && !d.sessions.some(function (s) { return s.email === c.email && s.status === 'Запланировано'; });
  });
  var low = d.clients.filter(function (c) { return c.status === 'Активен' && c.left <= 1; });
  if (!today.length && !newLeads.length && !unscheduled.length && !low.length) return;
  var li = function (arr, f) { return arr.length ? '<ul>' + arr.map(function (x) { return '<li>' + f(x) + '</li>'; }).join('') + '</ul>' : '<p style="color:#888">—</p>'; };
  var html = '<div style="font-family:Arial,sans-serif;max-width:560px">' +
    '<h2 style="margin:0 0 4px">Доброе утро, Лера 🌿</h2><p style="color:#666;margin:0 0 18px">' + d.today + '</p>' +
    '<h3>Сегодня занятий: ' + today.length + '</h3>' + li(today, function (s) { return '<b>' + s.time + '</b> · ' + esc_(s.name) + ' · ' + esc_(s.type) + ' (' + s.min + ' мин)'; }) +
    '<h3>Ответить на заявки: ' + newLeads.length + '</h3>' + li(newLeads, function (l) { return esc_(l.name) + ' — ' + esc_(l.program) + ' · ' + esc_(l.phone); }) +
    '<h3>Оплатили, но нет занятий в календаре: ' + unscheduled.length + '</h3>' + li(unscheduled, function (c) { return esc_(c.name) + ' — ' + esc_(c.program); }) +
    '<h3>Заканчивается пакет (предложи продление): ' + low.length + '</h3>' + li(low, function (c) { return esc_(c.name) + ' — осталось ' + c.left; }) +
    '<p style="color:#666">Доход за месяц: <b>$' + d.kpi.month + '</b></p>' +
    '<p><a href="' + ScriptApp.getService().getUrl() + '">Открыть панель →</a></p></div>';
  MailApp.sendEmail({ to: owner, subject: '🌿 План на сегодня: ' + today.length + ' занятий, ' + newLeads.length + ' заявок', htmlBody: html });
}

/* ================= helpers ================= */
function ss_() {
  var id = PropertiesService.getScriptProperties().getProperty('SHEET_ID');
  if (!id) throw new Error('Укажите SHEET_ID в свойствах скрипта');
  return SpreadsheetApp.openById(id);
}
function sheet_(name) {
  var sh = ss_().getSheetByName(name);
  if (!sh) { sh = ss_().insertSheet(name); sh.appendRow(HEAD[name]); sh.setFrozenRows(1); }
  return sh;
}
function rows_(name) {
  var sh = sheet_(name), n = sh.getLastRow() - 1; if (n < 1) return [];
  var h = sh.getRange(1, 1, 1, sh.getLastColumn()).getValues()[0];
  return sh.getRange(2, 1, n, h.length).getValues().filter(function (r) { return r[0] !== ''; }).map(function (r) {
    var o = {}; h.forEach(function (k, i) { o[k] = r[i]; }); return o;
  });
}
function col_(name, header) { var i = HEAD[name].indexOf(header); if (i < 0) throw new Error(header); return i + 1; }
function find_(name, header, value) {
  var sh = sheet_(name), n = sh.getLastRow() - 1; if (n < 1) return null;
  var h = sh.getRange(1, 1, 1, sh.getLastColumn()).getValues()[0], c = h.indexOf(header);
  var data = sh.getRange(2, 1, n, h.length).getValues();
  for (var i = 0; i < data.length; i++) {
    if (String(data[i][c]).toLowerCase() === String(value).toLowerCase()) {
      var o = {}; h.forEach(function (k, j) { o[k] = data[i][j]; });
      return { sheet: sh, row: i + 2, obj: o };
    }
  }
  return null;
}
function upsertClient_(email, name, phone, program, group, sessions) {
  email = String(email || '').toLowerCase(); if (!email) return;
  var f = find_(SH.CLIENTS, 'Email', email);
  if (f) {
    var total = (Number(f.obj['Занятий всего']) || 0) + sessions, done = Number(f.obj['Проведено']) || 0;
    f.sheet.getRange(f.row, 2, 1, 9).setValues([[name || f.obj['Имя'], phone || f.obj['Телефон'], program, group || f.obj['Поток'], total, done, total - done, f.obj['Начало'] || new Date(), 'Активен']]);
  } else {
    sheet_(SH.CLIENTS).appendRow([email, clean_(name, 80), clean_(phone, 40), program, group || '', sessions, 0, sessions, new Date(), 'Активен', '']);
  }
}
function changeDone_(email, delta) {
  var f = find_(SH.CLIENTS, 'Email', email); if (!f) return;
  var total = Number(f.obj['Занятий всего']) || 0, done = Math.max(0, (Number(f.obj['Проведено']) || 0) + delta);
  f.sheet.getRange(f.row, col_(SH.CLIENTS, 'Проведено'), 1, 2).setValues([[done, total - done]]);
  if (total - done <= 0) f.sheet.getRange(f.row, col_(SH.CLIENTS, 'Статус')).setValue('Завершён');
  else if (f.obj['Статус'] === 'Завершён') f.sheet.getRange(f.row, col_(SH.CLIENTS, 'Статус')).setValue('Активен');
}
function programByName_(n) { return getDashboardPrograms_().filter(function (p) { return p.name === n; })[0]; }
function programById_(id) { return getDashboardPrograms_().filter(function (p) { return p.id === id; })[0]; }
function getDashboardPrograms_() { return rows_(SH.PROGRAMS).map(function (r) { return { id: r.ID, name: r['Название'], sessions: +r['Занятий'] || 1, min: +r['Минут'] || 60 }; }); }
function setting_(k) {
  var r = rows_(SH.SETTINGS).filter(function (x) { return String(x['Ключ']).trim() === k; })[0];
  return r ? String(r['Значение']).trim() : '';
}
function setSetting_(k, v) {
  var f = find_(SH.SETTINGS, 'Ключ', k);
  if (f) f.sheet.getRange(f.row, 2).setValue(v); else sheet_(SH.SETTINGS).appendRow([k, v, '']);
}
function parseLocal_(date, time) { // дата+время в часовом поясе скрипта
  return Utilities.parseDate(date + ' ' + time, Session.getScriptTimeZone(), 'yyyy-MM-dd HH:mm');
}
function iso_(v) { return v instanceof Date ? Utilities.formatDate(v, Session.getScriptTimeZone(), "yyyy-MM-dd'T'HH:mm") : String(v || ''); }
function hhmm_(v) { return v instanceof Date ? Utilities.formatDate(v, Session.getScriptTimeZone(), 'HH:mm') : String(v || '').slice(0, 5); }
function clean_(v, max) {
  var s = String(v == null ? '' : v).trim().slice(0, max || 200);
  return /^[=+\-@]/.test(s) ? "'" + s : s;
}
function esc_(s) { return String(s == null ? '' : s).replace(/[&<>"']/g, function (c) { return { '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;' }[c]; }); }
