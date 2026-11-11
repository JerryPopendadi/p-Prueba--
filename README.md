# SeñalVal — Rediseño web

Web de una sola página (HTML + CSS + JS, sin dependencias) que posiciona a SeñalVal como
**gestor de proyectos de señalización de alta exigencia**. Abre `index.html` en el navegador.

## Estructura
```
index.html        Página completa (SEO, datos estructurados, secciones)
css/styles.css    Diseño (paleta corporativa blanco, negro y azul; Montserrat)
js/main.js        Menú, animaciones, carrusel de logos, formulario → email
assets/img/       Fotos y logo de SeñalVal
assets/logos/     Logos de clientes (SVG o PNG)
robots.txt, sitemap.xml
```

## Colores y logo
- La paleta es blanco, negro y azul. El azul corporativo está en una sola variable, `--blue`,
  al principio de `css/styles.css`; cámbiala por el código exacto del logo de SeñalVal
  (y `--blue-bright`, su versión clara para textos sobre negro).
- La cabecera es blanca para que el logo se vea con sus colores originales. Basta con dejar
  el archivo como `assets/img/logo-senalval.svg` (o `.png` / `.jpg`; se prueban en ese orden).

## Imágenes que hay que añadir
Si falta una imagen, la web muestra un recuadro azul con su descripción (y el logo de un cliente
se sustituye por su nombre), así que nunca se ve rota. Pon los archivos con estos nombres:

| Archivo | Contenido |
|---|---|
| `assets/img/logo-senalval.svg` (o `.png`) | Logo oficial, en sus colores originales |
| `assets/img/plaza-castilla.jpg` | Sedes judiciales, Plaza de Castilla (portada y proyecto destacado), ~1920 px |
| `assets/img/og-senalval.jpg` | Imagen para compartir en redes, 1200×630 |
| `assets/img/senaletica-interior.jpg` | Señalética interior / directorios |
| `assets/img/senalizacion-exterior.jpg` | Monolitos / exterior |
| `assets/img/rotulo-iluminado.jpg` | Rótulo iluminado |
| `assets/img/rotulacion-vehiculos.jpg` | Vehículos / flotas |
| `assets/img/vinilos.jpg` | Vinilos |
| `assets/img/senalizacion-accesible.jpg` | Braille / seguridad |
| `assets/img/salamanca.jpg`, `clece-burgos.jpg`, `fundacion-laboral.jpg`, `san-sebastian.jpg`, `autobus-clece.jpg` | Proyectos |
| `assets/logos/clece.svg`, `vias.svg`, `comunidad-madrid.svg`, `junta-cyl.svg`, `fundacion-laboral.svg`, `coca-cola.svg`, `toyota.svg` | Logos de clientes |

Exporta las fotos en JPG/WebP comprimido (≤ 250 KB, portada ≤ 400 KB) para que Google
valore bien la velocidad.

## Logos de clientes
- Incluidos: `toyota.svg` y `coca-cola.svg`, logos oficiales del paquete `simple-icons`
  (CC0; fuentes: guía de marca de Toyota y Wikimedia Commons), con sus colores de marca.
- Pendientes, que se muestran como nombre en texto hasta tener el archivo: Clece, Vías y Construcciones,
  Comunidad de Madrid, Junta de Castilla y León y Fundación Laboral de la Construcción.
  Descarga cada logo de la sala de prensa o del manual de marca de su web y guárdalo con el nombre de la tabla.
- Las marcas son propiedad de sus titulares: muéstralas solo con permiso del cliente.

## Pendiente de confirmar con SeñalVal
- Permiso para mostrar públicamente cada logo de cliente (sobre todo Coca-Cola y Toyota).
- Dirección y teléfono: añadirlos en contacto, pie y en el JSON-LD (`address`, `telephone`) mejora el SEO local.
- Documentación real disponible para licitaciones y certificaciones (ISO, etc.).
- Textos de los proyectos: los retos/soluciones son una redacción base; ajustar con datos reales (nº de señales, plazos, m²).
- Enlaces de Aviso legal, Privacidad y Cookies (obligatorios por LSSI/RGPD).

## SEO incluido
Título y descripción optimizados, canonical, Open Graph/Twitter, `lang="es"`, jerarquía H1–H3,
textos alternativos, datos estructurados Organization/LocalBusiness + OfferCatalog + WebSite + FAQPage,
sección FAQ visible, `robots.txt` y `sitemap.xml`, imagen principal precargada y el resto en carga diferida.

## Paso a WordPress
Cada sección es un bloque independiente: puede montarse con un tema ligero (p. ej. GeneratePress/Kadence)
pegando el CSS en el personalizador y las secciones como bloques HTML, o convertirse a un tema hijo.
El formulario debería pasar a Contact Form 7 / WPForms para que los mensajes lleguen sin depender del cliente de correo.
