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

  /* ---- Logos: si no carga, nombre de la empresa en texto ---- */
  const track = $('.marquee__track');
  if (track) {
    // Duplicamos para un bucle continuo
    $$('.logo', track).forEach(li => {
      const c = li.cloneNode(true);
      c.setAttribute('aria-hidden', 'true');
      track.appendChild(c);
    });
    $$('.logo img', track).forEach(img => {
      const fail = () => img.closest('.logo').classList.add('is-missing');
      if (img.complete && img.naturalWidth === 0) fail();
      img.addEventListener('error', fail);
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

  const y = $('#year'); if (y) y.textContent = new Date().getFullYear();
})();
