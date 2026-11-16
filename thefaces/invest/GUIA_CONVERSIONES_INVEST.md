# THE FACES INVEST · v03: vídeo, formulario y conversiones

Página: `thefacespeace.com/book-an-investor-meeting/` (widget HTML de Elementor).
Archivo nuevo: `the-faces-invest-v03.html` → sustituye todo el contenido del widget HTML.

## Qué cambia en v03
- **Vídeo de los fundadores** (inglés `M43ffm_eK9o` / ruso `uaOdDmGgYvE`) debajo del bloque «Founders».
  - En ruso se ve el ruso; en los demás idiomas, el inglés. Botones English / Русский.
  - YouTube solo se carga al pulsar play, sin cookies antes.
- **Formulario propio dentro de la tarjeta de contacto.** Ya no hace falta el widget Shortcode de Fluent Forms, que en la página real no estaba, por eso la tarjeta se quedaba en «Loading the form…».
  - **Campos obligatorios:** nombre, email válido, país, interés y casilla de 18+ / privacidad.
  - **Antispam:** casilla trampa invisible, bloqueo de envíos instantáneos y de reenvíos en 30 s.
  - **Con datos vacíos no se envía nada,** ni desde el navegador ni en el script de Google.
  - **Interés preseleccionado:** al pulsar «Ask about this project / route», el campo ya trae ese proyecto o formato.
- **Cada solicitud se guarda en una hoja de Google** y os llega un **email al momento** con todos los datos y la campaña de origen.
- **Conversión** `generate_lead` en el dataLayer con:
  - `lead_id`, `interest`, `country`, `form_language`, `placement` (botón pulsado), `value`;
  - además, UTM y gclid.

## 1. Activar la hoja de Google + email (5 minutos)
1. Crea una Hoja de cálculo de Google: «THE FACES INVEST · Leads».
2. En la hoja: **Extensiones → Apps Script**. Borra el código de ejemplo, pega `google-apps-script-leads.gs` y **guarda**.
   - Si el email debe ir a otra dirección, cambia `NOTIFY`.
3. **Implementar → Nueva implementación → tipo «Aplicación web»**:
   - Ejecutar como: **Yo**.
   - Quién tiene acceso: **Cualquier usuario**.
   - → Implementar → acepta los permisos.
4. Copia la **URL de la aplicación web** (termina en `/exec`).
5. En `the-faces-invest-v03.html`, busca `sheetUrl:''` y pega la URL: `sheetUrl:'https://script.google.com/macros/s/…/exec'`.
6. Pega el HTML en el widget de Elementor → Actualizar. Si quieres, borra el widget Shortcode de Fluent Forms.
7. Prueba enviando una solicitud tuya. Debe aparecer una fila en la pestaña **Leads** y llegar el email.

Sin `sheetUrl`, el formulario vuelve a Fluent Forms. En ese caso hace falta el widget Shortcode `[fluentform id="3"]` debajo del HTML.

## 2. Registrar la conversión en Google (Google Tag Manager `GTM-PHJSTTBR`)
1. **Variables → Nueva → Variable de capa de datos**, una por cada una: `lead_id`, `interest`, `country`, `form_language`, `placement`, `value`.
2. **Activador:** Evento personalizado → nombre del evento `generate_lead`.
3. **Etiqueta GA4 – Evento:**
   - nombre `generate_lead`;
   - parámetros: `lead_id`, `interest`, `country`, `form_language`, `placement`, `value`, `currency = USD`;
   - activador: el anterior.
4. **Etiqueta Google Ads – Seguimiento de conversiones:**
   - ID `18528850470` (la cuenta AW- que ya está en la web);
   - etiqueta de conversión: la que te da Google Ads (Objetivos → Conversiones → Nueva → Sitio web → «Enviar formulario de clientes potenciales»);
   - **ID de transacción = `{{lead_id}}`**, para no contar dos veces;
   - activador `generate_lead`.
   - Comprueba que existe la etiqueta **Vinculador de conversiones** en todas las páginas.
5. **Publicar** el contenedor.
6. En **GA4 → Administrar → Eventos clave**, marca `generate_lead` como evento clave. En **Definiciones personalizadas**, crea dimensiones para `interest`, `country`, `form_language` y `placement`.

Eventos extra que ya envía la página:
- `thefaces_form_start` (empieza a rellenar);
- `thefaces_form_error` (error de validación y campo);
- `thefaces_cta` (botón pulsado);
- `thefaces_booking_click` (calendario);
- `thefaces_video_play`.

## 3. Saber exactamente cuándo hay una conversión
- **Al momento:** email a `NOTIFY` con nombre, email, país, interés, mensaje y campaña (UTM y gclid).
- **Historial completo:** la hoja de Google (pestaña Leads), con fecha y hora. La columna `status` es para marcar new / contacted / qualified…
- **En Google:** GA4 → Tiempo real y Eventos clave; Google Ads → Conversiones, con el `lead_id` de cada una.
- **Opcional:** con el `gclid` guardado en la hoja se pueden importar a Google Ads las conversiones offline («reunión hecha», «firmado»).

## 4. Mensajes vacíos: qué más revisar en WordPress
- El formulario nuevo no permite envíos vacíos, y el script de Google también los rechaza.
- Los mensajes vacíos que llegaban venían muy probablemente de **bots que envían Fluent Forms / Contact Form 7 directamente**, sin pasar por la página.
- **Fluent Forms:** si ya no lo usas, desactiva el formulario 3. Si lo mantienes:
  - marca los campos como **obligatorios**;
  - activa **Honeypot** y **Cloudflare Turnstile o reCAPTCHA** (Fluent Forms → Global Settings → Security);
  - en la notificación por email usa `{all_data}`.
- **Contact Form 7** también está instalado: si no lo usas, desactívalo.
- **Barra de contacto de todo el sitio (WPCode):** en esta página el formulario «Send a request» (`#tff-form`) aparece **dos veces**. El snippet está instalado dos veces (WPCode y Elementor Custom Code). Deja solo uno.
