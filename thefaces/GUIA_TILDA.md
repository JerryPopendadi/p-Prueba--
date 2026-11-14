# THE FACES · Nueva web del spa en Tilda

Guía de montaje, estructura, estudio de mercado y datos pendientes de confirmar.
Previsualización: `thefaces/index.html` (abrir en el navegador). Bloques listos para pegar: carpeta `thefaces/tilda/`.

---

## 1. Qué hacemos y por qué

**Una sola web** que sustituye a thefacesworld.com (Tilda, conceptos y precios) y a thefacesspa.com (catálogo y reserva Altegio). Usa el **lenguaje visual de thefacespeace.com**, que es el rebranding: negro y blanco, Montserrat fina (200–300), titulares grandes, numeración «01 — Philosophy», fotos en blanco y negro que ganan color al pasar el ratón y vídeo de portada.

La recomendación de marketing (ver mensaje de la responsable de publicidad) queda resuelta así:

| Lo que pidió | Cómo queda en la nueva web |
|---|---|
| 1. Unir los dos sitios, página de los 5 elementos, historia y fundadores | Una web con: 5 elementos, menú, salones, «Our story» con Anna y Evgenii Dubinin, certificados, partners y blog |
| 2. Cada servicio con descripción y **precios** | Menú completo de 57 servicios con duración y precio en IDR, por categorías, visible antes de reservar |
| 3. Reserva en la propia web, eligiendo servicios | Constructor **«Your ritual»**: el cliente añade tratamientos con «+», ve tiempo y total, elige Ubud o Sanur y pasa a Altegio (maestro y hora) o envía la lista por WhatsApp |
| 4. DataLayer para e-commerce | Eventos GA4 estándar: `view_item_list`, `add_to_cart`, `remove_from_cart`, `view_cart`, `select_salon`, `begin_checkout`, `generate_lead` con artículos, precio y salón |

**Embudo resultante:** anuncio → página con precios → elige servicios (add_to_cart) → elige salón → Altegio/WhatsApp (begin_checkout + generate_lead) → reserva confirmada en Altegio (purchase, ver punto 6.4).
El clic en «Book» deja de ser una conversión falsa: quien llega a Altegio ya conoce el precio y lleva servicios elegidos.

---

## 2. Mapa del sitio

Portada larga (la previsualización) + páginas propias para SEO y anuncios:

| URL | Contenido | Para qué |
|---|---|---|
| `/` | Vídeo, filosofía, 5 elementos, tratamientos estrella, menú + constructor, galería, salones, historia, certificados, partners, blog, FAQ | Entrada principal |
| `/rituals/air` … `/rituals/love` | Una página por elemento: cuándo elegirlo, qué incluye, 3 h · IDR 1.800.000, botón «Add to ritual» | Anuncios por elemento, SEO |
| `/face-massage`, `/head-spa`, `/body` | Cada dirección con descripción larga, fotos y su parte del menú | Lo que pidió marketing (punto 2); SEO «face massage Ubud», «head spa Bali» |
| `/ubud`, `/sanur` | Dirección, mapa, horario, teléfono, WhatsApp, menú de ese salón | Google Business Profile apunta aquí |
| `/gift-certificates` | 4 certificados con bonus | Venta directa |
| `/partners` | Proyectos de inversión, franquicia, spa en hotel, empleo → enlaza a thefacespeace.com | «Ser partner / formar parte» |
| `/journal` | Blog (Tilda Feeds) | SEO y contenido para redes |
| `/faq`, `/legal/*` | Preguntas, cancelación, privacidad, cookies, términos | Confianza y ley |

Idiomas: **EN** (principal), **RU** e **ID**, cada uno como copia de página: `/ru/...`, `/id/...`.

---

## 3. Sistema de diseño (igual que thefacespeace.com)

| Elemento | Valor |
|---|---|
| Fuente | Montserrat: 200 titulares, 300 texto, 500 etiquetas en mayúsculas |
| Etiquetas | 11 px, mayúsculas, espaciado 0,24 em («01 — PHILOSOPHY») |
| Titulares | 40–96 px, peso 200, interlineado 1,05 |
| Colores | Negro `#0A0A0A`, blanco `#FFFFFF`, arena `#F4F3EF`, texto `#2B2724`, gris `#6F6A64`, dorado (solo detalles) `#C9A35A`, WhatsApp `#25D366` |
| Botones | Rectangulares, borde 1 px, texto 11 px en mayúsculas; relleno al pasar el ratón |
| Fotos | Blanco y negro → color al pasar el ratón; zoom lento al aparecer |
| Movimiento | Texto que sube al cargar, fade-up al hacer scroll, parallax suave, galería en dos filas que se desliza, palabras en marquesina, vídeo con zoom lento (Ken Burns). Todo se desactiva si el usuario pide «reducir movimiento» |
| Logo | `assets/logo-white.png` (fondo oscuro) y `assets/logo-black.png` (fondo claro), sacados del logo de thefacespeace.com |

---

## 4. Montaje en Tilda paso a paso

### 4.1 Proyecto
1. **Crear proyecto** nuevo (o duplicar el de thefacesworld.com para conservar dominio y estadísticas).
2. **Site settings → Fonts and colors:** fuente principal *Montserrat* (Google Fonts), color de texto `#2B2724`, color de enlaces `#0A0A0A`.
3. **Site settings → More → HTML code for the HEAD section:** pegar `tilda/00-head-code.html` (Consent Mode + Google Tag Manager + fuente). Cambiar `GTM-XXXXXXX` por el ID real.
4. **Favicon:** subir el logo negro recortado.
5. **Domain:** primero en el subdominio `*.tilda.ws` para revisar; al final apuntar thefacesworld.com (y redirigir thefacesspa.com, ver 6.5).

### 4.2 Cabecera
1. Añadir bloque de **Menú** (categoría *Menu*) con logo a la izquierda, enlaces en el centro y botón a la derecha; o un **Zero Block** de 80 px de alto si se quiere exactamente igual que la previsualización.
2. Ajustes del bloque: *Fixed* (fija arriba), fondo transparente al inicio y `#0A0A0A` al bajar (opción de cambio de fondo al hacer scroll).
3. Enlaces: Philosophy, Five elements, Menu & prices, Salons, About, Gift cards, Partnership, Journal; selector EN · RU · ID; botón **Book** → ancla `#menu`.
4. En móvil Tilda muestra el menú hamburguesa automáticamente. Añadir abajo un bloque fijo de 2 botones (Menu & prices / Your ritual) o pegar la barra del archivo de previsualización (`.mbar`).

### 4.3 Portada con vídeo
1. **Zero Block**, altura 100 % de la ventana, fondo `#0A0A0A`.
2. Añadir elemento **Video**: subir el vídeo a Vimeo o YouTube (o usar `assets/hero-720.mp4`, 2,7 MB, 25 s, sin texto incrustado). Activar *autoplay, loop, mute* y estirarlo a toda la pantalla.
3. Encima, un rectángulo negro con opacidad 45 % para que se lea el texto.
4. Textos: etiqueta «SPA IN UBUD & SANUR · BALI», titular «Five elements. One ritual.», subtítulo y dos botones (*Build your ritual* → `#menu`, *Choose by how you feel* → `#elements`).
5. **Animación** (pestaña *Animation* de cada elemento): titular *Fade in + move up*, 1,2 s; subtítulo y botones con 0,3 s y 0,5 s de retraso.
6. Opcional: filtro blanco y negro al vídeo editándolo antes de subir (Tilda no aplica filtros a vídeo).

> Nota: el vídeo de thefacespeace.com tiene al principio la frase en ruso «Природа всегда знала путь к гармонии» y al final el logo «Franchise». Por eso la previsualización usa solo el tramo de 6,5 s a 31,5 s.

### 4.4 Filosofía, elementos, tratamientos estrella
- **Filosofía:** Zero Block con dos fotos superpuestas (`g04-interior`, `g08-interior`). Animación *Zoom out* en las fotos y *Fade up* en el texto. En la foto pequeña, *Parallax* (Animation → Parallax, velocidad lenta).
- **Marquesina de palabras** (Air · Fire · Water · Earth · Love…): bloque de **línea de texto en movimiento** de Tilda o T123 con el `.words` de la previsualización.
- **Cinco elementos:** Zero Block con 5 columnas de foto en blanco y negro. Cada columna: nombre, frase corta y al pasar el ratón (*Hover* en Zero Block) la foto pasa a color y aparece «cuándo elegirlo», «qué incluye», precio y botón *Add to ritual*. En móvil, una tarjeta debajo de otra. Cada elemento enlaza también a su página `/rituals/...`.
- **Tratamientos estrella:** bloque de **galería/slider de tarjetas** con foto, nombre, duración, precio y botón. Myofascial, Shirodhara, Airkiss Detox, Jet Lag, Sculptural, Beauty & Detox.

### 4.5 Menú con precios + constructor «Your ritual» (la parte clave)
1. Añadir bloque **T123 (HTML code)**, en *Other*.
2. Pegar entero `tilda/04-menu-booking-builder.html`.
3. Darle al bloque el ancla `menu` (Settings → Block ID / anchor) para que funcionen los botones «Book».
4. Publicar y probar: añadir 2 tratamientos, cambiar a Sanur, pulsar WhatsApp: debe abrirse el chat de Sanur con la lista y el total.

**Para cambiar precios o servicios:** en la previsualización `index.html`, dentro de `const MENU=[...]`, cada línea es
`['categoría','id','Nombre',minutos,precio,'Descripción']`. Después ejecutar `python3 thefaces/tools/build_tilda_block.py` y volver a pegar el bloque. Un servicio solo de Sanur lleva `['sanur']` al final (ej. Sacred Honeymoon).

Números y enlaces que usa el bloque:

| Salón | WhatsApp | Reserva online |
|---|---|---|
| Ubud | +62 822 6699 9965 | https://n831884.alteg.io/ |
| Sanur | +62 813 3770 9190 | https://n811764.alteg.io/ |

### 4.6 Galería en movimiento
Bloque **T123** con `tilda/05-gallery-marquee.html`. Dos filas de fotos que se deslizan en sentidos opuestos y se paran al pasar el ratón. Cambiar las URLs por las de Tilda después de subir las fotos.

### 4.7 Salones, historia, certificados, partners
- **Salones:** bloque de 2 columnas con foto, dirección y botones (Book in Ubud, WhatsApp, llamar, Cómo llegar a Google Maps). Debajo: «Coming soon · The Faces Ubud Spa, Jl. Made Lebah 36, Peliatan».
- **Our story:** Zero Block negro con foto en parallax, texto, línea de tiempo (2013 primer salón · +5 salones incl. CUBO Eslovenia · Love Spa Ubud → The Faces Ubud y Sanur) y cifras 20+ / 2 / 50+ (animación de contador: bloque de números de Tilda).
- **Certificados:** bloque de 4 tarjetas. Botón «Order» → WhatsApp con el importe, o **formulario de pago de Tilda** (Tilda acepta pagos con Stripe/PayPal; para Indonesia comprobar Midtrans o Xendit vía Zapier/webhook).
- **Partnership:** Zero Block con foto de WATERFALL de fondo en parallax, 4 tarjetas de proyectos que enlazan a thefacespeace.com, 3 vías (invertir/franquicia, spa en hotel, unirse al equipo) y botones «Request a partnership call», «Partner catalogues», «Join the team». Incluir el aviso legal de que no es una oferta de valores.

### 4.8 Blog
1. **Tilda Feeds** (en el panel del proyecto: *Feeds*). Crear feed «Journal» con categorías: Face, Head spa, Rituals, Bali.
2. Página `/journal` con bloque de lista de feed; en portada, bloque de 3 últimas publicaciones.
3. Primeros artículos propuestos (en la previsualización): «Myofascial or sculptural face massage: which one to choose», «Shirodhara hair spa in Ubud: what happens in those two hours», «Jet lag in Bali: a spa plan for your first and last day». Cada artículo termina con botón «Add to ritual» del tratamiento.

### 4.9 FAQ, pie y redes
- FAQ: bloque de **acordeón** con las 7 preguntas.
- Pie negro: logo, texto, iconos de **Instagram** (instagram.com/thefacesbali, sin `?igsh=`), **TikTok** (@the.faces.ubud), **WhatsApp**, email, suscripción por email, enlaces a reserva online por salón, a THE FACES Network (thefacespeace.com), a Partnership y a los textos legales.

### 4.10 Idiomas
1. Terminar EN completa. **Duplicar** cada página para `/ru/` y `/id/` y traducir.
2. En cada página: *Settings → SEO* → título y descripción propios en su idioma, y en *Settings → More* los enlaces alternativos (hreflang).
3. Selector EN · RU · ID en la cabecera enlazando a la misma página en el otro idioma.

### 4.11 SEO por página (ejemplos)
| Página | Title | Description |
|---|---|---|
| Portada EN | The Faces Spa Bali · Face massage & head spa in Ubud and Sanur | Face massage, vegan head spa and five-element rituals. Full menu with prices from IDR 300,000. Book online or by WhatsApp. |
| Portada RU | The Faces Spa Бали · массаж лица и хэд-спа в Убуде и Сануре | Массаж лица, веган хэд-спа и ритуалы пяти стихий. Полное меню с ценами от 300 000 IDR. Запись онлайн или в WhatsApp. |
| /ubud | The Faces Spa Ubud · Face massage & head spa, Kedewatan | Address, hours, menu and prices of The Faces Ubud. Book online or WhatsApp +62 822 6699 9965. |

Además: imagen de vista previa (OG) 1200×630 por idioma, *alt* en cada foto, enviar el sitemap de Tilda a Google Search Console y Bing.

---

## 5. Animaciones en Tilda: qué usar para cada efecto

| Efecto de la previsualización | En Tilda |
|---|---|
| Titular que sube al cargar | Zero Block → Animation → *Fade in*, dirección arriba |
| Aparecer al hacer scroll | Animation básica en cada elemento (*Fade in / Zoom in*) |
| Parallax de fotos | Animation → *Parallax* (Zero Block) o fondo *Parallax* en bloques de portada |
| Foto B/N → color al pasar | Zero Block → *Hover* (filtro/opacidad) o dos capas de imagen |
| Columnas de elementos que se expanden | Zero Block con *Step-by-step animation* (trigger: hover) o T123 con el código de la previsualización |
| Galería que se desliza | `tilda/05-gallery-marquee.html` |
| Vídeo con zoom lento | Editado en el propio vídeo, o T123 con la animación `kb` de la previsualización |

Regla de estilo Aman: movimientos **lentos** (1–1,8 s), suaves, nunca rebotes ni giros.

---

## 6. Reserva, analítica y conversiones

### 6.1 Flujo de reserva
1. El cliente elige servicios en «Your ritual» (o pulsa «Add to ritual» en un elemento o tratamiento estrella).
2. Elige salón (Ubud/Sanur). Los servicios solo de un salón cambian el salón automáticamente.
3. Opción A: **Pick master & time** → abre el calendario de Altegio del salón para elegir maestro y hora.
   Opción B: **WhatsApp** → mensaje ya escrito con servicios, duración, total, salón y hora preferida.

### 6.2 Reserva sin salir de la web (fase 2)
Altegio ofrece un **widget** (botón o ventana) que se pega en Tilda con su código, de modo que el calendario se abre encima de la web en lugar de en otra pestaña. Pasos:
1. En Altegio: *Online booking → Widget*, crear widget para cada salón y copiar el código.
2. Pegarlo en un T123 y conectar el botón «Pick master & time» para que abra el widget del salón elegido.
3. Pedir a Altegio los **ID de cada servicio** para preseleccionar en el widget lo que el cliente eligió en «Your ritual». Esto hay que confirmarlo con el soporte de Altegio (formato de enlace con servicio preseleccionado).
4. **Pago/depósito online:** Altegio tiene pagos online en algunos países; para Indonesia comprobar qué pasarela admite (Midtrans, Xendit). Si no, depósito por enlace de pago.

### 6.3 Eventos del dataLayer (ya programados)
| Evento | Cuándo | Datos |
|---|---|---|
| `view_item_list` | Al ver una categoría del menú | lista de servicios |
| `add_to_cart` / `remove_from_cart` | «+» o «×» | servicio, categoría, precio, salón |
| `view_cart` | Abrir «Your ritual» | servicios elegidos |
| `select_salon` | Cambiar Ubud/Sanur | salón |
| `begin_checkout` + `generate_lead` | Clic en Altegio o WhatsApp | servicios, valor total en IDR, salón, `booking_method` (altegio / whatsapp) |

En **GTM**: crear activadores de *Evento personalizado* con esos nombres y etiquetas GA4 *Event* con «Enviar datos de comercio electrónico» activado. En Google Ads y Meta, optimizar por `generate_lead` (con valor) en vez del clic en «Book».

### 6.4 La reserva confirmada (purchase)
La reserva real ocurre en Altegio. Opciones, de mejor a más simple:
1. Integración de analítica de Altegio (GA4 / Meta Pixel en el widget), si su cuenta la tiene: envía la reserva completada.
2. Webhook de Altegio → servidor/Zapier → Measurement Protocol de GA4 y Conversions API de Meta.
3. Mínimo: importar las reservas de Altegio a Google Ads como conversiones offline una vez por semana.
Esto hay que hablarlo con los desarrolladores y con Altegio, como dice la propuesta de marketing.

### 6.5 Dominio único
Publicar la nueva web en **thefacesworld.com** (o en thefacesspa.com si se prefiere ese nombre) y redirigir el otro dominio página a página (301) para no perder posiciones en Google. Mantener los textos legales en `/legal/...`.

---

## 7. Estudio de mercado y referencia Aman

### 7.1 Precios de la competencia (orientativos)
| Spa | Zona | Precio | Nivel |
|---|---|---|---|
| Karsa Spa | Ubud | Masaje balinés 60 min ≈ IDR 180.000; 90 min ≈ 250.000 | Económico, muy demandado (se llena con una semana de antelación) |
| Lasati Spa (Beehouse Dijiwa) | Ubud | Facial 60 min IDR 450.000 | Medio |
| COMO Uma Ubud | Ubud | Taksu massage 90 min IDR 1.100.000; 120 min 1.500.000 | Hotel de lujo |
| Anantara Ubud | Ubud | Taksu massage 60 min IDR 2.250.000++; faciales 60 min 2,5–3,2 M | Hotel de lujo |
| Mandara Day Spa | Sanur | Masaje de cabeza 15 min IDR 100.000 | Cadena |
| The Nest / Glo Day Spa | Sanur | Masaje 60 min desde IDR 255.000–280.000 | Medio |
| **The Faces** | Ubud + Sanur | Masaje facial 90 min IDR 850–900 mil; Shirodhara 2 h 1.650.000; rituales 3 h 1.800.000 | **Premium de día, por debajo de los hoteles de lujo** |

**Lectura:** The Faces está entre los day spa (200–500 mil) y los spa de hotel (1,1–3,2 M). Sus precios son más altos que un day spa, así que la web tiene que **justificarlos**: técnica (miofascial, escultural, Shirodhara), duración larga, concepto de 5 elementos, fundadores con 20+ años. Pocos day spa de la zona publican el menú completo con precios en la web; enseñarlo es una ventaja.

### 7.2 Qué tomar de Aman (aman.com, Aman Spa)
- **Imagen a pantalla completa y poco texto:** la foto o el vídeo hablan primero.
- **Calma:** mucho espacio en blanco, tipografía fina, transiciones lentas, paleta neutra.
- **Narrativa del bienestar** como identidad, no lista de servicios: en The Faces, los 5 elementos y el amor.
- **Separar «Spa experiences» y «Wellness experiences»:** aquí, tratamientos sueltos vs rituales de 3 h y paquetes.
- **Reservar siempre a mano:** botón fijo arriba y barra inferior en móvil.
- Su rediseño se asocia a un aumento de ingresos del 25 % según la agencia (dato de la propia agencia, no independiente).

### 7.3 Posicionamiento propuesto
«Five elements. One ritual.» Masaje facial de autor, head spa vegano y rituales largos en Ubud y Sanur, con precios abiertos. Público: viajeras 28–50 (Rusia/CIS, Europa, Australia), parejas, y quien llega con jet lag. Ventaja frente a todos: concepto propio + tres idiomas + reserva clara por salón.

Fuentes: [COMO Uma Ubud spa menu](https://kompastour.com/useruploads/tiny_MCE/indonesia/bali/como_uma_ubud/como_uma_ubud_SPA_menu.pdf) · [Anantara Ubud spa menu dic. 2025](https://www.anantara.com/uploads/minor/anantara/documents/anantara-ubud-bali-resort/anantara-spa/spa-menu-updated-dec-2025.pdf) · [Anantara price list](https://www.anantara.com/uploads/minor/anantara/documents/anantara-ubud-bali-resort/anantara-spa/anantara_spa_price_list.pdf) · [Lasati Spa menu](https://dijiwasanctuaries.com/property/facility/lasati_spa_menu_edit.pdf) · [Karsa Spa (bali.live)](https://bali.live/p/karsa-spa-best-massage-in-ubud) · [Karsa Spa 2026 (trvlogue)](https://www.trvlogue.com/zh-Hant/karsa-spa-ubud-massage) · [Mandara Day Spa menú](https://www.mandaraspa.com/wp-content/uploads/160925-DAY-SPA_Web-Menu-ENG.pdf) · [Best spas in Sanur (Honeycombers)](https://thehoneycombers.com/bali/best-spas-in-sanur-massage-mani-pedi/) · [Aman: caso Inviqa](https://inviqa.com/case-studies/aman) · [Nucleus: arquitectura del lujo digital](https://www.nucleus.co.uk/opinion/The-Architecture-Of-Digital-Luxury) · [Ejemplos de webs de spa (Greenlit)](https://greenlitcontent.com/website/26-spa-website-examples-we-love-in-2024-and-what-makes-them-so-great)

---

## 8. Datos a confirmar con Anna antes de publicar

| Tema | Lo que encontré | Usado en la previsualización |
|---|---|---|
| Airkiss Detox Ritual | 1.200.000 en thefacesspa / 1.300.000 en thefacesworld | 1.200.000 |
| Full body massage 90 min | 900.000 / 850.000 | 900.000 |
| Certificados regalo | La web dice +20 % / +15 %, pero los importes dan otra cosa: 1,2 M→1,5 M (+25 %), 4 M→5 M (+25 %), 12,75 M→15 M (+18 %) y «30 M → total 25,5 M» (al revés) | Pagar 1,2/4/12,75/25,5 M → recibir 1,5/5/15/30 M |
| «Candal treatment» | Probablemente *Candle* | «Candle treatment» |
| Signature «The FACES» y «Author» | Sin descripción | Sin descripción |
| Menú de Sanur | «casi igual» + Sacred Honeymoon (3 h 20, 3.800.000) y The Faces Retreat (2 días, sin precio) | Honeymoon marcado «Sanur only»; Retreat pendiente |
| Horarios de los salones | No aparecen en ninguna web | No incluidos |
| Nombre del fundador | Evgeny (thefacesworld) / Evgenii (thefacespeace) | Evgenii, como el rebranding |
| Email | La web antigua muestra «thefacesorld@gmail.com» (falta la w) y enlaza a thefacesworld@gmail.com | thefacesworld@gmail.com; mejor uno del dominio |
| 5 elementos | La historia antigua menciona «metal»; la web nueva usa Air, Fire, Water, Earth, Love | Air, Fire, Water, Earth, Love |
| Página «constructor» que tenéis | Aún no la he visto | El constructor «Your ritual» la sustituye; cuando me la paséis, la integro |

Erratas corregidas del texto antiguo: «pay att attention to every y detail», «creators and creators», «smell, smell», «ta aste», «mnas», «& BLANCE», «PRIVELEGE».

---

## 9. Lista antes de publicar
- [ ] Precios y certificados confirmados (punto 8)
- [ ] GTM con el ID real, eventos probados en *Vista previa* de GTM
- [ ] Banner de cookies conectado a `tfConsent(true/false)`
- [ ] WhatsApp de Ubud y Sanur probados desde el móvil
- [ ] Enlaces Altegio de cada salón probados
- [ ] Títulos, descripciones y OG en EN, RU, ID
- [ ] Fotos con *alt* y comprimidas (WebP)
- [ ] Search Console + Bing + Google Business Profile de los dos salones apuntando a `/ubud` y `/sanur`
- [ ] Redirecciones 301 del dominio antiguo
