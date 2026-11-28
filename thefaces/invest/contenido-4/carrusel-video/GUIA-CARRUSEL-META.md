# THE FACES PARTNERS · Carrusel de vídeo para Instagram y Facebook

Hay 6 tarjetas de vídeo en 4:5 (1080×1350), en inglés (`TFP-EN-…`) y en ruso (`TFP-RU-…`). Duran 8 s cada una (la última, 10 s) y no llevan sonido.

| # | Tarjeta | Vídeo de fondo | Mensaje |
|---|---|---|---|
| 1 | Gancho | Campo de arroz, Ubud | Sé copropietario del 49 % de un spa de lujo en Bali. Lo gestiona nuestro equipo. |
| 2 | THE FACES Ubud | Masaje con cuenco y ritual | Está en funcionamiento: visítalo como cliente antes de decidir |
| 3 | The White Temple | Ritual de espuma | En reforma, en Sanur: 5 salas rituales |
| 4 | WATERFALL | Arrozales y jungla | En construcción, en Ubud |
| 5 | THE FACES Sanur | Head spa junto a la piscina | Planos listos: buque insignia de 250 m² |
| 6 | Cómo funciona | Dron sobre Ubud | No es un fondo. Llamada → visita → documentos → notaría |

No he usado el vídeo de "antes y después" de la cara. Meta rechaza los anuncios con resultados de antes y después, y además no tiene nada que ver con buscar socios.

---

## Por qué está hecho así

Se basa en el estudio de mercado de `ESTRATEGIA-PARTNERS-MERCADO.md`:
- **El público tiene miedo a las estafas en Bali.** Por eso no hay cifras de rentabilidad ni "ingresos pasivos". Sí hay pruebas: un spa que funciona, una visita como cliente, documentos y notario.
- **Sin precios.** El anuncio de villas de tu captura pone "$710 000". Funciona para vender inmuebles, pero en vuestro caso trae curiosos y además choca con las reglas financieras de Meta. El importe se da en la llamada.
- **Las palabras que atraen a estafadores y a cazadores de dinero fácil no aparecen:** invest, ROI, passive income, guaranteed, profit, %/mes.
- **Atrae a la persona normal con capital.** Quiere ser dueña de algo bonito y real, pero no quiere gestionarlo. Por eso el mensaje es "Our team runs it every day. You receive a monthly report."
- **El logo sale pequeño, arriba a la izquierda, en blanco.** Se ve en todas las tarjetas, pero no tapa el vídeo.

---

## Textos para Meta Ads Manager

### Inglés

**Texto principal:**
> We have run spas in Bali since 2013. Now you can co-own 49% of one of our four spas in Ubud and Sanur.
>
> Our team builds, staffs and runs the spa every day. You receive a monthly report and vote on key decisions.
>
> Not a fund and not a villa: a real spa you can visit as a guest before you decide. Registered shares, signed at a notary.
>
> Book a private call with the founders, Anna and Evgenii.
>
> Information only, not a public offer. Capital at risk.

**Titular de cada tarjeta (debajo del vídeo):**
1. Co-own a spa in Bali
2. THE FACES Ubud · operating
3. The White Temple · Sanur
4. WATERFALL · Ubud
5. THE FACES Sanur · flagship
6. Talk to the founders

**Descripción:** Fully managed · Monthly reports

**Botón:** *Más información* (Learn more). No uses "Registrarte" ni "Comprar".

### Ruso

**Texto principal:**
> Мы управляем спа на Бали с 2013 года. Теперь вы можете стать совладельцем 49% одного из наших четырёх спа в Убуде и Сануре.
>
> Наша команда строит, набирает персонал и управляет спа каждый день. Вы получаете ежемесячный отчёт и голосуете по ключевым решениям.
>
> Не фонд и не вилла: настоящий спа, который можно посетить как гость, прежде чем принимать решение. Зарегистрированные доли, подписание у нотариуса.
>
> Запишитесь на личный звонок с основателями, Анной и Евгением.
>
> Только информация, не публичная оферта. Капитал под риском.

**Titulares de las tarjetas:**
1. Совладение спа на Бали
2. THE FACES Ubud · работает
3. The White Temple · Санур
4. WATERFALL · Убуд
5. THE FACES Sanur · флагман
6. Звонок с основателями

---

## Configuración paso a paso (Ads Manager, desde el ordenador)

1. **Campaña → Crear → objetivo "Clientes potenciales".**
2. **Categoría especial de anuncios:** si Meta pide "Productos y servicios financieros", márcala. Esa categoría limita la segmentación por edad y género, pero si no la marcas y Meta la exige, rechazará el anuncio.
3. **Ubicación de conversión:** Formulario instantáneo, de tipo **"Mayor intención"**.
   - Preguntas: nombre, email, teléfono; "You are" (Private partner / Hotel or property owner / Company); "When would you like to start?"; presupuesto.
   - Pantalla final: botón **"Book a call with the founders"** → https://calendar.app.google/b7nddp1H5fBoGYT98
   - Alternativa: enviar a la web https://thefacespeace.com/spa-partnership-bali/
4. **Público:**
   - países como en Google: Singapur, Australia, Hong Kong, EAU, Reino Unido, Alemania, Suiza, Países Bajos, Francia, Indonesia;
   - edad 35–65 si la categoría lo permite;
   - Advantage+ con sugerencias: business owners, hospitality, luxury travel, wellness.
   - El conjunto de anuncios en ruso va a los países donde vive el público ruso que tú conoces (EAU, Indonesia, Chipre, Georgia, Serbia, Turquía…), no a Rusia.
5. **Ubicaciones:** Advantage+, o manual: Instagram Feed + Facebook Feed. Las Stories recortan el 4:5.
6. **Anuncio → Formato "Secuencia" (Carrusel)** → sube los 6 vídeos **en orden** (01 → 06).
   - Desactiva "Mostrar automáticamente primero las tarjetas con mejor rendimiento": la historia tiene un orden.
   - Desactiva las "mejoras creativas automáticas" de Advantage+. Si no, Meta puede añadir música o textos que no hemos revisado.
7. **Presupuesto:** 15–20 € al día durante 14 días. No toques nada en los 5 primeros días.
8. **Píxel:** el píxel 1557758462849935 ya está en thefacesbali.com (plugin 1.7.0). Para thefacespeace.com te preparo la instalación si lo quieres.

## Qué se puede cambiar

- Los textos de cada tarjeta están en `slides.py`. Se regeneran con `python3 overlays.py`, `node render.js _ov/jobs.json` y `python3 build.py`.
- **Antes de publicar, confirma:**
  - que el 49 % se ofrece en los 4 spas;
  - que el vídeo del head spa junto a la piscina se puede usar para THE FACES Sanur. Si es de otro spa, lo cambio.
