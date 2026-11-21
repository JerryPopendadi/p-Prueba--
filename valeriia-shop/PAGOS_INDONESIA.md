# Pagos de los PDF — cuenta de Lera en Indonesia (PayPal + USDT)

**Resumen:** los 2 PDF (20 $ cada uno, 34 $ los dos) se venden con **Payhip conectado al PayPal de Lera**.
- La clienta paga con su cuenta PayPal **o con tarjeta** (PayPal permite pagar con tarjeta sin cuenta en la mayoría de países).
- Payhip envía el PDF **automáticamente** y pone el email de la compradora en cada página.
- **USDT** es una segunda opción **manual**: la clienta envía el pago y escribe a Lera, y Lera le manda el PDF.
- **Stripe no** se usa: no acepta cuentas de Indonesia.

```
Clienta → botón «Comprar 20 $» → ventana de Payhip → PayPal (cuenta o tarjeta) → descarga inmediata + email
Clienta → botón «Pagar USDT» → dirección + QR → envía USDT → WhatsApp a Lera → Lera le manda el PDF
```

---

## 1. PayPal de Lera (10 min)
1. Entrar en paypal.com con la cuenta de Lera.
2. Recomendado: pasar a **cuenta Business** (Configuración → «Actualizar a cuenta business»). Es gratis y se ve más profesional (el nombre aparece en el recibo).
3. Comprobar que está **verificada**: identidad (KTP/pasaporte) y **cuenta bancaria indonesia** vinculada, para poder retirar en IDR.
4. Comisiones aproximadas por venta internacional de 20 $: ~4,4 % + tarifa fija, más la conversión al retirar. Lo exacto está en «Tarifas» de PayPal Indonesia.

## 2. Payhip (15 min) — tienda y entrega automática
1. Ir a **payhip.com → Sign up**, con el email de Lera.
2. **Settings → Payment gateways → PayPal → Connect** e iniciar sesión con el PayPal de Lera.
   No conectar Stripe.
3. **Add product → Digital product**, tres veces:

   | Producto | Precio | Archivos que se suben |
   |---|---|---|
   | 21-Day Recipe Book / Книга рецептов | 20 $ | `recipes_en.pdf`, `recipes_ru.pdf`, `recipes_bi.pdf` |
   | Flat Belly 30 Days / Плоский живот | 20 $ | `belly_en.pdf`, `belly_ru.pdf` |
   | Bundle (los dos) | 34 $ | **Add product → Bundle** y elegir los 2 anteriores |

   Los PDF están en la carpeta `valeria/1_PDF`.
4. En cada producto activar:
   - **PDF Stamping**: imprime el email de la compradora en cada página y frena que se comparta.
   - **Limit downloads**: 5.
5. Copiar el **código** de cada producto. En el enlace `https://payhip.com/b/AbC1`, el código es `AbC1`.
6. Plan **Free** de Payhip: 5 % por venta. Payhip además cobra y declara solo el IVA de clientes de la UE y del Reino Unido.

## 3. USDT (5 min)
1. Pedir a Lera su dirección **USDT** y confirmar **la red**:
   - empieza por **T** y tiene 34 caracteres → **TRC20 (Tron)**, la recomendada (comisión baja);
   - empieza por **0x** → ERC20 o BEP20. En ese caso cambiar el texto `network` en la configuración, porque si la clienta envía por otra red el dinero se puede perder.
2. Cuando llega un pago:
   - Lera lo comprueba en su wallet o en tronscan.org con la dirección;
   - responde por email con los PDF;
   - opcional: lo apunta en su panel (Деньги → «＋ вручную»).
3. Plantilla de respuesta para Lera:
   > Hi! Payment received, thank you 🌿 Here are your guides (RU + EN). Enjoy! — Lera

## 4. Poner los datos en la web (2 min)
Abrir `index.html` y, al principio, en `CONFIG`:
```js
payhip: { recipes: 'CÓDIGO1', belly: 'CÓDIGO2', bundle: 'CÓDIGO3' },
crypto: { network: 'USDT · TRC20 (Tron)', address: 'T…dirección de Lera…' },
whatsapp: '62…número de Lera sin + ni espacios…',
supportEmail: 'email de Lera',
```
O pásame los datos (email de PayPal, dirección USDT y WhatsApp) y lo dejo hecho yo. **Nunca contraseñas.**

## 5. Subir a WordPress
1. Medios → subir `img/` y `video/hero.mp4`.
2. En `index.html` cambiar `src="img/` y `src="video/` por la ruta de los medios.
3. Página en blanco o «Elementor Canvas» → bloque **HTML personalizado** → pegar `index.html`.
4. Ajustes → Lectura → página de inicio.

## 6. Probar antes de publicar
1. En Payhip: **Coupons → crear uno del 100 %** → comprar tu propio producto con él → debe llegar el email con los PDF y su sello.
2. Hacer una compra real de un producto de prueba a 1 $ con otra cuenta de PayPal y devolverla desde PayPal.
3. Pulsar «Pagar USDT» → debe salir la dirección correcta, el QR y el botón de WhatsApp con el mensaje ya escrito.

---

### Entrenamientos
En la web **no hay precios**: solo «es posible entrenar con Lera online (1:1, grupos, nutrición)» y un formulario.
- Sin el CRM instalado, la solicitud se abre como mensaje de WhatsApp a Lera.
- Con el CRM (`valeria/3_Apps_y_CRM`), queda en su tabla y en su app.

### Impuestos
Payhip se ocupa del IVA de la UE y el Reino Unido. Los ingresos en Indonesia los declara Lera. Conviene preguntarle a un consultor local qué régimen le corresponde.
