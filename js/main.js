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
  const heroImg = $('.hero__media img');
  if (heroImg) {
    const hide = () => { heroImg.style.display = 'none'; };
    if (heroImg.complete && heroImg.naturalWidth === 0) hide();
    heroImg.addEventListener('error', hide);
  }

  /* ---- Vídeo de portada ---- */
  const video = $('.hero__video');
  if (video) {
    const reduce = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
    const drop = () => video.parentNode && video.parentNode.removeChild(video);
    if (reduce) { video.pause(); drop(); }
    else {
      const on = () => video.classList.add('is-playing');
      if (video.readyState >= 3) on();
      video.addEventListener('playing', on);
      video.addEventListener('canplay', () => { on(); video.play().catch(() => {}); });
      $('source', video).addEventListener('error', drop);
      video.addEventListener('error', drop);
      // Ahorro de batería: pausa el vídeo cuando la portada no está a la vista
      new IntersectionObserver(([e]) => { e.isIntersecting ? video.play().catch(() => {}) : video.pause(); }).observe(video);
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

  /* ---- Formulario → email preparado ---- */
  const form = $('#contact-form');
  form.addEventListener('submit', e => {
    e.preventDefault();
    let ok = true;
    $$('[required]', form).forEach(f => {
      const bad = f.type === 'checkbox' ? !f.checked : !f.value.trim() || (f.type === 'email' && !/^\S+@\S+\.\S+$/.test(f.value));
      f.classList.toggle('is-invalid', bad);
      if (bad) ok = false;
    });
    const note = $('#form-note');
    if (!ok) { note.textContent = 'Revise los campos marcados, por favor.'; return; }
    const d = Object.fromEntries(new FormData(form));
    const subject = `[Web] ${d.tipo} — ${d.empresa || d.nombre}`;
    const body = [
      `Nombre: ${d.nombre}`, `Empresa / organismo: ${d.empresa || '-'}`,
      `Email: ${d.email}`, `Teléfono: ${d.telefono || '-'}`,
      `Tipo de consulta: ${d.tipo}`, `Plazo: ${d.plazo}`, '', d.mensaje
    ].join('\n');
    window.location.href = `mailto:${EMAIL}?subject=${encodeURIComponent(subject)}&body=${encodeURIComponent(body)}`;
    note.textContent = 'Gracias. Se ha abierto su correo con la consulta preparada; solo tiene que enviarlo.';
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
    const url = `${blogApi}?per_page=${blogCount}&_embed=wp:featuredmedia,wp:term&_fields=link,title,excerpt,date,_links,_embedded`;
    return fetch(url, { signal: ctrl.signal })
      .then(r => { if (!r.ok) throw new Error(r.status); return r.json(); })
      .then(list => (Array.isArray(list) ? list : []).map(p => {
        const emb = p._embedded || {};
        const media = (emb['wp:featuredmedia'] || [])[0];
        const sizes = (media && media.media_details && media.media_details.sizes) || {};
        const cat = ((emb['wp:term'] || [])[0] || [])[0];
        const title = strip((p.title && p.title.rendered) || '');
        return {
          link: p.link,
          title,
          date: fmt(p.date),
          cat: cat ? strip(cat.name) : '',
          img: media ? ((sizes.medium_large || sizes.large || {}).source_url || media.source_url) : '',
          imgLarge: media ? ((sizes.large || sizes.full || {}).source_url || media.source_url) : '',
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
        if (p.img) { const im = $('img', a); im.src = p.img; im.alt = p.alt; im.addEventListener('error', () => box.classList.add('is-missing')); }
        else box.classList.add('is-missing');
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
      const items = list.filter(p => p.imgLarge).slice(0, 5);
      if (items.length < 2) return;
      const slides = $('.stories__slides', stories);
      const bars = $('.stories__bars', stories);
      items.forEach((p, i) => {
        const a = document.createElement('a');
        a.className = 'story';
        a.href = p.link;
        a.innerHTML = '<div class="story__img"><img alt=""></div><div class="story__body"><span class="story__meta"></span><h3 class="story__title"></h3></div>';
        const im = $('img', a); im.src = p.imgLarge; im.alt = p.alt; if (i) im.loading = 'lazy';
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

  const y = $('#year'); if (y) y.textContent = new Date().getFullYear();
})();
