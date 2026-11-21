# THE FACES INVEST · v05 · Forminator 703 + conversiones

Página: `thefacespeace.com/book-an-investor-meeting/`
Archivo: `the-faces-invest-v05.html` → sustituye **todo** el contenido del widget HTML de Elementor.

**Sobre los corchetes.** El shortcode de Forminator 703 ya está dentro del HTML, en la tarjeta de contacto, y es lo **único** entre corchetes. Este WordPress ejecuta los shortcodes dentro del widget HTML. No escribas nunca otro shortcode en el código, en los comentarios ni en el script, porque rompe la página. No hace falta ningún widget Shortcode aparte; si existe uno con Fluent Forms, bórralo.

---

## 1. Preparar el formulario 703 en Forminator (Forminator → Forms → 703 → Edit)

### Campos
Crea los campos en este orden. Así sus **Field ID** coinciden con el código. Si alguno no coincide, lee el apartado «Si los Field ID no coinciden».

| # | Tipo de campo en Forminator | Field ID | Etiqueta (ejemplo) | ¿Obligatorio? |
|---|---|---|---|---|
| 1 | Name | `name-1` | Full name | Sí |
| 2 | Email | `email-1` | Email | Sí |
| 3 | Phone | `phone-1` | Phone / WhatsApp | No |
| 4 | Input (texto) | `text-1` | Country of residence | Sí |
| 5 | Select | `select-1` | You are | Sí |
| 6 | Select | `select-2` | I am interested in | Sí |
| 7 | Select | `select-3` | Indicative budget | No |
| 8 | Select | `select-4` | Preferred contact | No |
| 9 | Textarea | `textarea-1` | Your message | No |
| 10 | GDPR Approval | `gdprcheckbox-1` | I am 18+, I have read the privacy notice and understand this page is not an offer | Sí |
| 11–18 | Hidden (×8) | `hidden-1` … `hidden-8` | ver abajo | — |

### Opciones de los desplegables
En cada opción, pon el **Value** igual que el texto, o el valor de la columna Value.

- **select-1 «You are»:** Private investor · Family office / fund · Hotel or resort owner · Developer / property owner · Spa operator / entrepreneur · Other
- **select-2 «I am interested in»:** THE FACES Ubud · operating spa · THE FACES SANUR · Five Elements · The White Temple · Sanur · WATERFALL · Ubud · Any Bali project · Hotel & resort spas · Spa development · Wellness management · Franchise & licensing · Strategic partnerships · Other
  - Con estos textos, al pulsar «Ask about this project» en la página, el interés se elige solo.
- **select-3 «Indicative budget»:** Prefer to discuss · < US$100,000 · US$100,000 – 250,000 · US$250,000 – 500,000 · US$500,000 – 1,000,000 · > US$1,000,000
- **select-4 «Preferred contact»:** Email · WhatsApp · Video call · Phone call

### Campos ocultos
En cada campo Hidden, **Default value = «Custom value»** y déjalo vacío: la página los rellena al enviar.

| Field ID | Etiqueta | La página pone |
|---|---|---|
| `hidden-1` | Lead ID | ID único de la solicitud (el mismo que recibe Google Ads) |
| `hidden-2` | Language | idioma de la página |
| `hidden-3` | Clicked | botón pulsado antes (`proj_ub`, `route_3`, `hero`…) |
| `hidden-4` | UTM source | `utm_source` |
| `hidden-5` | UTM medium | `utm_medium` |
| `hidden-6` | UTM campaign | `utm_campaign` |
| `hidden-7` | GCLID | `gclid` de Google Ads |
| `hidden-8` | Page | dirección de la página |

### Comportamiento (pestaña Behaviour)
- **Submission method: AJAX.** Es obligatorio para que la página detecte la conversión.
- **After submission:** «Inline message». Ejemplo: «Thank you, we have received your enquiry. We reply within 2 working days.»
- **Spam protection:** activa **Honeypot**. Mejor aún, añade un campo **reCAPTCHA v3 / hCaptcha / Turnstile** (Forminator → Settings → CAPTCHA).
- **Envíos limitados:** si tu versión lo tiene, activa «Prevent multiple submissions».

### Notificación por email (pestaña Email Notifications)
- **Admin email:** a `info@thefacespeace.com`. Asunto: `New enquiry · {name-1} · {select-2}`. Cuerpo: `{all_fields}`.
- **Opcional:** email de confirmación al cliente (`{email-1}`) con el enlace del calendario: https://calendar.app.google/b7nddp1H5fBoGYT98

### Guardar en Google Sheets (gratis en Forminator)
1. **Forminator → Integrations → Google Sheets → Connect:** inicia sesión con la cuenta de Google donde quieres la hoja.
2. **Forminator → Forms → 703 → Integrations → Google Sheets → Activate:** elige una carpeta de Drive y un nombre de hoja, por ejemplo «THE FACES INVEST · Leads».

Cada envío crea una fila con todos los campos, incluidos los ocultos: campaña, gclid y botón pulsado. Además, las entradas siempre quedan en **Forminator → Submissions**.

### Si los Field ID no coinciden
En el HTML, busca `fields:{name:'name-1'` y `hidden:{lead_id:'hidden-1'`. Cambia el nombre de la derecha por el Field ID real que ves en Forminator (al editar cada campo, arriba aparece «Field ID»). Si el formulario no tiene un campo, pon `''`.

---

## 2. Conversión en Google (Tag Manager `GTM-PHJSTTBR` + Google Ads + GA4)

Cuando Forminator confirma el envío, la página manda a `dataLayer` el evento **`generate_lead`** con:
- `lead_id`, `profile`, `interest`, `budget`, `contact_pref`, `country`, `form_language`, `placement`, `value`, `currency`;
- `utm_source`, `utm_medium`, `utm_campaign`, `gclid`.

**Solo se cuenta si el envío ha ido bien**: los envíos vacíos o fallidos no cuentan.

### Google Ads: crear la conversión
1. **Objetivos → Conversiones → Nueva acción de conversión → Sitio web → «Manualmente con código».** No uses «Carga de la página»: contaría cada visita.
2. **Categoría:** «Enviar formulario de clientes potenciales». **Valor:** el mismo para cada conversión (por ejemplo 50 USD) o ninguno. **Recuento:** «Una». **Ventana:** 90 días. **Atribución:** basada en datos.
3. Elige **«Usar Google Tag Manager»** y apunta el **ID de conversión** (`18528850470`) y la **Etiqueta de conversión**.

### Google Tag Manager
1. **Variables → Nueva → Variable de capa de datos**, una por cada una: `lead_id`, `profile`, `interest`, `budget`, `country`, `form_language`, `placement`, `value`.
2. **Activadores → Nuevo → Evento personalizado** → nombre del evento: `generate_lead`.
3. **Etiqueta «Seguimiento de conversiones de Google Ads»:**
   - ID `18528850470`;
   - la etiqueta de conversión del paso anterior;
   - valor `{{value}}` y moneda `USD`;
   - **ID de transacción `{{lead_id}}`**;
   - activador `generate_lead`.
4. **Etiqueta «Google Analytics: evento GA4»:**
   - nombre `generate_lead`;
   - parámetros: `lead_id`, `profile`, `interest`, `budget`, `country`, `form_language`, `placement`, `value`, `currency`;
   - activador `generate_lead`.
5. Comprueba que existe la etiqueta **«Vinculador de conversiones»** con activador «All Pages».
6. **Vista previa:** envía una prueba y mira que se disparen las dos etiquetas. Después, **Enviar → Publicar**.

### GA4
- **Administrar → Eventos clave:** marca `generate_lead`.
- **Administrar → Definiciones personalizadas:** crea dimensiones de evento para `profile`, `interest`, `budget`, `country`, `form_language` y `placement`. Así ves de dónde vienen y qué buscan los contactos.

### Si pones valor a la conversión
En el HTML cambia `leadValue:0` por el mismo número, por ejemplo `leadValue:50`.

---

## 3. Cómo sabrás cada conversión
- **Al momento:** email de Forminator a info@thefacespeace.com.
- **Historial:** la hoja de Google Sheets y Forminator → Submissions, con el lead ID, la campaña y el gclid.
- **En Google:** Google Ads → Conversiones (con el `lead_id` como ID de transacción) y GA4 → Eventos clave y Tiempo real.

## 4. Lista final
- [ ] Pegar `the-faces-invest-v05.html` en el widget HTML. Borrar antes todo lo anterior.
- [ ] Borrar el widget Shortcode de Fluent Forms y desactivar el formulario Fluent Forms #3 (es el que enviaba mensajes vacíos).
- [ ] Forminator 703: campos obligatorios, AJAX, honeypot o captcha, notificación y Google Sheets.
- [ ] Google Ads: conversión manual + etiqueta en GTM con ID de transacción `{{lead_id}}`. Publicar el contenedor.
- [ ] GA4: `generate_lead` como evento clave.
- [ ] Vaciar la caché del sitio y hacer un envío de prueba.
- [ ] Barra de contacto de todo el sitio: dejar una sola copia (está instalada dos veces).
