# THE FACES · Plugin de WordPress «THE FACES Spa»

Archivo para instalar: **`thefaces-spa.zip`** (carpeta `thefaces/wordpress-plugin/thefaces-spa`).
Es la misma web que la previsualización (`thefaces/preview/index.html`), en 7 idiomas, con SEO, ahora como plugin.

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
- crea las 63 páginas (9 páginas × 7 idiomas) con su shortcode y la plantilla de pantalla completa;
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
