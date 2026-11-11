(() => {
  const $ = (s, c = document) => c.querySelector(s);
  const $$ = (s, c = document) => [...c.querySelectorAll(s)];
  const EMAIL = 'luismi.olea@senalval.es';

  /* ---- Imágenes: si una foto no carga, recuadro con su nombre ---- */
  $$('.media img').forEach(img => {
    const box = img.closest('.media');
    box.dataset.label = img.alt;
    const fail = () => box.classList.add('is-missing');
    if (img.complete && img.naturalWidth === 0) fail();
    img.addEventListener('error', fail);
  });
  /* Prueba una lista de URLs hasta que una cargue; si ninguna, llama a fail() */
  const chain = (img, list, fail) => {
    const q = [...list];
    const next = () => { if (!q.length) { fail && fail(); return; } img.src = q.shift(); };
    img.addEventListener('error', next); next();
  };

  /* ---- Portada: fotos de proyectos que se van alternando ---- */
  const slides = $$('.hero__slide');
  if (slides.length) {
    const cap = $('.hero__slidecap-text');
    const dots = $('.hero__slidecap-dots');
    slides.forEach((img, k) => {
      const d = document.createElement('i'); dots.appendChild(d);
      const fail = () => { img.classList.add('is-broken'); };
      if (img.complete && img.naturalWidth === 0) fail();
      img.addEventListener('error', fail);
      if (k) img.loading = 'eager'; // se precargan tras la primera
    });
    const reduce = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
    let cur = 0;
    const show = i => {
      const ok = slides.filter(s => !s.classList.contains('is-broken'));
      if (!ok.length) return;
      cur = (i + slides.length) % slides.length;
      if (slides[cur].classList.contains('is-broken')) return show(cur + 1);
      slides.forEach((s, k) => s.classList.toggle('is-active', k === cur));
      $$('i', dots).forEach((d, k) => d.classList.toggle('is-on', k === cur));
      cap.classList.remove('is-in'); void cap.offsetWidth;
      cap.textContent = slides[cur].dataset.caption || '';
      cap.classList.add('is-in');
    };
    show(0);
    if (!reduce) {
      let timer = setInterval(() => show(cur + 1), 6500);
      document.addEventListener('visibilitychange', () => {
        clearInterval(timer);
        if (!document.hidden) timer = setInterval(() => show(cur + 1), 6500);
      });
    }
  }

  /* ---- Logos de clientes ----
     Cada logo prueba sus fuentes en orden (archivo local .svg, .png y, si hay, una URL externa).
     Si ninguna carga, el logo se retira: nunca se muestra texto en su lugar. */
  const track = $('.marquee__track');
  if (track) {
    const load = li => new Promise(done => {
      const img = $('img', li);
      const srcs = (li.dataset.srcs || '').split('|').filter(Boolean);
      const next = () => {
        if (!srcs.length) { li.remove(); return done(false); }
        img.src = srcs.shift();
      };
      img.addEventListener('load', () => done(true));
      img.addEventListener('error', next);
      next();
    });
    Promise.all($$('.logo', track).map(load)).then(() => {
      const items = $$('.logo', track);
      const clients = $('#clientes');
      if (!items.length) { clients.hidden = true; return; }
      if (items.length < 5) { clients.classList.add('clients--static'); return; }
      // Bucle continuo: duplicamos la tira
      items.forEach(li => { const c = li.cloneNode(true); c.setAttribute('aria-hidden', 'true'); track.appendChild(c); });
      clients.classList.add('clients--moving');
    });
  }

  /* ---- Navegación ---- */
  const nav = $('.nav');
  const floatCta = $('.float-cta');
  const onScroll = () => {
    const y = window.scrollY;
    nav.classList.toggle('is-scrolled', y > 40);
    if (floatCta) floatCta.classList.toggle('is-visible', y > window.innerHeight * .8);
  };
  onScroll();
  window.addEventListener('scroll', onScroll, { passive: true });

  const burger = $('.nav__burger');
  const menu = $('#mobile-menu');
  const setMenu = open => {
    burger.setAttribute('aria-expanded', String(open));
    menu.hidden = !open;
    if (open) nav.classList.add('is-scrolled'); else onScroll();
  };
  burger.addEventListener('click', () => setMenu(menu.hidden));
  $$('a', menu).forEach(a => a.addEventListener('click', () => setMenu(false)));

  // Enlace activo según la sección visible
  const links = $$('.nav__links a');
  const spy = new IntersectionObserver(entries => {
    entries.forEach(e => {
      if (!e.isIntersecting) return;
      links.forEach(a => a.classList.toggle('is-active', a.getAttribute('href') === '#' + e.target.id));
    });
  }, { rootMargin: '-45% 0px -50% 0px' });
  links.forEach(a => { const s = $(a.getAttribute('href')); if (s) spy.observe(s); });

  /* ---- Aparición escalonada ---- */
  const io = new IntersectionObserver(entries => {
    entries.forEach(e => {
      if (!e.isIntersecting) return;
      const sibs = $$('.reveal', e.target.parentElement);
      e.target.style.transitionDelay = Math.min(sibs.indexOf(e.target), 6) * 70 + 'ms';
      e.target.classList.add('is-in');
      io.unobserve(e.target);
    });
  }, { threshold: .12 });
  $$('.reveal').forEach(el => io.observe(el));

  /* ---- Prefijar el tipo de consulta desde otros botones ---- */
  const tipo = $('#form-tipo');
  const msg = $('#form-msg');
  const preset = (type, text) => {
    [...tipo.options].forEach(o => { if (o.text === type) tipo.value = o.text; });
    if (text && !msg.value) msg.value = text;
  };
  $$('[data-topic]').forEach(a => a.addEventListener('click', () => {
    const t = a.dataset.topic;
    if (t.startsWith('Guía')) preset('Guía técnica', `Me gustaría recibir la ${t.toLowerCase()}.`);
    else if (t === 'Licitación') preset('Licitación', 'Tenemos una licitación de señalización. Expediente / enlace al pliego: ');
  }));
  $('#dossier-btn').addEventListener('click', () => {
    preset('Dossier de sector', `Me gustaría recibir el dossier del sector: ${$('#dossier-sector').value}.`);
    $('#contacto').scrollIntoView({ behavior: 'smooth' });
  });

  /* ---- Formulario → email o WhatsApp ya rellenados ----
     No hay servidor: se abre la app de correo o WhatsApp del visitante con la consulta escrita. */
  const WHATSAPP = '34665863597';
  const form = $('#contact-form');
  let via = 'email';
  $$('.form__send button', form).forEach(b => b.addEventListener('click', () => { via = b.value; }));
  form.addEventListener('submit', e => {
    e.preventDefault();
    if (e.submitter && e.submitter.value) via = e.submitter.value;
    let ok = true;
    $$('[required]', form).forEach(f => {
      const bad = f.type === 'checkbox' ? !f.checked : !f.value.trim() || (f.type === 'email' && !/^\S+@\S+\.\S+$/.test(f.value));
      f.classList.toggle('is-invalid', bad);
      if (bad) ok = false;
    });
    const note = $('#form-note');
    if (!ok) { note.textContent = 'Revise los campos marcados, por favor.'; return; }
    const d = Object.fromEntries(new FormData(form));
    const lines = [
      `Nombre: ${d.nombre}`, `Empresa / organismo: ${d.empresa || '-'}`,
      `Email: ${d.email}`, `Teléfono: ${d.telefono || '-'}`,
      `Tipo de consulta: ${d.tipo}`, `Plazo: ${d.plazo}`, '', d.mensaje
    ];
    if (via === 'whatsapp') {
      const text = ['Hola SeñalVal, os escribo desde la web.', '', ...lines].join('\n');
      window.open(`https://wa.me/${WHATSAPP}?text=${encodeURIComponent(text)}`, '_blank', 'noopener');
      note.textContent = 'Gracias. Se ha abierto WhatsApp con su consulta escrita; solo tiene que pulsar enviar.';
    } else {
      const subject = `[Web] ${d.tipo} — ${d.empresa || d.nombre}`;
      window.location.href = `mailto:${EMAIL}?subject=${encodeURIComponent(subject)}&body=${encodeURIComponent(lines.join('\n'))}`;
      note.textContent = 'Gracias. Se ha abierto su correo con la consulta escrita; solo tiene que pulsar enviar.';
    }
  });

  /* ---- Blog: últimos artículos desde WordPress (REST API) ---- */
  const strip = html => { const d = document.createElement('div'); d.innerHTML = html; return (d.textContent || '').trim(); };
  const fmt = iso => new Date(iso).toLocaleDateString('es-ES', { day: 'numeric', month: 'long', year: 'numeric' });
  const posts = $('#posts');
  const blogApi = (posts && posts.dataset.api) || 'https://senalval.es/wp-json/wp/v2/posts';
  const blogCount = (posts && posts.dataset.count) || 6;
  const blog = (() => {
    const ctrl = new AbortController();
    setTimeout(() => ctrl.abort(), 9000);
    const url = `${blogApi}?per_page=${blogCount}&_embed=wp:featuredmedia,wp:term&_fields=link,title,excerpt,content,date,_links,_embedded`;
    return fetch(url, { signal: ctrl.signal })
      .then(r => { if (!r.ok) throw new Error(r.status); return r.json(); })
      .then(list => (Array.isArray(list) ? list : []).map(p => {
        const emb = p._embedded || {};
        const media = (emb['wp:featuredmedia'] || [])[0];
        const sizes = (media && media.media_details && media.media_details.sizes) || {};
        const cat = ((emb['wp:term'] || [])[0] || [])[0];
        const title = strip((p.title && p.title.rendered) || '');
        const usable = u => u && !/\.heic$/i.test(u);
        const inContent = (((p.content && p.content.rendered) || '').match(/<img[^>]+src="([^"]+)"/gi) || [])
          .map(tag => tag.match(/src="([^"]+)"/i)[1].replace(/^https:\/\/i\d\.wp\.com\//, 'https://').split('?')[0])
          .filter(usable);
        const feat = media ? [(sizes.large || {}).source_url, (sizes.medium_large || {}).source_url, media.source_url].filter(usable) : [];
        const pool = [...feat, ...inContent.flatMap(u => [u, u.replace(/-\d+x\d+(\.\w+)$/, '$1')])];
        return {
          imgs: [...new Set(pool)],
          link: p.link,
          title,
          date: fmt(p.date),
          cat: cat ? strip(cat.name) : '',
          img: [...new Set(pool)][0] || '',
          imgLarge: [...new Set(pool)][0] || '',
          alt: (media && media.alt_text) || title,
          excerpt: strip((p.excerpt && p.excerpt.rendered) || '').replace(/\s*\[(…|&hellip;|\.\.\.)\]\s*$/, '…')
        };
      }));
  })();

  if (posts) {
    const fallback = () => { posts.hidden = true; $('#posts-fallback').hidden = false; };
    blog.then(list => {
      if (!list.length) return fallback();
      posts.innerHTML = '';
      list.forEach(p => {
        const a = document.createElement('a');
        a.className = 'post';
        a.href = p.link;
        a.innerHTML = `
          <div class="media">${p.img ? '<img loading="lazy" alt="">' : ''}</div>
          <div class="post__body">
            <span class="post__meta"></span>
            <h3></h3>
            <p></p>
            <span class="post__more">Leer artículo →</span>
          </div>`;
        const box = $('.media', a);
        box.dataset.label = p.title;
        if (p.imgs.length) { const im = $('img', a); im.alt = p.alt; chain(im, p.imgs, () => { im.remove(); box.classList.add('media--brand'); }); }
        else box.classList.add('media--brand');
        $('.post__meta', a).textContent = [p.cat, p.date].filter(Boolean).join(' · ');
        $('h3', a).textContent = p.title;
        $('p', a).textContent = p.excerpt;
        posts.appendChild(a);
      });
    }).catch(fallback);
  }

  /* ---- Portada: historias con imágenes del blog ---- */
  const stories = $('#hero-stories');
  if (stories) {
    blog.then(list => {
      const items = list.filter(p => p.imgs.length).slice(0, 5);
      if (items.length < 2) return;
      const slides = $('.stories__slides', stories);
      const bars = $('.stories__bars', stories);
      items.forEach((p, i) => {
        const a = document.createElement('a');
        a.className = 'story';
        a.href = p.link;
        a.innerHTML = '<div class="story__img"><img alt=""></div><div class="story__body"><span class="story__meta"></span><h3 class="story__title"></h3></div>';
        const im = $('img', a); im.alt = p.alt; chain(im, p.imgs, () => { a.remove(); });
        $('.story__meta', a).textContent = [p.cat, p.date].filter(Boolean).join(' · ');
        $('.story__title', a).textContent = p.title;
        slides.appendChild(a);
        const b = document.createElement('span'); b.innerHTML = '<i></i>'; bars.appendChild(b);
      });
      const sign = $('.hero__sign'); if (sign) sign.hidden = true;
      stories.hidden = false;

      const DURATION = 6000;
      const all = $$('.story', stories), allBars = $$('span', bars);
      let cur = 0, timer = null, paused = false;
      const show = i => {
        cur = (i + all.length) % all.length;
        all.forEach((s, k) => s.classList.toggle('is-active', k === cur));
        allBars.forEach((b, k) => { b.classList.toggle('is-done', k < cur); b.classList.toggle('is-active', k === cur); });
        // reinicia la animación de la barra
        const bar = $('i', allBars[cur]); bar.style.animation = 'none'; void bar.offsetWidth; bar.style.animation = '';
        clearTimeout(timer);
        if (!paused) timer = setTimeout(() => show(cur + 1), DURATION);
      };
      $$('.stories__btn', stories).forEach(btn => btn.addEventListener('click', () => show(cur + Number(btn.dataset.dir))));
      stories.addEventListener('mouseenter', () => { paused = true; clearTimeout(timer); stories.classList.add('is-paused'); });
      stories.addEventListener('mouseleave', () => { paused = false; stories.classList.remove('is-paused'); show(cur); });
      show(0);
    }).catch(() => {});
  }

  /* ---- Proyectos: ventana con galería e información ---- */
  const dataEl = $('#projects-data');
  const modal = $('#pmodal');
  if (dataEl && modal) {
    const P = JSON.parse(dataEl.textContent);
    const img = $('.pmodal__img', modal), thumbs = $('.pmodal__thumbs', modal), count = $('.pmodal__count', modal);
    let list = [], cur = 0, cfg = null;
    const go = i => {
      if (!list.length) return;
      cur = (i + list.length) % list.length;
      img.classList.remove('is-in'); void img.offsetWidth;
      img.src = list[cur]; img.alt = `${cfg.title} · foto ${cur + 1} de ${list.length}`;
      img.classList.add('is-in');
      count.textContent = `${cur + 1} / ${list.length}`;
      $$('button', thumbs).forEach((b, k) => b.classList.toggle('is-on', k === cur));
      const on = $$('button', thumbs)[cur]; if (on) on.scrollIntoView({ block: 'nearest', inline: 'center', behavior: 'smooth' });
      const nxt = new Image(); nxt.src = list[(cur + 1) % list.length];
    };
    const open = id => {
      cfg = P[id]; if (!cfg) return;
      list = cfg.gallery.length ? cfg.gallery : (cfg.cover ? [cfg.cover] : []);
      modal.classList.toggle('pmodal--nogallery', !list.length);
      $('.pmodal__sector', modal).textContent = cfg.sector;
      $('#pmodal-title').textContent = cfg.title;
      $('.pmodal__sub', modal).textContent = cfg.sub;
      $('.pmodal__case', modal).innerHTML = '';
      [['Reto', cfg.reto], ['Solución', cfg.solucion], ['Materiales', cfg.materiales], ['Instalación', cfg.instalacion]].forEach(([k, v]) => {
        const d = document.createElement('div'); d.innerHTML = '<dt></dt><dd></dd>';
        $('dt', d).textContent = k; $('dd', d).textContent = v; $('.pmodal__case', modal).appendChild(d);
      });
      const link = $('.pmodal__link', modal); link.hidden = !cfg.link; if (cfg.link) link.href = cfg.link;
      thumbs.innerHTML = '';
      list.forEach((u, k) => {
        const b = document.createElement('button'); b.type = 'button'; b.setAttribute('aria-label', `Ver foto ${k + 1}`);
        b.innerHTML = '<img loading="lazy" alt="">'; $('img', b).src = u;
        b.addEventListener('click', () => go(k)); thumbs.appendChild(b);
      });
      $$('.pmodal__nav', modal).forEach(b => b.hidden = list.length < 2);
      modal.showModal(); document.documentElement.classList.add('is-locked');
      go(0);
    };
    const close = () => { modal.close(); };
    modal.addEventListener('close', () => document.documentElement.classList.remove('is-locked'));
    $('.pmodal__close', modal).addEventListener('click', close);
    modal.addEventListener('click', e => { if (e.target === modal) close(); });
    $('.pmodal__nav--prev', modal).addEventListener('click', () => go(cur - 1));
    $('.pmodal__nav--next', modal).addEventListener('click', () => go(cur + 1));
    modal.addEventListener('keydown', e => { if (e.key === 'ArrowLeft') go(cur - 1); if (e.key === 'ArrowRight') go(cur + 1); });
    let sx = null;
    $('.pmodal__stage', modal).addEventListener('touchstart', e => { sx = e.touches[0].clientX; }, { passive: true });
    $('.pmodal__stage', modal).addEventListener('touchend', e => { if (sx === null) return; const dx = e.changedTouches[0].clientX - sx; if (Math.abs(dx) > 40) go(cur + (dx < 0 ? 1 : -1)); sx = null; });
    $('.pmodal__cta', modal).addEventListener('click', () => {
      close();
      const m = $('#form-msg'); if (m && !m.value) m.value = `Hemos visto el proyecto «${cfg.title}» y queremos algo similar. `;
    });
    $$('[data-project]').forEach(el => {
      el.addEventListener('click', e => { if (el.tagName === 'A') { e.preventDefault(); const m = $('#mobile-menu'); if (m && !m.hidden) $('.nav__burger').click(); el.blur(); } open(el.dataset.project); });
      el.addEventListener('keydown', e => { if ((e.key === 'Enter' || e.key === ' ') && el.tagName !== 'BUTTON') { e.preventDefault(); open(el.dataset.project); } });
    });
  }

  const y = $('#year'); if (y) y.textContent = new Date().getFullYear();
})();
