# SeñalVal — Nueva portada web

Portada de una sola página que posiciona a SeñalVal como **gestor de proyectos de señalización
de alta exigencia**. Paleta blanco, negro y azul; tipografía Montserrat; logo original de SeñalVal.

Todas las fotos y logos se cargan **directamente desde senalval.es** (biblioteca de medios de
WordPress). Algunos logos institucionales se cargan desde Wikimedia Commons. No hay que subir imágenes.

## Para ponerla en WordPress

Los archivos listos están en `wordpress/` (se generan con `python3 tools/build_wordpress.py`):

| Archivo | Para qué |
|---|---|
| `wordpress/senalval-portada.html` | Página completa en un solo archivo. Se abre con doble clic para revisarla. |
| `wordpress/senalval-bloque.html` | El mismo contenido listo para pegar dentro de WordPress. |

Pasos con Elementor:
1. Páginas → Añadir nueva → "Editar con Elementor".
2. En ajustes de página, plantilla **Elementor Canvas** (sin cabecera ni pie del tema).
3. Arrastra un widget **HTML** y pega todo el contenido de `senalval-bloque.html`.
4. Publica y, si quieres, márcala como portada en Ajustes → Lectura.

Sin Elementor: página con plantilla en blanco + bloque **HTML personalizado** con el mismo contenido.

SEO: el título y la descripción de la página se ponen en Yoast / Rank Math:
- Título: `SeñalVal | Proyectos de señalización y señalética de alta exigencia`
- Descripción: `SeñalVal gestiona proyectos integrales de señalización y señalética: diseño, fabricación, instalación y mantenimiento para sedes públicas, sanidad, residencias, educación, industria y retail. Preparados para licitaciones.`
Los datos estructurados (empresa, dirección, teléfono, servicios y preguntas frecuentes) ya van dentro del bloque.

## Estructura del proyecto
```
docs/estudio-de-color.md Estudio de color para el perfil de cliente
index.html               Portada (fuente)
css/styles.css           Estilos
js/main.js               Interacción: portada con fotos, blog, galerías, logos, formulario
tools/build_wordpress.py Genera los archivos de wordpress/
wordpress/               Archivos listos para WordPress
robots.txt, sitemap.xml
```
Si cambias `index.html`, `css/` o `js/`, vuelve a ejecutar `python3 tools/build_wordpress.py`.

## Qué incluye
- **Menús:** menú superior con desplegables al pasar el ratón (Empresa, Servicios con fotos, Sectores, Proyectos con fotos que abren la galería);
  en el móvil, menú por grupos y barra inferior fija (Inicio, Servicios, Proyectos, Contacto, WhatsApp). Pie con menú completo.
- **Color:** paleta basada en el logo (azul SeñalVal, azul cielo, azul noche) y validada para accesibilidad. Ver `docs/estudio-de-color.md`.
- **Portada:** 5 fotos reales de sedes judiciales que se alternan, panel con lo último del blog y banda de logos de clientes.
- **Clientes (logos reales, nunca texto):** Aena, ADIF, Guardia Civil, Comunidad de Madrid, Junta de Castilla y León
  (Wikimedia Commons); Real Valladolid, Coca-Cola, Toyota, Mahou, Dragados, Hummel, Clece, Vías, Fundación Laboral,
  Emilio Moro, Gerovida y Rapimueble (bloque "Nuestros Clientes" de senalval.es); Laboral Kutxa (Wikimedia Commons).
  Si un logo no carga, se retira sin dejar hueco.
- **Sectores** con foto de fondo de trabajos reales.
- **Servicios** con fotos reales.
- **Proyectos desplegables:** cada proyecto abre una ventana con todas sus fotos (flechas, miniaturas, deslizar en el móvil)
  y su información (reto, solución, materiales, instalación) tomada de los artículos del blog, con enlace al artículo.
- **Blog:** últimos 6 artículos de WordPress, cargados automáticamente.
- **Contacto:** el formulario abre el correo del visitante (a luismi.olea@senalval.es) o WhatsApp (665 863 597)
  con la consulta ya escrita. Botón flotante de WhatsApp en el móvil.

## Guías técnicas (PDF)
En `guias/` hay tres guías A4 con el logo, fotos de proyectos reales y la normativa citada por su nombre oficial:
- `guia-planificar-senalizacion-edificio-publico.pdf`
- `guia-senalizacion-accesible-criterios-normativa.pdf`
- `guia-materiales-senalizacion.pdf`

Se regeneran con `python3 tools/guias/build_guias.py` (textos en `tools/guias/contenido.py`).
Para ofrecerlas en la web, súbelas a Medios de WordPress; los botones "Solicitar guía" piden los datos del visitante antes de enviarla.

## Vídeo de presentación
`video/senalval-presentacion.mp4`: 78 s, 1920×1080, 30 fps, sin audio. Se regenera con `python3 tools/video/build_video.py`.

## Pendiente de confirmar
- Permiso de cada cliente para mostrar su logo, en especial **Guardia Civil** (su emblema es de uso regulado),
  Aena, ADIF, Coca-Cola y Toyota.
- **Real Valladolid:** fotos del trabajo y alcance exacto (estadio, ciudad deportiva…).
- **ADIF · Gallur:** las fotos del artículo están rotas en el servidor (los archivos no existen); volver a subirlas.
- Documentación real disponible para licitaciones y certificaciones.
- Bodegas Arzuaga no aparece como cliente (fue sede de un evento, no cliente confirmado).
