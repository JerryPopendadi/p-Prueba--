=== THE FACES Spa ===
Requires at least: 5.8
Requires PHP: 7.4
Stable tag: 1.5.7
License: GPL-2.0-or-later

Web de THE FACES Spa (Ubud y Sanur, Bali) en 9 idiomas como plugin de WordPress, con idioma automático según el navegador y blog (Journal) creado automáticamente.

== Descripción ==
Portada con vídeo, cinco sentidos, cinco elementos, tratamientos estrella, menú completo con los precios de Altegio,
galería en movimiento, salones, fundadores, certificados regalo, partners, Próximamente Waterfall Spa, blog y preguntas.
Idiomas: English, Español, Français, Deutsch, Русский, Українська, 日本語, ไทย, Bahasa Indonesia.
Todos los botones «Reservar» abren https://n831884.alteg.io.

== Instalación ==
1. Plugins > Añadir nuevo > Subir plugin > thefaces-spa.zip > Instalar > Activar.
2. Ajustes > THE FACES: ID de Google Tag Manager e idioma por defecto.
3. Crea la página de inicio con la plantilla «THE FACES · pantalla completa» y el contenido [thefaces page="home"].

== Shortcodes ==
[thefaces page="home"]  (también: menu, five-elements, ubud, sanur, founders, gift-certificates, partners, journal)
[thefaces block="senses"]  (header, hero, philosophy, senses, elements, signatures, menu-builder, gallery, salons, founders, gifts, partners, waterfall, journal, faq, footer)
[thefaces page="menu" lang="ru"]  (fuerza el idioma)

== Cambiar precios o textos ==
Los textos y precios están en thefaces/src del repositorio. Tras cambiarlos: python3 thefaces/src/build.py
y vuelve a subir el plugin (o sustituye las carpetas blocks/ y data/).
