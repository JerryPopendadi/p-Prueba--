# SEO y velocidad de senalval.es · Plan de mejora (noviembre 2026)

Resultados de partida: PageSpeed móvil 57 y ordenador 74; Seobility con avisos en título, encabezados,
imágenes, negritas, enlaces, redes sociales, tiempo de respuesta y backlinks.

## 1. Lo que ya está corregido en el código (`wordpress/senalval-portada-optimizada.html`)
Se ha partido de la portada **publicada** (no se pierde ninguno de los cambios hechos en la web).

| Aviso | Antes | Ahora |
|---|---|---|
| Encabezados vacíos | 3 | 0 |
| Número de encabezados H | 61 | 41 |
| Imágenes sin texto ALT | 27 | 0 |
| Negrita repetida («Inventario final») | 2 | 0 |
| Enlaces con el mismo texto repetido | 36 | 6 (menú principal, inevitables) |
| Redes sociales | ninguna | Instagram + compartir en LinkedIn, Facebook, X, WhatsApp y email |
| Imágenes descargadas al abrir la página (móvil) | 26 · 2,3 MB | 18 · 1,8 MB |

Cambios de velocidad: las fotos 2-5 de la portada se descargan justo antes de mostrarse; las miniaturas del
menú, al abrirlo; el blog y los logos de clientes, después de que la página haya cargado; las fotos de
Wikimedia, a 640 px en lugar de 1280 px.

## 2. Título y descripción (Yoast SEO → bloque bajo el editor de la portada)
- **Título SEO** (≈ 50 caracteres, Seobility lo quiere por debajo de ~580 px):
  `Señalética y señalización en Valladolid | SeñalVal`
- **Meta descripción** (≈ 155 caracteres):
  `Proyectos de señalización de alta exigencia: diseño, fabricación e instalación para sedes judiciales, sanidad, residencias y empresas en toda España.`
- En Yoast → pestaña **Social**: imagen `ROTULO-PLAZA-DE-CASTILLA.jpg` (ahora comparte el logo, que se ve pequeño).

## 3. Velocidad del servidor (tiempo de respuesta 1,05 s → objetivo < 0,4 s)
No depende del código de la portada, sino de WordPress y del hosting:
1. **Plugin de caché.** Si el hosting usa LiteSpeed: *LiteSpeed Cache*. Si no: *WP Super Cache* o *WP Fastest Cache*
   (gratis). Activa caché de página, compresión y «Lazy load». Tras activarlo, vuelve a medir.
2. **Quitar lo que la portada no usa.** La portada carga 18 scripts y 21 hojas de estilo del tema Konte y sus
   complementos (jQuery, slick, masonry, countdown…) que no necesita. Con el plugin gratuito **Asset CleanUp**:
   en la portada, desactiva los scripts de `konte`, `konte-addons`, `masonry`, `slick`, `circle-progress`,
   `jquery.countdown` y las hojas de estilo de Elementor que no usa. Comprueba la web después de cada cambio.
3. **Wordfence:** en *Wordfence → All Options*, desactiva «Live Traffic» si no lo usas (consume recursos en cada visita).
4. Si con caché el tiempo sigue por encima de 0,8 s, el problema es el hosting: pide al proveedor PHP 8.2+ y OPcache,
   o valora un plan con LiteSpeed.

## 4. Backlinks (enlaces desde otras webs: 6 desde 3 dominios)
No se arregla con código: hay que conseguir que otras webs enlacen a senalval.es. Por orden de impacto:
1. **Perfil de Empresa de Google** (Google Maps) con la web, fotos de proyectos y reseñas de clientes.
2. Directorios de empresas: Páginas Amarillas, Infoisinfo, Cylex, Europages, Kompass, Habitissimo.
3. **Clientes y colaboradores:** pedir a constructoras y empresas con las que trabajáis (Clece, Vías, Fundación
   Laboral…) que os citen en su web como proveedor, o publicar el caso conjunto.
4. Asociaciones del sector y la Cámara de Comercio de Valladolid (directorio de socios).
5. Notas de prensa en medios locales (El Norte de Castilla, Diario de Valladolid) con proyectos destacados,
   por ejemplo las sedes judiciales de Madrid.
6. Perfiles en LinkedIn (empresa), Instagram y YouTube (subir el vídeo de presentación) con enlace a la web.
