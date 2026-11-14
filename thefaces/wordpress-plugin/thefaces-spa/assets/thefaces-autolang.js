/* THE FACES · automatic language (runs in <head>, before the page is painted).
   First visit only: if the visitor lands on the default (English) page and the browser prefers one of the
   site languages, go to that version. A language chosen in the switcher is remembered and always wins.
   Bots and search engines are never redirected, so every language keeps its own URL in Google. */
(function () {
  function links() {
    var out = {}, nodes = document.querySelectorAll('link[rel="alternate"][hreflang], .langsel a[hreflang]');
    for (var i = 0; i < nodes.length; i++) {
      var h = nodes[i].getAttribute("hreflang");
      if (h && h !== "x-default" && !out[h]) out[h] = nodes[i].href;
    }
    return out;
  }
  function run() {
    try {
      if (/bot|crawl|spider|slurp|facebookexternalhit|lighthouse|headless|preview/i.test(navigator.userAgent || "")) return true;
      var saved = localStorage.getItem("tf_lang");
      var current = (document.documentElement.getAttribute("lang") || "en").slice(0, 2).toLowerCase();
      if (current !== "en") { localStorage.setItem("tf_lang", current); return true; }
      if (saved === "en") return true;
      var l = links(), found = false;
      for (var k in l) { found = true; break; }
      if (!found) return false;
      if (saved) {
        if (l[saved] && l[saved] !== location.href) location.replace(l[saved]);
        return true;
      }
      var prefs = navigator.languages && navigator.languages.length ? navigator.languages : [navigator.language || "en"];
      for (var j = 0; j < prefs.length; j++) {
        var code = String(prefs[j]).toLowerCase().split("-")[0];
        if (code === "in") code = "id";
        if (code === "en") return true;
        if (l[code] && l[code] !== location.href) { localStorage.setItem("tf_lang", code); location.replace(l[code]); return true; }
      }
    } catch (e) {}
    return true;
  }
  if (!run()) document.addEventListener("DOMContentLoaded", run);
  document.addEventListener("click", function (e) {
    var a = e.target.closest && e.target.closest("a[hreflang]");
    if (a) { try { localStorage.setItem("tf_lang", a.getAttribute("hreflang")); } catch (err) {} }
  }, true);
})();
