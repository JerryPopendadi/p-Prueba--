# THE FACES · Plugin de WordPress «THE FACES Spa»

Archivo para instalar: **`thefaces-spa.zip`** (carpeta `thefaces/wordpress-plugin/thefaces-spa`).
Es la misma web que la previsualización (`thefaces/preview/index.html`), en 9 idiomas (English, Español, Français, Deutsch, Русский, Українська, 日本語, ไทย, Bahasa Indonesia), con SEO, ahora como plugin.

Probado en WordPress 6.6 con el tema Twenty Twenty-Four: portada, menú y salones en inglés, español y ruso, sin errores de PHP ni de JavaScript; títulos, descripciones, idioma de la página, enlaces entre idiomas (hreflang) y Google Tag Manager correctos; imágenes y vídeo cargando desde el propio plugin; sin desbordes en móvil.

---

## 1. Instalar
1. **Plugins → Añadir nuevo → Subir plugin** → `thefaces-spa.zip` → Instalar → **Activar**.
2. **Ajustes → THE FACES**:
   - **Google Tag Manager**: el ID (GTM-…). Se carga con Consent Mode v2: nada se activa hasta que el visitante acepta las cookies.
   - **Idioma por defecto**: el de la portada principal (recomendado: English).
   - **Direcciones por idioma** (activado): `/ru/`, `/es/`, `/de/`, `/th/`, `/id/`, `/ja/`; inglés sin prefijo.
   - **SEO** (activado): título, descripción, Open Graph y hreflang de cada página. Si usáis Yoast, Rank Math, AIOSEO o SEOPress, el plugin no toca título ni descripción; con Polylang o WPML, ellos ponen el hreflang.

## 2. Crear la web (un botón)
Al activar el plugin aparece arriba en el Escritorio el aviso **«THE FACES Spa: la web todavía no tiene páginas»** con el botón **«Crear la web de THE FACES»** (también en Ajustes → THE FACES). Al pulsarlo:
- crea las 153 páginas (17 páginas × 9 idiomas) con su shortcode y la plantilla de pantalla completa;
- crea los 27 artículos del Journal (3 artículos × 9 idiomas), enlazados entre sí por idioma;
- pasa a borrador el contenido de ejemplo de WordPress («Hello world!», «Sample page»);
- pone la portada en inglés como página de inicio (Ajustes → Lectura);
- activa las direcciones bonitas (`/ru/menu/`) si estaban desactivadas.
Si ya existe alguna página con esa dirección, la reutiliza: se puede pulsar más de una vez sin duplicar nada.

**Actualizar el plugin:** Plugins → Añadir nuevo → Subir plugin → el nuevo `thefaces-spa.zip` → «Reemplazar el actual con el subido».

## 2b. Crear las páginas a mano (opcional)
Cada página de WordPress lleva **un shortcode** y la plantilla **«THE FACES · pantalla completa»** (Atributos de página → Plantilla). Esa plantilla quita la cabecera y el pie del tema: la web trae los suyos.

| Página en WordPress | Dirección | Contenido |
|---|---|---|
| Inicio (Ajustes → Lectura → página de inicio) | `/` | `[thefaces page="home"]` |
| Menu | `/menu/` | `[thefaces page="menu"]` |
| Face massage | `/face-massage/` | `[thefaces page="face-massage"]` |
| Head spa | `/head-spa/` | `[thefaces page="head-spa"]` |
| Skin care | `/skin-care/` | `[thefaces page="skin-care"]` |
| Body massage | `/body-massage/` | `[thefaces page="body-massage"]` |
| Couples spa | `/couples-spa/` | `[thefaces page="couples-spa"]` |
| Five elements | `/five-elements/` | `[thefaces page="five-elements"]` |
| Ubud | `/ubud/` | `[thefaces page="ubud"]` |
| Sanur | `/sanur/` | `[thefaces page="sanur"]` |
| Founders | `/founders/` | `[thefaces page="founders"]` |
| Gift certificates | `/gift-certificates/` | `[thefaces page="gift-certificates"]` |
| Partners | `/partners/` | `[thefaces page="partners"]` |
| Journal | `/journal/` | `[thefaces page="journal"]` |

**Otros idiomas sin plugin de idiomas:** crea una página madre con el código del idioma (`ru`, `es`, `de`, `th`, `id`, `ja`) con `[thefaces page="home"]`, y dentro sus páginas hijas con los mismos nombres (`/ru/menu/`, `/ru/ubud/`…). El plugin reconoce el idioma por la dirección.

**Con Polylang o WPML:** crea las traducciones de cada página con el mismo shortcode; el plugin toma el idioma activo. Configura el idioma con prefijo en la URL (`/ru/`, `/es/`…).

**Forzar un idioma:** `[thefaces page="menu" lang="ja"]`.

## 2c. Idioma automático
En la primera visita, si la persona entra a la versión en inglés y su navegador está en otro de los 9 idiomas, la web la lleva a su versión (`/es/`, `/fr/`, `/ru/`…). Si después elige un idioma en el selector, se recuerda y se respeta siempre. Los buscadores (Google, Bing) no se redirigen: cada idioma conserva su propia dirección y su SEO.

## 2d. Blog (Journal) automático
- El botón crea 3 artículos en los 9 idiomas: «Masaje facial miofascial o escultural», «Shirodhara en Ubud» y «Cinco elementos: cómo elegir tu ritual». Cada uno se ve con el diseño de la web (cabecera, foto, texto, caja de reserva, pie) y su selector de idioma lleva a la traducción del mismo artículo.
- La sección Journal de la portada y la página `/journal/` muestran **las entradas reales** del idioma de la página, las más recientes primero.
- Para publicar un artículo nuevo: Entradas → Añadir. En «Plantilla» elige «THE FACES · pantalla completa». Para indicar el idioma añade el campo personalizado `_tf_lang` con el código (`es`, `fr`…); sin él cuenta como idioma por defecto (inglés). Para enlazar traducciones entre sí, dales el mismo campo `_tf_group`.

## 2e. Páginas de tratamientos (SEO)
Cinco páginas pensadas para búsquedas de turistas, en los 9 idiomas: **masaje facial**, **head spa**, **cuidado de la piel**, **masaje corporal** y **spa para parejas**. Cada una tiene titular H1, texto propio, CTA claro arriba («Reservar tratamiento» + «desde IDR…»), los tratamientos de esa familia con precios de Altegio, una caja de reserva al final y enlaces al resto. Aparecen en el desplegable «Tratamientos» del menú, en el menú móvil y en el pie.

## 2f. Pestaña dorada, redes y horarios
- En ordenador hay una pestaña dorada fija en el lado derecho («Reservar») que lleva a Altegio.
- Redes: Instagram @thefacesubud y @thefacesspaubud, TikTok @thefaces.bali y LinkedIn (company/the-faces), en el pie, en el menú y en la sección «Sigue nuestros rituales», que muestra los dos perfiles de Instagram como vista previa. Las fotos de esa vista previa son de la web; para mostrar las publicaciones reales hace falta conectar la API de Instagram (Meta) o un plugin de feed.
- Horarios (de Altegio): Ubud todos los días 10:00–22:00, Sanur 10:00–20:00; también en los datos para Google.

## 2g. Certificados, privacidad, condiciones, mapa del sitio, Journal y Yoast (versión 1.4.0)
- **Certificados**: certificado de marca THE FACES (IDM001282706, protegida hasta 19/06/2034) y de derechos de autor del Five Elements Concept (000638738). Página propia `/certificates/` y bloque debajo de los fundadores. En el certificado de autor la dirección particular de Evgenii está difuminada por privacidad.
- **Política de privacidad** `/privacy/` (con apartado de cookies) y **Condiciones** `/terms/` (cancelación, cambios de cita, uso y certificados regalo), en 9 idiomas. Todos los enlaces legales del pie, del aviso de cookies y de la suscripción llevan aquí; ya no se usa thefacesspa.com.
  - Responsable del tratamiento (como en thefacespeace.com): Evgenii Dubinin, nombre comercial THE FACES, NPWP indonesio como persona física, domicilio fiscal Jl. Bedugul No. 35, Sidakarya, Denpasar Selatan, Bali; correo de privacidad info@thefacespeace.com. Titular de la marca y los derechos de autor: PT. Indo Sintez Group. Todo aparece en una ficha «Datos de la empresa» al principio de `/privacy/`, con 12 apartados. **Conviene que lo revise vuestro asesor legal**: los textos no fijan plazos ni penalizaciones de cancelación; remiten a las condiciones que muestra Altegio al reservar.
- **Menú**: Tratamientos ▾ · Menú y precios · Salones ▾ (Ubud, Sanur) · Nosotros ▾ (Fundadores, Cinco sentidos, Certificados, Partners) · Regalos · Blog. Todo lleva a páginas.
- **Mapa del sitio** en el pie de todas las páginas (desplegable, 17 páginas en el idioma) + enlace al `wp-sitemap.xml` de WordPress.
- **Journal**: todas las entradas del idioma, con categorías (Rostro, Head spa, Rituales; las entradas nuevas usan su primera categoría de WordPress) y buscador instantáneo.
- **Yoast SEO**: el plugin rellena título SEO, meta descripción, frase clave e imagen/títulos para redes en las 153 páginas y 27 artículos, en su idioma. Lo hace al pulsar «Crear la web» y al actualizar el plugin. Si editas un campo a mano en Yoast, se respeta.

## 2h. Idioma del dispositivo y blog (versión 1.5.0)
- **Idioma**: la web sigue el idioma del dispositivo (ajustes del móvil o del navegador). En la primera página de cada visita lleva a la versión de ese idioma; si el idioma del dispositivo no está entre los 9, se queda en inglés. Si la persona elige otro idioma en el selector, se recuerda y manda siempre. Los buscadores no se redirigen.
- **Blog**: 12 artículos en cada idioma (108 en total) en 6 categorías: Rostro, Head spa, Rituales, Cinco elementos, Nuestra historia y Novedades. La página del blog muestra un artículo destacado, todas las entradas, las categorías con su número de artículos y el buscador. Cada artículo termina con «Sigue leyendo» (3 artículos relacionados).
- Las categorías son **categorías reales de WordPress** (una por idioma, p. ej. «Cinco elementos (ES)»); su dirección de WordPress abre el blog de ese idioma ya filtrado.
- **Escribir un artículo nuevo**: Entradas → Añadir. A la derecha, caja «THE FACES · Idioma del artículo»: elige el idioma (el diseño THE FACES viene marcado). Pon una de las categorías de ese idioma y una imagen destacada.

## 2i. SEO sin canibalización, páginas de salón y vídeo de portada (versión 1.5.3)
- **Una intención de búsqueda por página.** Portada: «day spa de los cinco elementos en Ubud y Sanur». Ubud: «spa en Ubud». Sanur: «spa en Sanur». Masaje facial, head spa, skin care, masaje corporal y parejas tienen cada una su propia página; los títulos ya no se pisan.
- **Páginas de Ubud y Sanur nuevas**, con el mismo diseño que el resto de la web pero con contenido propio en los 9 idiomas:
  - foto de portada distinta, dirección, horario y teléfono;
  - tres motivos para elegir ese salón;
  - texto SEO local;
  - tratamientos que solo hay en ese salón, con precio;
  - cómo llegar con mapa;
  - preguntas frecuentes del salón;
  - enlace al otro salón;
  - datos estructurados DaySpa, FAQ y migas de pan.
  - Ya no repiten la carta completa ni la galería de la portada.
- **La carta completa** solo está en la portada y en `/menu/`. El FAQ general (datos FAQPage) solo cuenta en la portada.
- **Bloques repetidos fuera:** fundadores ya no aparece en partners ni en certificados; sentidos y partners ya no aparecen en fundadores.
- **Artículos del Journal que repiten una página principal** (elementos, sentidos, historia, regalos, Waterfall) llevan un *canonical* hacia esa página (cinco elementos, fundadores, certificados regalo, partners). Los artículos de masaje facial y head spa siguen indexándose solos.
- Cada artículo termina con un botón hacia su tratamiento.
- **Vídeo de portada:** THE-FACES-VIDEO convertido a MP4 (H.264) para que se vea en todos los navegadores, con versión ligera para móvil (`hero-854.mp4`, 2,8 MB), versión de escritorio (`hero-1280.mp4`, 8 MB) y foto de la cascada mientras carga.
- Tras actualizar: **Ajustes > THE FACES > Volver a comprobar y completar las páginas**, para que Yoast reciba los títulos nuevos.

## 2j. Reserva por salón y carta por salón (versión 1.5.5)
- **Cada página de salón reserva en su propio Altegio.** Todos los botones de la página de Ubud, incluidos cabecera, pestaña dorada, barra del móvil y pie, abren `n831884.alteg.io/company/780725/...`. Los de Sanur abren `n811764.alteg.io/company/762669/...`. Úsalas como página de destino de las campañas de cada salón.
- **El resto de la web** (botón fijo del móvil, carta, portada y páginas de tratamientos) abre `https://n831884.alteg.io/select-city?o=`, donde el cliente elige ciudad y salón (versión 1.5.8).
- **Carta principal:** cada tratamiento lleva la marca *Ubud* / *Sanur*, o «Solo en Ubud» / «Solo en Sanur».
- **Página de cada salón:** carta completa de ese salón, con su duración y su precio (Ubud 49 tratamientos, Sanur 51, igual que en Altegio el 15/11/2026). Los exclusivos llevan la marca «Solo aquí».
- **Analítica:** el evento `booking_click` incluye `booking_salon` (`ubud`, `sanur` o `any`), para medir en GA4 / Google Ads las conversiones de cada salón.

## 2k. Páginas de salón con movimiento (versión 1.5.7)
- **Portada de cada salón:** fondo de vídeo propio. Ubud tiene cascada y terrazas de arroz (`salon-ubud.mp4`); Sanur tiene mar y costa (`salon-sanur.mp4`). Cada uno tiene versión ligera para móvil y foto mientras carga.
- Encima del vídeo flota una foto del salón real con forma de arco.
- **Tira de fotos del salón** que se desliza sola y se para al pasar el ratón.
- **Fotos con movimiento:** las del texto se desplazan a distinta velocidad con el scroll, y la foto de fondo de «Solo en este salón» hace un zoom lento.
- **Tarjetas:** se elevan al pasar el ratón.
- **Botón fijo del móvil:** dice «Reservar en Ubud» o «Reservar en Sanur» y abre el Altegio de ese salón.
- **Movimiento reducido:** si el visitante tiene activado «reducir movimiento» en su dispositivo, las animaciones se paran.

## 2l. Mejoras en móvil (versión 1.5.9)
- **Páginas más cortas:** la portada en móvil pasa de unas 37 a 27 pantallas, y los cinco elementos de 11.000 a 7.400 px.
- **Filas que se deslizan con el dedo,** con una tarjeta y un trozo de la siguiente, en lugar de bloques apilados:
  - cinco sentidos, certificados regalo, partners y blog;
  - perfiles de Instagram y certificados de marca;
  - motivos de cada salón.
  - Debajo aparece la pista «Desliza».
- **Barra de reserva de abajo:**
  - Se oculta en la primera pantalla, que ya tiene su botón, y aparece al bajar.
  - Es translúcida, con dos botones redondeados («Menú y precios» y «Reservar»).
  - Respeta la zona inferior del iPhone.
- **Más fácil de tocar y de leer:**
  - Enlaces y botones de al menos unos 40–48 px de alto: menú, idiomas, pie, Instagram y «ver todo».
  - Textos pequeños a 13–14 px.
  - En la carta de la portada, las descripciones se cortan a dos líneas.

## 2m. Portada más corta (versión 1.6.0)
- **10 bloques en lugar de 18:** portada con vídeo, filosofía, cinco sentidos, cinco elementos, tratamientos estrella, salones, «Descubre», preguntas y pie.
- **«Descubre»:** seis tarjetas con foto que llevan a cada página (carta y precios, regalos, fundadores, partners y Waterfall, certificados, blog). En móvil se deslizan con el dedo.
- **Bloques que ya no están en la portada,** pero siguen en su página: carta completa (`/menu/`), galería, Instagram (páginas de Ubud y Sanur), fundadores, certificados, regalos, partners, Waterfall y blog.
- **Altura:** en móvil, la portada pasa de unos 23.000 px a unos 11.000 px; en ordenador, a unos 14.000 px.
- **SEO:** la portada ya no repite la carta, los fundadores ni los partners, así que compite menos con esas páginas.

## 2n. Opiniones de Google (versión 1.6.1)
- **Portada y página de Sanur:** bloque «Opiniones» con la nota real de Google de **The FACES Sanur (4,9 ★, 855 reseñas, 15/11/2026)** y 4 reseñas reales.
  - Los textos son la parte visible en Google, con «…» donde Google los corta.
  - En ruso se muestran tal cual; en los demás idiomas, traducidos y marcados «Traducido del ruso».
  - Solo se muestra el nombre de pila con la inicial del apellido.
- **Botones:** «Ver todas las reseñas» y «★ Dejar una reseña» abren el perfil de Google (https://share.google/BTJjVaqg9cQkmz7Gd). En GA4 se miden con el evento `review_click` (`read` / `write`).
- **Para actualizar la nota o cambiar reseñas:** edita `thefaces/src/content_reviews.py` (rating, count, items) y vuelve a generar el plugin.
- **Datos estructurados:** no se añaden estrellas en los datos para Google, porque Google no muestra estrellas de reseñas que una empresa publica sobre sí misma en su propia web. Las estrellas en Google salen de la ficha de Google Maps.
- **Ubud:** cuando tengáis sus reseñas, se añaden igual en su página.

## 2o. Portada completa en ordenador, corta en móvil (versión 1.6.2)
- **Ordenador y tablet (más de 760 px):** portada completa, con:
  - portada con vídeo, filosofía, sentidos, elementos y tratamientos estrella;
  - carta y precios, galería, Instagram, salones y opiniones;
  - **fundadores** y **certificados**;
  - regalos, partners, Waterfall, blog y preguntas.
- **Móvil (hasta 760 px):** portada corta. Fundadores, certificados, carta, galería, Instagram, regalos, partners, Waterfall y blog se ocultan, y en su lugar aparece el bloque «Descubre» con tarjetas a cada página. El bloque «Descubre» no se ve en ordenador.
- **Cómo funciona:** el bloque «Descubre» solo existe en la portada y lleva la regla que decide qué se ve en cada pantalla. Las demás páginas no cambian.

## 2p. Seguridad (versión 1.6.3)

### Lo que hace el plugin (Ajustes > THE FACES > Seguridad, activado por defecto)
- **Cabeceras de seguridad:**
  - HTTPS estricto (HSTS, solo si la web ya va por https);
  - anti-clickjacking: nadie puede meter la web dentro de otra;
  - anti-sniffing;
  - política de referer;
  - bloqueo de cámara, micrófono y ubicación;
  - CSP básica: `frame-ancestors`, `base-uri`, `object-src` y subida automática a https.
- **No revela la versión de WordPress.**
- **No deja descubrir los nombres de usuario:** `?author=1` redirige a la portada, la API de usuarios no se ve sin iniciar sesión y no hay mapa del sitio de usuarios.
- **Freno a ataques de contraseña:** 5 intentos fallidos desde una IP la bloquean 15 minutos, incluso con la contraseña correcta. Si la web está detrás de Cloudflare, usa la IP real del visitante.
- **Errores de acceso genéricos:** «usuario o contraseña incorrectos», sin decir cuál de los dos falla.
- **Editor de código del escritorio desactivado:** si alguien entra con una cuenta robada, no puede inyectar código en temas o plugins.
- **XML-RPC desactivado:** responde 403. Desmárcalo solo si usas la app móvil de WordPress o Jetpack.
- **Sin listado de carpetas:** `index.php` vacío en cada carpeta del plugin.
- **Código del plugin revisado:**
  - todos los formularios comprueban permisos y un token de seguridad (nonce);
  - los datos se limpian al guardarse y se escapan al mostrarse;
  - ningún archivo se puede abrir directamente;
  - el JavaScript no inserta texto del visitante en la página.
- **Comprobación de seguridad** en la página de ajustes, con ✔/✖: HTTPS, usuario «admin», número de administradores, errores visibles, versión de PHP, editor desactivado y WordPress actualizado.

### Lo que hay que hacer fuera del plugin (ningún plugin puede hacerlo solo)
1. **Copias de seguridad diarias** fuera del servidor (UpdraftPlus a Google Drive, o las de tu hosting). Es la protección más importante.
2. **Verificación en dos pasos** para todos los administradores (plugin «Two Factor» o Wordfence Login Security).
3. **Contraseñas largas y únicas.** No uses un usuario llamado «admin»: crea otro administrador, pasa los contenidos a él y borra «admin».
4. **Cortafuegos y anti-DDoS:** Cloudflare gratuito delante de la web (proxy naranja, «Bot Fight Mode», SSL «Full (strict)»), o el cortafuegos de tu hosting.
5. **Actualizaciones:** WordPress, tema y plugins siempre al día. Borra los plugins y temas que no uses.
6. **HTTPS** con certificado válido y PHP 8.1 o superior en el hosting.
7. **Opcional:** Wordfence o Solid Security para escaneo de malware y avisos por email.

Ninguna web es invulnerable. Con estas capas se cubren los ataques automáticos más comunes: robo de contraseñas, búsqueda de usuarios, XML-RPC, clickjacking, inyección por el editor y versiones antiguas. Lo que queda depende sobre todo de las copias de seguridad, las actualizaciones y la verificación en dos pasos.

## 2q. Correcciones del análisis Seobility / PageSpeed (versión 1.6.4)

### Corregido en el plugin
- **Una sola etiqueta viewport:** la plantilla de pantalla completa quita la segunda que añaden los temas de bloques.
- **Favicon e icono para la pantalla de inicio del iPhone** (`apple-touch-icon`) con el logo de THE FACES. Solo se usan si en WordPress no hay un «Icono del sitio» puesto.
- **Menos encabezados:** de 54 a 42 en la portada. Los nombres de los tratamientos estrella, las categorías de la carta y los proyectos de partners ya no son encabezados; se ven igual.
- **Sin bloques de texto duplicados:** en las páginas que muestran los tratamientos estrella, esos mismos tratamientos ya no repiten la descripción en la carta.
- **Velocidad en móvil:** los vídeos de fondo (portada y salones) empiezan a cargarse cuando la página ya está cargada. Mientras tanto se ve la foto.
- **HTTPS siempre:** cualquier dirección `http://` se redirige a `https://`. Detrás de Cloudflare no se aplica, para evitar bucles.
- **Aviso en el escritorio si hay dos plugins de SEO activos.**

### Lo que hay que hacer en WordPress (no lo puede hacer el plugin)
1. **Desactivar BeyondSEO** (Plugins > BeyondSEO > Desactivar) y dejar solo **Yoast SEO**. Ahora mismo los dos escriben meta descripción, canonical y etiquetas de redes, y por eso Seobility ve «varias meta descripciones» y «varios canonical». BeyondSEO pone además su propio favicon.
2. **Icono del sitio:** Apariencia > Personalizar > Identidad del sitio, o Ajustes > General > Icono del sitio. Sube el logo cuadrado. Si no lo subes, el plugin pone el suyo.
3. **Velocidad del servidor** (0,53 s; lo recomendado es menos de 0,4 s): activa una caché de páginas. Puede ser LiteSpeed Cache si el hosting es LiteSpeed, o WP Super Cache / W3 Total Cache. Cloudflare delante de la web también ayuda.
4. **Backlinks** (Seobility: 1 dominio enlazando). Esto no se arregla en la web. Hay que conseguir enlaces desde otras webs:
   - Google Business Profile de Ubud y Sanur con el enlace a la web;
   - TripAdvisor;
   - perfiles de Instagram, TikTok y LinkedIn con el enlace;
   - thefacespeace.com y thefacesworld.com enlazando a thefacesbali.com;
   - directorios de spas de Bali, blogs de viajes y prensa local, y hoteles partners.
5. **Enlaces externos (69):** son sobre todo los botones de reserva de Altegio, WhatsApp, mapas y redes. Son necesarios; es solo una recomendación de Seobility.

## 2r. Vídeo de los fundadores (versión 1.6.5)
- **Dónde está:** en el bloque de fundadores (página Fundadores y portada en ordenador) hay ahora el vídeo de la historia de THE FACES en dos versiones:
  - English: `M43ffm_eK9o`;
  - Русский: `uaOdDmGgYvE`.
- **Qué versión se ve primero:** en ruso y ucraniano sale primero la rusa; en los demás idiomas, la inglesa. Con los botones «English / Русский» se cambia.
- **Velocidad y privacidad:** YouTube solo se carga al pulsar play, con youtube-nocookie y sin cookies hasta entonces. En GA4 se mide con el evento `video_play`.
- **Para cambiar los vídeos:** edita `FO_VIDEO` en `thefaces/src/build.py`.

## 3. Secciones sueltas
Para usar una sección dentro de otra página (por ejemplo el blog o una landing de anuncios):

`[thefaces block="senses"]` · también: `header`, `hero`, `philosophy`, `senses`, `elements`, `signatures`, `menu-builder`, `gallery`, `salons`, `founders`, `gifts`, `partners`, `waterfall`, `journal`, `faq`, `footer`.

Mejor con la plantilla de pantalla completa: dentro de la columna de un tema normal se ven estrechas.

## 4. Reserva
Todos los botones «Reservar» abren https://n831884.alteg.io, donde el cliente elige ciudad (Sanur = Denpasar), salón, tratamientos, maestro y hora. En la web no se elige ni se guarda nada antes.
Los botones de reserva tienen **el mismo aspecto que los de Altegio** (verde casi negro #060F07, esquinas redondeadas de 16 px, tipografía Inter, sin mayúsculas), para que el paso de la web a la reserva se vea continuo. Sobre fondos oscuros van en blanco con la misma forma.

Analítica: evento `booking_click` (con el botón de origen) y `menu_category` en el dataLayer.

## 5. Blog
El bloque «Journal» muestra 3 artículos de ejemplo. Para el blog real, usa las **Entradas** de WordPress en la página `/journal/` (o la página de entradas del tema) y añade `[thefaces block="header"]` y `[thefaces block="footer"]` si quieres la misma cabecera y pie.

## 6. Cambiar precios o textos
Textos, precios y diseño están en `thefaces/src/` (ver `GUIA_TILDA.md`, punto 4). Después:
```
python3 thefaces/src/build.py
```
y vuelve a subir el plugin (o sustituye sus carpetas `blocks/`, `data/` y `assets/`). La versión de Tilda sigue en `thefaces/tilda/` por si la necesitáis.

## 7. Datos pendientes
Los mismos que en `GUIA_TILDA.md`, punto 8: tercer local de Altegio (Peliatan) sin servicios, erratas en Altegio, horarios, enlaces exactos de Google Maps y fotos propias para los cinco sentidos.
