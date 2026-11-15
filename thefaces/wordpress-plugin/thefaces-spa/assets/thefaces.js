/* THE FACES · shared behaviour for all Tilda blocks.
   Booking: every "Book" link goes straight to Altegio (n831884.alteg.io), where the guest chooses
   city, salon and treatments. Nothing is pre-selected or stored on the website. */
(function () {
  "use strict";
  function $(s, r) { return (r || document).querySelector(s); }
  function $$(s, r) { return Array.prototype.slice.call((r || document).querySelectorAll(s)); }

  function init() {
    var cfgEl = $("#tf-i18n");
    var T = cfgEl ? JSON.parse(cfgEl.textContent) : {};
    window.dataLayer = window.dataLayer || [];

    /* ---------- toast (newsletter) ---------- */
    var toastEl = $(".toast");
    function toast(msg) {
      if (!toastEl) return;
      $(".msg", toastEl).textContent = msg; toastEl.classList.add("show");
      clearTimeout(toastEl._h); toastEl._h = setTimeout(function () { toastEl.classList.remove("show"); }, 2600);
    }

    /* ---------- clicks ---------- */
    document.addEventListener("click", function (e) {
      var el;
      if ((el = e.target.closest("[data-book]"))) {
        // One signal for ads/analytics: the visitor left for the booking system. The real booking happens in Altegio.
        window.dataLayer.push({ event: "booking_click", booking_location: el.getAttribute("data-book"),
          booking_item: el.getAttribute("data-item") || "", booking_salon: el.getAttribute("data-salon") || "any",
          page_language: T.lang || "en" });
        return;
      }
      if ((el = e.target.closest("[role=tab][data-tab]"))) {
        var id = el.getAttribute("data-tab");
        $$("[role=tab][data-tab]").forEach(function (x) { x.setAttribute("aria-selected", x === el); });
        $$(".cat").forEach(function (c) { c.hidden = c.id !== "cat-" + id; });
        window.dataLayer.push({ event: "menu_category", menu_category: id });
        return;
      }
      if ((el = e.target.closest(".el"))) { $$(".el").forEach(function (x) { x.classList.toggle("open", x === el); x.setAttribute("aria-expanded", x === el); }); return; }
      if ((el = e.target.closest(".langsel>button"))) { el.parentNode.classList.toggle("open"); el.setAttribute("aria-expanded", el.parentNode.classList.contains("open")); return; }
      if (!e.target.closest(".langsel")) $$(".langsel.open").forEach(function (x) { x.classList.remove("open"); });
    });
    document.addEventListener("keydown", function (e) {
      if (e.key === "Enter" && e.target.classList && e.target.classList.contains("el")) e.target.click();
      if (e.key === "Escape") { $$(".mnav.open").forEach(function (m) { m.classList.remove("open"); }); $$(".langsel.open").forEach(function (x) { x.classList.remove("open"); }); }
    });

    /* ---------- header, mobile nav, hero sound ---------- */
    var burger = $(".burger"), mnav = $(".mnav");
    if (burger && mnav) {
      burger.addEventListener("click", function () { mnav.classList.add("open"); });
      $(".mnav .close").addEventListener("click", function () { mnav.classList.remove("open"); });
      $$(".mnav a").forEach(function (a) { a.addEventListener("click", function () { mnav.classList.remove("open"); }); });
      var mimgs = $$(".mn-img img");
      $$(".mn-links a").forEach(function (a, i) {
        a.addEventListener("mouseenter", function () { mimgs.forEach(function (im, k) { im.classList.toggle("on", k === i); }); });
      });
    }
    var snd = $(".sound"), vid = $(".hero video");
    if (snd && vid) snd.addEventListener("click", function () { vid.muted = !vid.muted; snd.textContent = vid.muted ? snd.getAttribute("data-off") : snd.getAttribute("data-on"); });

    /* ---------- signature rail ---------- */
    var rail = $(".rail");
    if (rail) {
      var pv = $(".railnav .prev"), nx = $(".railnav .next");
      if (pv) pv.addEventListener("click", function () { rail.scrollBy({ left: -400, behavior: "smooth" }); });
      if (nx) nx.addEventListener("click", function () { rail.scrollBy({ left: 400, behavior: "smooth" }); });
      var drag = false, moved = false, x0 = 0, s0 = 0;
      rail.addEventListener("pointerdown", function (e) { if (e.pointerType !== "mouse" || e.target.closest("a")) return; drag = true; moved = false; x0 = e.clientX; s0 = rail.scrollLeft; rail.style.scrollSnapType = "none"; });
      window.addEventListener("pointerup", function () { drag = false; rail.style.scrollSnapType = ""; });
      rail.addEventListener("pointermove", function (e) { if (drag) { moved = true; rail.scrollLeft = s0 - (e.clientX - x0); } });
    }

    /* ---------- journal: search + categories ---------- */
    var jo = $(".jo-all");
    if (jo) {
      var jin = $(".jo-search input", jo), jcat = "", cardsJ = $$(".jo-grid .post", jo), cnt = $(".jo-count", jo), none = $(".jo-none", jo);
      var tpl = jo.getAttribute("data-count-tpl") || "{n}";
      var norm = function (t) { return (t || "").toLowerCase().normalize("NFD").replace(/[̀-ͯ]/g, ""); };
      var applyJ = function () {
        var q = norm(jin.value.trim()), shown = 0;
        cardsJ.forEach(function (c) {
          var ok = (!jcat || c.getAttribute("data-cat") === jcat) && (!q || norm(c.getAttribute("data-text") || c.textContent).indexOf(q) > -1);
          c.hidden = !ok; if (ok) shown++;
        });
        cnt.textContent = tpl.replace("{n}", shown); none.hidden = shown > 0;
        jo.classList.toggle("jo-filtering", !!(q || jcat));
      };
      jin.addEventListener("input", applyJ);
      $$(".jo-chips button", jo).forEach(function (b) {
        b.addEventListener("click", function () {
          jcat = b.getAttribute("data-jcat");
          $$(".jo-chips button", jo).forEach(function (x) { x.classList.toggle("on", x === b); });
          applyJ();
          window.dataLayer.push({ event: "journal_filter", journal_category: jcat || "all" });
        });
      });
      try {
        var qs = new URLSearchParams(location.search);
        if (qs.get("q")) jin.value = qs.get("q");
        var qc = qs.get("cat") || (location.hash || "").replace("#cat-", "");
        if (qc) $$(".jo-chips button", jo).forEach(function (x) { if (x.getAttribute("data-jcat") === qc) { jcat = qc; $$(".jo-chips button", jo).forEach(function (y) { y.classList.toggle("on", y === x); }); } });
      } catch (e) {}
      applyJ();
    }

    /* ---------- five senses: active item swaps the sticky image ---------- */
    var snItems = $$(".sn-item"), snImgs = $$(".sn-frame img"), snDots = $$(".sn-dots i"), snNum = $(".sn-frame .num");
    if (snItems.length && "IntersectionObserver" in window) {
      var setSense = function (i) {
        snItems.forEach(function (x, k) { x.classList.toggle("on", k === i); });
        snImgs.forEach(function (x, k) { x.classList.toggle("on", k === i); });
        snDots.forEach(function (x, k) { x.classList.toggle("on", k === i); });
        if (snNum) snNum.textContent = "0" + (i + 1);
      };
      var so = new IntersectionObserver(function (es) {
        es.forEach(function (en) { if (en.isIntersecting) setSense(snItems.indexOf(en.target)); });
      }, { rootMargin: "-45% 0px -45% 0px" });
      snItems.forEach(function (x) { so.observe(x); });
      setSense(0);
    }

    /* ---------- reveal + parallax + solid header ---------- */
    var reduce = window.matchMedia && matchMedia("(prefers-reduced-motion: reduce)").matches;
    if ("IntersectionObserver" in window) {
      var io = new IntersectionObserver(function (es) { es.forEach(function (en) { if (en.isIntersecting) { en.target.classList.add("in"); io.unobserve(en.target); } }); }, { threshold: 0.15 });
      $$(".rv,.mask").forEach(function (x) { io.observe(x); });
    } else $$(".rv,.mask").forEach(function (x) { x.classList.add("in"); });
    var head = $(".top"), px = $$("[data-parallax]"), ticking = false;
    function onScroll() {
      if (head) head.classList.toggle("solid", window.scrollY > 60);
      if (!reduce) px.forEach(function (el) {
        var r = el.getBoundingClientRect(), k = parseFloat(el.getAttribute("data-parallax"));
        var v = Math.max(-80, Math.min(80, -(r.top + r.height / 2 - innerHeight / 2) * k));
        el.style.transform = "translate3d(0," + v.toFixed(1) + "px,0)";
      });
      ticking = false;
    }
    window.addEventListener("scroll", function () { if (!ticking) { requestAnimationFrame(onScroll); ticking = true; } }, { passive: true });
    onScroll();

    /* ---------- newsletter + cookie banner ---------- */
    $$(".news").forEach(function (f) { f.addEventListener("submit", function (e) { e.preventDefault(); toast(T.ft_thanks || "Thank you"); f.reset(); }); });
    var ck = $(".cookie");
    if (ck) {
      var c = null; try { c = localStorage.getItem("tf_consent"); } catch (e) {}
      if (!c) ck.classList.add("show");
      $$("[data-consent]", ck).forEach(function (b) {
        b.addEventListener("click", function () {
          var ok = b.getAttribute("data-consent") === "yes";
          if (window.tfConsent) window.tfConsent(ok); else try { localStorage.setItem("tf_consent", ok ? "granted" : "denied"); } catch (e) {}
          ck.classList.remove("show");
        });
      });
    }
    // Clean up the old "Your ritual" selection saved by earlier versions of the site.
    try { localStorage.removeItem("tf_ritual"); } catch (e) {}
  }
  if (document.readyState === "loading") document.addEventListener("DOMContentLoaded", init); else init();
})();
