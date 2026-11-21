# Cómo dejarlo todo a nombre de Lera (y que tú no tengas problemas)

**Idea clave:** domdiseno.com solo **presta el espacio**.
- Lera es la **titular de la web**, la **vendedora** y la **responsable de los datos**.
- El dinero **nunca pasa por ti**.
- Todo esto queda escrito en 3 sitios: su página legal, el pie de su web y un acuerdo firmado entre los dos.

> No soy abogado: es una plantilla razonable. Si puedes, que un asesor le dé un vistazo, sobre todo al acuerdo.

## Los 3 documentos
| Archivo | Para qué | Dónde va |
|---|---|---|
| `legal-wordpress.html` | Aviso legal + Política de privacidad + Condiciones de venta + Cookies de **Lera** (inglés, ruso y español; se elige el idioma del dispositivo) | Página de WordPress `domdiseno.com/lera-legal` |
| `acuerdo-alojamiento.pdf` | Contrato entre tú y Lera: cesión gratuita, ella responsable de todo, tú solo alojamiento, indemnidad, retirada de contenidos | Firmado por los dos. Cada uno guarda una copia |
| `index-wordpress.html` (actualizado) | Su web, con el pie «Sitio de Lera · domdiseno solo aloja» y enlace a la página legal | Página `domdiseno.com/lera` |

## Paso a paso
1. **Rellenar los datos de Lera** (campos amarillos `[[…]]`) en `legal-wordpress.html`:
   - nombre completo como en el pasaporte;
   - ciudad o dirección en Bali;
   - email;
   - fecha.
2. **En el acuerdo**, rellenar tus datos (nombre, NIF, dirección, ciudad y proveedor de hosting) y los de Lera (nombre y n.º de pasaporte).
3. **Firmar el acuerdo**: imprimir y firmar, o firmar el PDF electrónicamente. Lera te lo devuelve firmado por email o WhatsApp. **Guárdalo.**
4. **WordPress:**
   - Página «Lera — legal», enlace `lera-legal`, plantilla en blanco, bloque HTML personalizado → pegar `legal-wordpress.html`.
   - Página «Lera», enlace `lera` → pegar el nuevo `index-wordpress.html`.
   - En los **Ajustes SEO** (Yoast o Rank Math) de la página legal: «no indexar».
5. **Cuentas siempre a nombre de Lera**:
   - Payhip, con su email y como «Store name» su nombre;
   - su PayPal;
   - su wallet USDT.
   - Tú **no** creas ninguna cuenta de cobro ni pones tus datos en Payhip.
6. En **Payhip → Settings**, pon como política de privacidad y términos el enlace `https://domdiseno.com/lera-legal/`.
7. En **tu propia política de privacidad** (la de domdiseno.com), añade este párrafo:
   > «domdiseno.com aloja de forma gratuita páginas de terceros (por ejemplo, domdiseno.com/lera). Sus titulares son los únicos responsables de sus contenidos, ventas y del tratamiento de los datos de sus usuarios; domdiseno.com actúa solo como prestador de alojamiento.»
8. **No pongas tu analítica ni tus píxeles** (Google Analytics, Meta Pixel…) en las páginas de Lera. Si tu web tiene banner de cookies global, asegúrate de que también aparece ahí o excluye esas páginas del seguimiento.
9. **Si te llega una queja o un requerimiento** sobre los contenidos de Lera: reenvíaselo a ella. Si es ilegal o lo pide una autoridad, despublica la página (el acuerdo te lo permite).

## Tu WhatsApp
- La web de Lera **oculta automáticamente** el botón o chat de WhatsApp de tu WordPress (plugins como Joinchat, Click to Chat, WP Social Chat, QL WhatsApp, Chaty y otros).
- En su página solo se ve el botón verde con **el número de Lera** (+62 877-2343-4348).
- Si aun así aparece el tuyo, entra en los ajustes del plugin → «Visibilidad / Mostrar en» → **excluir** las páginas `lera` y `lera-legal`.
- Lo mismo con la cabecera y el pie de tu tema: usa plantilla **en blanco o Canvas** para que no salgan tus datos de contacto.

## Por qué así estás cubierto
- **Ley española (LSSI art. 16):** quien solo aloja no responde de los contenidos de otro mientras no sepa que son ilícitos y actúe al saberlo. Por eso el acuerdo dice que puedes retirarlos.
- **RGPD:** Lera es la responsable de los datos. Tú solo eres encargado de los registros técnicos del servidor, y eso queda firmado (art. 28).
- **Dinero e impuestos:** no cobras nada ni recibes pagos. No hay venta tuya ni ingreso que declarar.
- **Derechos de imagen y fotos:** Lera garantiza en el acuerdo que son suyos.
- **Indemnidad:** si alguien reclama por algo de Lera, ella responde y te cubre.
