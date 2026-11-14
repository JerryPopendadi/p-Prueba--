# THE FACES · Web del spa en Tilda, por bloques y en 7 idiomas

Previsualización completa: abre `thefaces/preview/index.html` (elige idioma) — son las 9 páginas × 7 idiomas, igual que quedarán en Tilda.
Bloques para pegar: carpeta `thefaces/tilda/`. Mapa del sitio, títulos y descripciones SEO: `thefaces/SEO_ESTRUCTURA.md`.

---

## 1. Qué hay y cómo está organizado

```
tilda/
  00-site-head.html            ← UNA vez para todo el sitio (estilos, comportamiento, cookies, GTM, fuentes)
  en/ ru/ es/ de/ th/ id/ ja/  ← un juego de bloques por idioma
     01-header.html … 15-footer.html     ← secciones de la portada (T123)
     pages/<página>-intro.html           ← H1 + migas de pan de cada página interior
     pages/<página>-01-header.html       ← cabecera de esa página (su selector de idioma apunta a la misma página)
     pages/<página>-15-footer.html       ← pie de esa página
     head/<página>.html                  ← código HEAD de cada página (hreflang + Open Graph)
```

### Los 15 bloques
| Nº | Bloque | Qué muestra |
|---|---|---|
| 01 | header | Logo, menú, selector de 7 idiomas, «Tu ritual» con contador, botón Reservar, menú móvil |
| 02 | hero | **Vídeo** a pantalla completa, H1 con palabras clave, «Cinco elementos. Un ritual.», 2 botones |
| 03 | philosophy | Filosofía con fotos superpuestas y marquesina de palabras en movimiento |
| 04 | senses | **Los 5 sentidos + intuición**: imagen grande fija que cambia al hacer scroll (vista, oído, olfato, tacto, gusto, intuición), número gigante, puntos de progreso. En móvil, cada sentido con su foto |
| 05 | elements | Los 5 elementos en columnas que se expanden: cuándo elegirlo, qué incluye, precio, «Añadir al ritual» |
| 06 | signatures | Carrusel de 6 tratamientos estrella |
| 07 | menu-builder | Menú completo (57 servicios, precios en el HTML para Google) + constructor «Tu ritual» → Altegio o WhatsApp |
| 08 | gallery | Galería en dos filas que se deslizan |
| 09 | salons | Ubud y Sanur: dirección, reservar, WhatsApp, teléfono, cómo llegar (la reserva online va a n831884.alteg.io) |
| 10 | founders | **Anna y Evgenii Dubinin**: foto grande, historia, cita, línea de tiempo, cifras |
| 11 | gifts | 4 certificados con bonus |
| 12 | partners | 4 proyectos, invertir/franquicia, spa en hotel, empleo → thefacespeace.com |
| 13 | journal | 3 artículos del blog |
| 14 | faq | 7 preguntas + datos estructurados FAQPage |
| 16 | waterfall | **Próximamente: THE FACES Waterfall Spa** — lema, texto de bienvenida, 2 fotos de la obra y los 6 rituales (Tierra, Agua, Fuego, Aire, Silencio, Amor) desplegables, sin precios; botón «Avísame cuando abra» (WhatsApp). Va después del 12 en la portada y en Partners |
| 15 | footer | Redes, enlaces a todas las páginas e idiomas, legales, barra inferior móvil, aviso de cookies, datos estructurados del negocio (DaySpa × 2) |

### Las 9 páginas (en cada idioma)
| Página | URL | Bloques |
|---|---|---|
| Portada | `/` | 01 → 12, 16, 13 → 15 |
| Menú y precios | `/menu` | header · intro · 07 · 06 · 14 · footer |
| Cinco elementos y sentidos | `/five-elements` | header · intro · 04 · 05 · 07 · 14 · footer |
| Ubud | `/ubud` | header · intro · 09 · 07 · 08 · 14 · footer |
| Sanur | `/sanur` | header · intro · 09 · 07 · 08 · 14 · footer |
| Fundadores | `/founders` | header · intro · 10 · 03 · 04 · 12 · footer |
| Certificados | `/gift-certificates` | header · intro · 11 · 06 · 14 · footer |
| Partners | `/partners` | header · intro · 12 · 16 · 10 · footer |
| Journal (blog) | `/journal` | header · intro · 13 · footer + Tilda Feeds |

URLs por idioma: inglés sin prefijo (`/menu`), el resto con prefijo: `/ru/menu`, `/es/menu`, `/de/menu`, `/th/menu`, `/id/menu`, `/ja/menu`.

---

## 2. Montaje en Tilda paso a paso

### Paso 1 · Proyecto y cabecera del sitio
1. Crea el proyecto (o usa el de thefacesworld.com).
2. **Site settings → More → HTML code for the HEAD section** → pega `tilda/00-site-head.html` entero.
3. En ese mismo código cambia `GTM-XXXXXXX` por el ID real de Google Tag Manager (mientras diga XXXX no se carga nada).
4. **Site settings → SEO**: desactiva el banner de cookies de Tilda si lo hubiera (ya viene uno en el bloque 15).

### Paso 2 · Crear las páginas
Por cada idioma crea las 9 páginas con su dirección (Page settings → Page address):
- Inglés: `/` (portada, márcala como *Home page*), `menu`, `five-elements`, `ubud`, `sanur`, `founders`, `gift-certificates`, `partners`, `journal`.
- Otros idiomas: `ru`, `ru/menu`, `ru/five-elements`… y lo mismo con `es`, `de`, `th`, `id`, `ja`.

Consejo: monta primero toda la versión inglesa, **duplica** cada página y sustituye los bloques por los del otro idioma.

### Paso 3 · Pegar los bloques
1. En la página: **+ Add block → Other → T123 (HTML code)**.
2. Abre el archivo (ej. `tilda/es/02-hero.html`), copia todo y pégalo. Un bloque T123 por archivo, en el orden de la tabla.
3. En las páginas interiores usa `pages/<página>-01-header.html`, después `pages/<página>-intro.html`, los bloques de la tabla y al final `pages/<página>-15-footer.html`.
4. Pulsa **Publish**. En el editor de Tilda los bloques T123 no se ven animados: compruébalo en la página publicada.

### Paso 4 · SEO de cada página
En `SEO_ESTRUCTURA.md` tienes, por idioma y página, el **Title** y la **Description** (con su longitud).
1. **Page settings → SEO**: pega Title y Description; activa la indexación.
2. **Page settings → Additional → HTML code for the HEAD**: pega `tilda/<idioma>/head/<página>.html` (enlaces hreflang entre los 7 idiomas + imagen para redes).
3. **Page settings → Language**: elige el idioma de la página (Tilda lo pone en `<html lang>`).
4. **Facebook & Social**: imagen `assets/og-1200x630.jpg` (logo sobre foto en blanco y negro).

### Paso 5 · Blog
**Tilda Feeds** → crea un feed «Journal» por idioma (o uno con categoría por idioma). En `/journal` añade el bloque de lista de Feeds debajo del bloque 13. Cada artículo termina con un botón al menú (`/menu`).

### Paso 6 · Dominio y Google
1. Conecta thefacesworld.com (o el dominio elegido) y redirige el antiguo con 301.
2. Google Search Console: añade el dominio, envía `sitemap.xml` (Tilda lo genera) y pide indexar la portada de cada idioma.
3. Bing Webmaster Tools: importa desde Search Console.
4. Google Business Profile de Ubud y Sanur: enlaza a `/ubud` y `/sanur`.

---

## 3. Imágenes y vídeo (importante)
Los bloques cargan fotos y vídeo desde un CDN público (jsDelivr) que lee la carpeta `thefaces/assets` de este repositorio, fijado a una versión concreta. **Si el repositorio es privado, no se verán.** Dos opciones:
- **A (recomendada para producción):** sube las imágenes a Tilda (cualquier bloque de imagen → copiar enlace), apunta cada URL en `src/assets_map.json` así: `{"founders.webp": "https://static.tildacdn.com/…/founders.webp"}` y ejecuta `python3 thefaces/src/build.py`. Todos los bloques se regeneran con las URLs de Tilda.
- **B:** pon otra dirección base en `src/assets_base.txt` (tu propio hosting o CDN) y vuelve a generar.

**Fotos que conviene sustituir por material propio en alta calidad:** las 6 de los sentidos son fotogramas del vídeo de thefacespeace.com (sirven para la maqueta, pero son de baja resolución). Ideal: vista (velas/luz en sala), oído (cuencos tibetanos), olfato (flores y aceites), tacto (manos en un masaje facial), gusto (té de hierbas servido tras el ritual), intuición (la imagen de las manos ya es buena).

---

## 4. Cambiar textos o precios
Todo sale de `thefaces/src/`:
| Archivo | Qué contiene |
|---|---|
| `menu.py` | Servicios, duración, **precios**, certificados, salones, teléfonos, enlaces Altegio y redes |
| `content_ui.py` | Textos de todas las secciones en los 7 idiomas |
| `content_rich.py` | Sentidos, elementos, descripciones del menú y preguntas frecuentes en los 7 idiomas |
| `content_seo.py` | Páginas, bloques de cada página, títulos y descripciones SEO |
| `site.css` / `site.js` | Diseño y comportamiento |

Después: `python3 thefaces/src/build.py` → vuelve a pegar en Tilda los bloques que cambiaron (si cambias precios: el bloque 07 y, si afecta, 05, 06 y 11).

---

## 5. Idiomas: notas
- **Indonesio (Bahasa Indonesia)** es la versión «de Bali»: es el idioma oficial, el que usa Google en Indonesia y el del equipo. Si quieres además frases en **balinés** (Basa Bali), como saludo «Om Swastiastu» en la portada o en los rituales, se pueden añadir como detalle de marca; para SEO no aporta búsquedas.
- Los **nombres de los tratamientos** se mantienen en inglés en todos los idiomas, como en la carta del spa; las descripciones sí están traducidas.
- Las traducciones al **tailandés, japonés y alemán** conviene que las revise un nativo antes de publicar (las de ruso, español, inglés e indonesio están listas para revisión normal).
- El **mensaje de WhatsApp** que recibe el equipo llega en ruso desde la web rusa, en indonesio desde la indonesia y en inglés desde el resto, para que el personal lo entienda siempre.
- Fuentes: Montserrat (como thefacespeace.com) + Noto Sans Thai y Noto Sans JP para tailandés y japonés; solo se descargan si la página las necesita.

---

## 6. SEO incluido
- Un **H1 por página** con palabras clave (portada: «Face massage, head spa & five-element rituals in Ubud and Sanur, Bali» y su traducción).
- **Title y description** propios en cada página e idioma (63 combinaciones) en `SEO_ESTRUCTURA.md`.
- **hreflang** entre los 7 idiomas + `x-default`.
- **Datos estructurados**: Organization con fundadores, DaySpa de Ubud y Sanur (dirección, teléfono, rango de precios, reserva), FAQPage, BreadcrumbList.
- **Menú y precios en el HTML** (no cargados por JavaScript), para que Google los lea.
- Enlazado interno: menú, pie y bloques enlazan a las páginas de salón, menú, elementos, fundadores, certificados y partners.
- Imágenes con `alt` traducido, carga diferida, tamaños declarados.

Probado en la previsualización: las 63 páginas sin errores, con un solo H1, datos estructurados válidos y sin desbordes en escritorio (1440 px) ni en móvil (iPhone 13).

---

## 7. Reserva y analítica
El cliente elige tratamientos y salón en la web y después:
- **Reserva online:** se abre **tal cual** la página de Altegio https://n831884.alteg.io (la misma para los dos salones). Allí elige ciudad (Ubud, o **Denpasar = Sanur**), salón, maestro y hora. Esta página no se modifica ni se incrusta.
- **WhatsApp:** mensaje ya escrito con los tratamientos, la duración, el total y el salón. Eventos GA4 en el dataLayer: `view_item_list`, `add_to_cart`, `remove_from_cart`, `view_cart`, `select_salon`, `begin_checkout`, `generate_lead` (con valor en IDR, salón y método). El aviso de cookies activa Google Consent Mode v2: nada de analítica ni publicidad hasta que el visitante acepta.

Para medir la reserva confirmada sin tocar la página de Altegio: activar en Altegio su integración con Google Analytics / Meta Pixel (si la cuenta la tiene) o importar las reservas a Google Ads como conversiones offline.

---

## 8. Datos a confirmar antes de publicar
| Tema | Situación |
|---|---|
| Airkiss Detox | 1.200.000 o 1.300.000 (dos webs distintas) — usado 1.200.000 |
| Masaje corporal 90 min | 900.000 o 850.000 — usado 900.000 |
| Certificados | Usado: pagas 1,2 / 4 / 12,75 / 25,5 M → recibes 1,5 / 5 / 15 / 30 M (la web antigua no cuadraba) |
| Horarios | No aparecen en ninguna web: añadirlos a `menu.py` y a los datos estructurados |
| The Faces Retreat (Sanur) | Sin precio |
| Coordenadas de los salones | Para el mapa y Google: enviar enlace exacto de Google Maps de cada salón |
| Email | thefacesworld@gmail.com; mejor uno del dominio |
| Fotos de los sentidos | Sustituir por fotos propias (punto 3) |

---

## 9. Estudio de mercado (resumen)
The Faces está entre los day spa de Ubud/Sanur (masaje 60 min ≈ IDR 180–280 mil) y los spa de hotel de lujo (COMO Uma, Anantara: 1,1–3,2 M). Su ventaja: técnica de autor (miofascial, escultural, Shirodhara), rituales largos, concepto propio (5 elementos + 5 sentidos + amor), fundadoras con 20+ años, precios abiertos y web en 7 idiomas. De Aman tomamos: imagen a pantalla completa, poco texto, movimiento lento, narrativa de bienestar y botón de reserva siempre visible.

Fuentes: [COMO Uma Ubud](https://kompastour.com/useruploads/tiny_MCE/indonesia/bali/como_uma_ubud/como_uma_ubud_SPA_menu.pdf) · [Anantara Ubud dic. 2025](https://www.anantara.com/uploads/minor/anantara/documents/anantara-ubud-bali-resort/anantara-spa/spa-menu-updated-dec-2025.pdf) · [Lasati Spa](https://dijiwasanctuaries.com/property/facility/lasati_spa_menu_edit.pdf) · [Karsa Spa](https://bali.live/p/karsa-spa-best-massage-in-ubud) · [Mandara Day Spa](https://www.mandaraspa.com/wp-content/uploads/160925-DAY-SPA_Web-Menu-ENG.pdf) · [Spas en Sanur (Honeycombers)](https://thehoneycombers.com/bali/best-spas-in-sanur-massage-mani-pedi/) · [Aman: caso Inviqa](https://inviqa.com/case-studies/aman) · [Nucleus: lujo digital](https://www.nucleus.co.uk/opinion/The-Architecture-Of-Digital-Luxury)
