# Paso a paso: web + pagos + app de Lera + app de alumnas

Todo funciona **gratis** sobre la cuenta de Google de Lera. No hay servidor que pagar.

```
Web (WordPress) ──► formulario ──► API (Apps Script) ──► Google Sheet  ◄── Panel de Lera (móvil)
                       pago: Stripe / PayPal / USDT ─────────┘               │  chat
App de alumnas  ◄── login con código por email ── API ── mensajes ──────────┘
```

## Lo que hay
| Pieza | Para quién | Qué hace |
|---|---|---|
| `index.html` | clientas | web en 5 idiomas, programas, horarios, reserva y pago |
| **Panel de Lera** (`crm/app.gs` + `crm/app.html`) | Lera | hoy, chats, solicitudes, clientas, grupos, dinero |
| **App de alumnas** (`crm/student.gs` + `crm/student.html`) | clientas que pagaron | próximas clases + Zoom, sesiones restantes, **chat con Lera**, materiales; 5 idiomas |
| `crm/api.gs` | — | recibe solicitudes y pagos (PayPal, Payhip), sirve la app de alumnas |
| Google Sheet | Lera | todo queda guardado; se puede descargar como Excel |

**Acceso a la app de alumnas (sin contraseña que compartir):**
- La alumna pone su email y recibe un código de 6 dígitos válido 10 minutos.
- Solo pueden entrar clientas con estado «Активен» (activa).
- Máximo 2 dispositivos: si entra en un 3.º, el más antiguo se cierra.
- Cuando termina su paquete, Lera la pasa a «Архив» y pierde el acceso.

---

## PASO 0 — Pedir a Lera
1. **Una cuenta de Google (Gmail)**. Todo se crea dentro de ella. Mejor que te dé acceso como editor, o hacerlo juntas por videollamada. Activar la verificación en 2 pasos.
2. Email de **PayPal Business** (sin contraseña).
3. Si tiene **Stripe** (sí/no y país).
4. Dirección **USDT TRC20** (si quiere cobrar en cripto).
5. Su **WhatsApp** y un **enlace fijo de Zoom**.

## PASO 1 — Crear la tabla (5 min)
1. En el Google Drive de Lera: **Nuevo → Hojas de cálculo**, nombre `Lera CRM`.
2. Copiar el **ID** de la dirección: `docs.google.com/spreadsheets/d/`**`ESTE_TROZO`**`/edit`.

## PASO 2 — Proyecto «API» (10 min)
1. En la tabla: **Extensiones → Apps Script**. Nombre del proyecto: `Lera API`.
2. Archivo `Código.gs`: borrar todo y pegar **`crm/api.gs`**.
3. **＋ → Script**, nombre `student`: pegar **`crm/student.gs`**.
4. **＋ → HTML**, nombre `student`: pegar **`crm/student.html`**.
5. ⚙️ **Configuración del proyecto** → «Mostrar appsscript.json» ✔ → en el editor abrir `appsscript.json` y pegar **`crm/appsscript.api.json`**.
6. **Implementar → Nueva implementación → Aplicación web**. Ejecutar como: **Yo**. Acceso: **Cualquier usuario**. → Implementar → Autorizar.
7. Copiar la URL `https://script.google.com/macros/s/…/exec`. Es la **URL API**.
   - App de alumnas = **URL API + `?page=app`**.

## PASO 3 — Proyecto «Panel de Lera» (10 min)
1. Abrir [script.google.com](https://script.google.com) → **Nuevo proyecto** → nombre `Lera Panel`.
2. `Código.gs` ← **`crm/app.gs`**. **＋ → HTML** nombre `app` ← **`crm/app.html`**. `appsscript.json` ← **`crm/appsscript.app.json`**.
3. ⚙️ **Propiedades del script → Añadir**:
   - `SHEET_ID` = el ID del paso 1;
   - `STRIPE_SECRET_KEY` = clave restringida de Stripe (si hay Stripe).
4. Arriba elegir la función **`setup`** → **Ejecutar** → Autorizar.
   Crea todas las hojas (Заявки, Клиенты, Занятия, Оплаты, Группы, Программы, Настройки, Сообщения, Доступ, Материалы), los precios y los automatismos.
5. **Implementar → Aplicación web**. Ejecutar como: **Yo**. Acceso: **Solo yo**.
6. Abrir esa URL **en el móvil de Lera** (con su Google) → Compartir → **«Añadir a pantalla de inicio»**. Ya tiene su app.

## PASO 4 — Rellenar «Настройки» en la tabla (3 min)
| Clave | Valor |
|---|---|
| `OWNER_EMAIL` | email de Lera (avisos) |
| `ZOOM_LINK` | su enlace fijo de Zoom |
| `PAYPAL_EMAIL` | email de PayPal |
| `STUDENT_APP_URL` | URL API + `?page=app` |
| `TELEGRAM_CHAT_ID` | opcional, ver paso 7 |

## PASO 5 — La web (15 min)
1. Abrir `index.html` con un editor de texto. Al principio, en el bloque `CONFIG`, rellenar:
   - `apiUrl` — la URL API;
   - `appUrl` — URL API + `?page=app` (aparece el botón **App** en la web);
   - `paypal.email`;
   - `crypto.address` + `crypto.contact` (`https://wa.me/NUMERO?text={msg}`);
   - `programs.*.stripe` — enlaces de pago de Stripe, si hay;
   - `supportEmail`.
2. Subir a WordPress (Hostinger o IONOS):
   - Medios → subir todo `img/`;
   - en `index.html` cambiar `src="img/` por la URL de la carpeta de medios;
   - Página nueva → plantilla **vacía / Elementor Canvas** → bloque **HTML personalizado** → pegar todo `index.html`;
   - Ajustes → Lectura → página de inicio.
3. Crear las páginas `/privacy-policy/`, `/terms/`, `/refund-policy/`. Stripe y PayPal las revisan.

## PASO 6 — Pagos
Detalle completo en **`PAYMENTS.md`**. Resumen:
- **PayPal**: solo email. Los pagos se marcan solos en la tabla (aviso IPN).
- **Stripe**: enlaces de pago + clave de solo lectura. Se marcan solos cada 15 min.
- **USDT**: manual. Lera ve el dinero en su wallet → Panel → Dinero → «＋ вручную» → Solicitudes → «Сделать клиентом».
- **PDF**: Payhip (sello con email del comprador).

## PASO 7 — Avisos al móvil de Lera por Telegram (opcional, 5 min)
1. En Telegram abrir **@BotFather** → `/newbot` → copiar el **token**.
2. Proyecto **Lera API** → Propiedades del script → `TELEGRAM_BOT_TOKEN` = token.
3. Lera escribe cualquier cosa a su bot nuevo. Luego abre **@userinfobot** y copia su **ID**.
4. Tabla → «Настройки» → `TELEGRAM_CHAT_ID` = ese ID.
5. Llegan avisos «🌿 Nueva solicitud» y «💬 mensaje de alumna».

## PASO 8 — Materiales para alumnas
En la hoja **«Материалы»**, una fila por material:
- Название — título;
- Ссылка — enlace `https://…`;
- Программы — `все` (todas) o el nombre del programa;
- Описание — descripción corta.

Los enlaces pueden ser:
- vídeos en YouTube **ocultos** o Vimeo privado;
- descarga de Payhip;
- PDF de Drive (pero quien tenga el enlace podrá abrirlo).

## PASO 9 — Probar todo (10 min)
1. Hoja **«Клиенты»**: añadir una fila con **tu** email, nombre, programa, `8` en «Занятий всего», `0` en «Проведено», `8` en «Осталось», `Активен` en «Статус».
2. Abrir la app de alumnas (URL API + `?page=app`) → tu email → código del correo → entrar.
3. Escribir en el chat → en el Panel de Lera, pestaña **Чаты**, aparece con punto rojo → responder → en tu app aparece la respuesta (en unos 6 s).
4. En el panel: **＋ Занятие** para tu email → te llega invitación de calendario y la clase aparece en tu app con botón Zoom.
5. En la web: reservar → elegir PayPal → pagar 1 $ de prueba → en la tabla aparece «Оплачено».

## Uso diario de Lera (lo único que tiene que hacer)
1. Abrir su app → pestaña **Сегодня**: clases de hoy, solicitudes nuevas, chats sin leer.
2. Responder chats.
3. Poner clases con **＋ Занятие**.
4. Tras cada clase: **✓ Проведено**.
5. Cada mañana a las 8:00 le llega un email con el resumen.

---

## Límites honestos
- Al abrir la app de alumnas directamente, Google muestra arriba una franja gris («creado por otro usuario»).
  Para que se vea 100 % de marca, insertarla en una página de la web (`/app`) con un iframe:
  `<iframe src="URL_API?page=app" style="width:100%;height:100vh;border:0"></iframe>`.
- Gmail gratuito puede enviar **100 emails/día** (códigos, avisos, confirmaciones). Con Google Workspace son 1 500.
- El chat se actualiza cada 6 s, no es instantáneo como WhatsApp. Para muchas clientas (100+) conviene pasar a una app propia (Firebase/Supabase), y los datos de la tabla se pueden migrar.
- Compartir no se puede impedir al 100 %. Lo que hay lo hace difícil: código al email de la dueña, 2 dispositivos, acceso solo mientras la clienta esté activa.
