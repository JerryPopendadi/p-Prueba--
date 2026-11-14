/* THE FACES · shared behaviour for all Tilda blocks. Reads everything from the HTML (data-* attributes),
   so prices and texts live in the blocks and this file never needs translating. */
(function () {
  "use strict";
  var SALONS = {
    ubud: { name: "Ubud", wa: "6282266999965", online: "https://n831884.alteg.io/" },
    sanur: { name: "Sanur", wa: "6281337709190", online: "https://n811764.alteg.io/" }
  };
  var LOCALE = { en: "en-US", ru: "ru-RU", es: "es-ES", de: "de-DE", th: "th-TH", id: "id-ID", ja: "ja-JP" };

  function $(s, r) { return (r || document).querySelector(s); }
  function $$(s, r) { return Array.prototype.slice.call((r || document).querySelectorAll(s)); }
  var store = {
    get: function (k) { try { return JSON.parse(localStorage.getItem(k) || "null"); } catch (e) { return null; } },
    set: function (k, v) { try { localStorage.setItem(k, JSON.stringify(v)); } catch (e) {} }
  };

  function init() {
    var cfgEl = $("#tf-i18n");
    var T = cfgEl ? JSON.parse(cfgEl.textContent) : {};
    var lang = T.lang || "en";
    var nf = new Intl.NumberFormat(LOCALE[lang] || "en-US");
    var idr = function (n) { return "IDR " + nf.format(n); };
    var dur = function (m) {
      var u = T.dur || ["h", "min", " "], h = Math.floor(m / 60), r = m % 60, out = [];
      if (h) out.push(h + (u[2] ? " " : "") + u[0]);
      if (r) out.push(r + (u[2] ? " " : "") + u[1]);
      return out.join(u[2]);
    };
    var t = function (k, v) { var s = T[k] || k; if (v) for (var x in v) s = s.split("{" + x + "}").join(v[x]); return s; };

    /* ---------- item registry from the markup ---------- */
    var ITEMS = {};
    $$("[data-add]").forEach(function (el) {
      var id = el.getAttribute("data-add");
      if (!ITEMS[id] && el.hasAttribute("data-p")) {
        ITEMS[id] = { id: id, name: el.getAttribute("data-name"), d: +el.getAttribute("data-d"), p: +el.getAttribute("data-p"),
          cat: el.getAttribute("data-cat") || "", only: (el.getAttribute("data-only") || "").split(",").filter(Boolean) };
      }
    });

    window.dataLayer = window.dataLayer || [];
    function ga(event, items, extra) {
      var list = items.filter(Boolean);
      window.dataLayer.push({ ecommerce: null });
      var o = { event: event, ecommerce: { currency: "IDR", value: list.reduce(function (s, i) { return s + i.p; }, 0),
        items: list.map(function (i, ix) { return { item_id: i.id, item_name: i.name, item_category: i.cat, price: i.p, quantity: 1, index: ix }; }) } };
      for (var k in (extra || {})) o[k] = extra[k];
      window.dataLayer.push(o);
    }

    var saved = store.get("tf_ritual") || {};
    var cart = (saved.cart || []).filter(function (id) { return ITEMS[id]; });
    var salon = saved.salon || "ubud";
    var save = function () { store.set("tf_ritual", { cart: cart, salon: salon }); };

    /* ---------- toast ---------- */
    var toastEl = $(".toast");
    function toast(msg) {
      if (!toastEl) return;
      $(".msg", toastEl).textContent = msg; toastEl.classList.add("show");
      clearTimeout(toastEl._h); toastEl._h = setTimeout(function () { toastEl.classList.remove("show"); }, 2600);
    }

    function toggle(id) {
      var it = ITEMS[id]; if (!it) return;
      if (it.only.length && it.only.indexOf(salon) < 0) { salon = it.only[0]; toast(t("toast_switched", { salon: SALONS[salon].name })); }
      var i = cart.indexOf(id);
      if (i > -1) { cart.splice(i, 1); ga("remove_from_cart", [it], { salon: salon }); }
      else { cart.push(id); ga("add_to_cart", [it], { salon: salon }); toast(t("toast_added") + ": " + it.name); }
      save(); render();
    }
    function setSalon(s) { salon = s; ga("select_salon", cart.map(function (i) { return ITEMS[i]; }), { salon: s }); save(); render(); }

    function render() {
      $$("[data-add]").forEach(function (b) {
        var on = cart.indexOf(b.getAttribute("data-add")) > -1;
        b.classList.toggle("on", on); b.setAttribute("aria-pressed", on);
        if (b.classList.contains("plus")) b.textContent = on ? "✓" : "+";
        else if (b.hasAttribute("data-l-add")) b.textContent = on ? b.getAttribute("data-l-on") : b.getAttribute("data-l-add");
      });
      $$("[data-salon]").forEach(function (b) { b.classList.toggle("on", b.getAttribute("data-salon") === salon); });
      $$("[data-count]").forEach(function (b) { b.textContent = cart.length; b.classList.toggle("has", cart.length > 0); });
      var bl = $("#tf-blist"); if (!bl) return;
      var items = cart.map(function (i) { return ITEMS[i]; });
      $("#tf-bempty").hidden = items.length > 0;
      bl.innerHTML = items.map(function (i) {
        return '<li><span>' + i.name + '<small>' + dur(i.d) + '</small></span><span>' + idr(i.p) + '</span><button type="button" data-rm="' + i.id + '" aria-label="' + t("remove") + ' ' + i.name + '">×</button></li>';
      }).join("");
      var tm = items.reduce(function (s, i) { return s + i.d; }, 0), pr = items.reduce(function (s, i) { return s + i.p; }, 0);
      $("#tf-btime").textContent = tm ? dur(tm) : "—";
      $("#tf-btotal").textContent = idr(pr);
      var S = SALONS[salon], W = T.wa || {}, when = ($("#tf-bdate") || {}).value || "";
      var msg = (W.hello || "").replace("{salon}", S.name) + "\n" +
        (items.length ? items.map(function (i) { return "• " + i.name + " (" + i.d + " " + (W.min || "min") + ", IDR " + i.p.toLocaleString("en-US") + ")"; }).join("\n") +
          "\n" + (W.total || "Total") + ": IDR " + pr.toLocaleString("en-US") + " · " + tm + " " + (W.min || "min") : (W.advice || "")) +
        (when.trim() ? "\n" + (W.time || "Time") + ": " + when.trim() : "");
      $("#tf-bwa").href = "https://wa.me/" + S.wa + "?text=" + encodeURIComponent(msg);
      $("#tf-bonline").href = S.online;
      $("#tf-bonline .s").textContent = S.name;
    }

    /* ---------- clicks ---------- */
    document.addEventListener("click", function (e) {
      var el;
      if ((el = e.target.closest("[data-add]"))) { e.preventDefault(); e.stopPropagation(); toggle(el.getAttribute("data-add")); return; }
      if ((el = e.target.closest("[data-rm]"))) { toggle(el.getAttribute("data-rm")); return; }
      if ((el = e.target.closest("[data-salon]"))) { setSalon(el.getAttribute("data-salon")); return; }
      if ((el = e.target.closest("[data-book-salon]"))) {
        setSalon(el.getAttribute("data-book-salon"));
        var m = $("#menu"); if (m) { e.preventDefault(); m.scrollIntoView({ behavior: "smooth" }); }
        return;
      }
      if ((el = e.target.closest("[data-open-builder]"))) {
        var b = $("#tf-builder");
        ga("view_cart", cart.map(function (i) { return ITEMS[i]; }));
        if (b) { e.preventDefault(); b.scrollIntoView({ behavior: "smooth", block: "start" }); }
        return;
      }
      if ((el = e.target.closest("[role=tab][data-tab]"))) {
        var id = el.getAttribute("data-tab");
        $$("[role=tab][data-tab]").forEach(function (x) { x.setAttribute("aria-selected", x === el); });
        $$(".cat").forEach(function (c) { c.hidden = c.id !== "cat-" + id; });
        ga("view_item_list", $$("#cat-" + id + " [data-add]").map(function (b) { return ITEMS[b.getAttribute("data-add")]; }), { item_list_name: id });
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
    var dateIn = $("#tf-bdate"); if (dateIn) dateIn.addEventListener("input", render);
    ["#tf-bonline", "#tf-bwa"].forEach(function (s) {
      var a = $(s); if (!a) return;
      a.addEventListener("click", function () {
        var items = cart.map(function (i) { return ITEMS[i]; }), m = s === "#tf-bwa" ? "whatsapp" : "altegio";
        ga("begin_checkout", items, { salon: salon, booking_method: m });
        ga("generate_lead", items, { salon: salon, booking_method: m });
      });
    });

    /* ---------- header, mobile nav, hero sound ---------- */
    var burger = $(".burger"), mnav = $(".mnav");
    if (burger && mnav) {
      burger.addEventListener("click", function () { mnav.classList.add("open"); });
      $(".mnav .close").addEventListener("click", function () { mnav.classList.remove("open"); });
      $$(".mnav a").forEach(function (a) { a.addEventListener("click", function () { mnav.classList.remove("open"); }); });
    }
    var snd = $(".sound"), vid = $(".hero video");
    if (snd && vid) snd.addEventListener("click", function () { vid.muted = !vid.muted; snd.textContent = vid.muted ? snd.getAttribute("data-off") : snd.getAttribute("data-on"); });

    /* ---------- signature rail ---------- */
    var rail = $(".rail");
    if (rail) {
      var pv = $(".railnav .prev"), nx = $(".railnav .next");
      if (pv) pv.addEventListener("click", function () { rail.scrollBy({ left: -400, behavior: "smooth" }); });
      if (nx) nx.addEventListener("click", function () { rail.scrollBy({ left: 400, behavior: "smooth" }); });
      var drag = false, x0 = 0, s0 = 0;
      rail.addEventListener("pointerdown", function (e) { if (e.pointerType !== "mouse") return; drag = true; x0 = e.clientX; s0 = rail.scrollLeft; rail.style.scrollSnapType = "none"; });
      window.addEventListener("pointerup", function () { drag = false; rail.style.scrollSnapType = ""; });
      rail.addEventListener("pointermove", function (e) { if (drag) rail.scrollLeft = s0 - (e.clientX - x0); });
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
    $$(".news").forEach(function (f) { f.addEventListener("submit", function (e) { e.preventDefault(); toast(t("ft_thanks")); f.reset(); }); });
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

    render();
    var firstTab = $("[role=tab][aria-selected=true]");
    if (firstTab) ga("view_item_list", $$("#cat-" + firstTab.getAttribute("data-tab") + " [data-add]").map(function (b) { return ITEMS[b.getAttribute("data-add")]; }), { item_list_name: firstTab.getAttribute("data-tab") });
  }
  if (document.readyState === "loading") document.addEventListener("DOMContentLoaded", init); else init();
})();
