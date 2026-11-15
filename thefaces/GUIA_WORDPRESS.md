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
