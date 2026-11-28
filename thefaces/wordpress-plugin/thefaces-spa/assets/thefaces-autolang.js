/* THE FACES · automatic language (runs in <head>, before the page is painted).
   The site follows the language of the visitor's device (browser / phone settings).
   - A language picked by hand in the switcher is remembered and always wins.
   - Otherwise, on the first page of each visit, the visitor is sent to the version in the device language
     (if the site has it). Links shared in another language are respected for the rest of the visit.
   - Bots and search engines are never redirected, so every language keeps its own URL in Google. */
(function () {
  var LANGS = ["en", "ru", "es", "de", "th", "id", "ja", "fr", "uk"];
  function links() {
    var out = {}, nodes = document.querySelectorAll('link[rel="alternate"][hreflang], .langsel a[hreflang]');
    for (var i = 0; i < nodes.length; i++) {
      var h = nodes[i].getAttribute("hreflang");
      if (h && h !== "x-default" && !out[h]) out[h] = nodes[i].href;
    }
    return out;
  }
  function deviceLang() {
    var prefs = navigator.languages && navigator.languages.length ? navigator.languages : [navigator.language || navigator.userLanguage || "en"];
    for (var j = 0; j < prefs.length; j++) {
      var code = String(prefs[j] || "").toLowerCase().split(/[-_]/)[0];
      if (code === "in") code = "id";
      if (code === "be" || code === "kk") code = "ru";
      if (LANGS.indexOf(code) > -1) return code;
    }
    return "en";
  }
  function store(k, v) { try { if (v === null) localStorage.removeItem(k); else localStorage.setItem(k, v); } catch (e) {} }
  function read(k, sess) { try { return (sess ? sessionStorage : localStorage).getItem(k); } catch (e) { return null; } }
  function run() {
    if (/bot|crawl|spider|slurp|facebookexternalhit|lighthouse|headless|preview|whatsapp|telegrambot/i.test(navigator.userAgent || "")) return true;
    if (read("tf_seen", true)) return true;                     // only the first page of a visit
    var l = links(), any = false;
    for (var k in l) { any = true; break; }
    if (!any) return false;                                      // links not parsed yet: retry on DOMContentLoaded
    try { sessionStorage.setItem("tf_seen", "1"); } catch (e) {}
    store("tf_lang", null);                                      // old automatic choice from earlier versions
    var current = (document.documentElement.getAttribute("lang") || "en").slice(0, 2).toLowerCase();
    var target = read("tf_lang_manual") || deviceLang();
    if (target !== current && l[target] && l[target] !== location.href) location.replace(l[target]);
    return true;
  }
  if (!run()) document.addEventListener("DOMContentLoaded", run);
  document.addEventListener("click", function (e) {
    var a = e.target.closest && e.target.closest(".langsel a[hreflang], .mnav .langs a[hreflang], .f-langs a[hreflang]");
    if (a) store("tf_lang_manual", a.getAttribute("hreflang"));
  }, true);
})();
