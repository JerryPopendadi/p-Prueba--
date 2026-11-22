# Seguridad de la web de Lera

## Lo que ya está hecho en la web (`lera-web`)
| Medida | Qué evita |
|---|---|
| **Web estática** | No hay base de datos, contraseñas ni PDF en el servidor: no hay nada que robar ahí. |
| **Pagos fuera de la web** (Payhip + PayPal) | Los datos de tarjeta nunca pasan por la web de Lera. |
| **0 scripts de terceros** | Se quitó el script de Payhip y el de un CDN externo: los botones son enlaces directos a Payhip. Nadie de fuera puede inyectar código. |
| **Fuentes y QR dentro de la propia web** | No se envían las IP de las visitantes a Google ni a ningún CDN (mejor también para el RGPD). |
| **Content-Security-Policy estricta** (archivo `_headers`) | El navegador solo ejecuta los scripts exactos de la web, verificados por hash. Cualquier script añadido o inyectado se bloquea. |
| **Anti-iframe** (`frame-ancestors 'none'`, `X-Frame-Options`) | Nadie puede meter la web de Lera dentro de otra página para engañar a la gente (clickjacking). |
| **HTTPS obligatorio** (HSTS) | La conexión siempre va cifrada. |
| **nosniff, Referrer-Policy, Permissions-Policy** | El navegador no adivina tipos de archivo, no envía datos de procedencia de más y no da acceso a cámara, micrófono ni ubicación. |
| **Dirección USDT verificada** | Comprobé su suma de control: es una dirección TRC20 válida y sin erratas. |

Probado con las mismas cabeceras que aplica Netlify: **0 conexiones externas y 0 errores de seguridad**.

> Si un día se añade algo externo (analítica, el CRM de Google, otro script), hay que **añadir ese dominio en `_headers`** o el navegador lo bloqueará. Se regenera con `python3 src/build_netlify.py`.

## Lo más importante: las cuentas
El riesgo real no está en el código, sino en que alguien entre en una cuenta y **cambie la dirección USDT o el PayPal**.

| Cuenta | Qué activar |
|---|---|
| **Email de Lera** (el de todas las cuentas) | Verificación en 2 pasos con una app (Google Authenticator) **o** llave/passkey. Contraseña única. |
| **Netlify** | 2FA: User settings → Security. Que solo Lera, y tú si hace falta, seáis miembros. |
| **Payhip** | 2FA (Account → Security). Revisar el email de cobros. |
| **PayPal** | 2FA (Seguridad → Verificación en 2 pasos). Activar avisos de cada cobro. |
| **Instagram / WhatsApp** | 2FA. En WhatsApp: «Verificación en dos pasos» con PIN. |
| **Wallet USDT** | La frase semilla (12/24 palabras) **solo en papel**, nunca en fotos, chats ni la nube. Nadie de soporte la pide nunca. |

Otras normas:
- Nunca enviar contraseñas por WhatsApp o email. Si hay que compartir acceso, invitar como miembro del equipo, no con la contraseña.
- No instalar extensiones raras en el navegador donde se gestionan las cuentas.

## Estafas típicas y cómo evitarlas
1. **Capturas de pago falsas (USDT):** antes de mandar el PDF, comprobar que el dinero **ha llegado de verdad** a la wallet o en tronscan.org con la dirección `TGj83GW2wcNR4JUwXmBhsCNbsQkGvvyFQX`. Nunca fiarse solo de una captura.
2. **«Envenenamiento de dirección»:** estafadores mandan céntimos desde una dirección **casi igual** para que se copie por error del historial. Copiar siempre la dirección de la web o del perfil, nunca del historial de transacciones.
3. **Webs clon:** alguien podría copiar la web con otra dirección USDT. Conviene que Lera tenga la web enlazada **solo** desde su Instagram oficial y diga en historias: «Solo pago en whynotleraa.netlify.app».
4. **Phishing:** emails falsos de «PayPal», «Payhip» o «Netlify» pidiendo iniciar sesión. Entrar siempre escribiendo la dirección a mano, nunca desde el enlace del email.

## Comisiones (texto legal ya en la web)
- La clienta paga **exactamente** el precio indicado. No se añaden recargos (en la UE está prohibido cobrar recargos por pagar con tarjeta o PayPal a consumidores).
- La comisión de PayPal y Payhip la asume la vendedora.
- Si la tarjeta de la clienta es de otra moneda, **PayPal o su banco** pueden cobrar su propia conversión: eso lo cobran ellos.
- En USDT, la comisión de la red la paga quien envía.
- Si Lera quiere ingresar 20 $ limpios, lo legal es **subir el precio** (por ejemplo 22 $), no añadir un recargo.
