# Cómo hacer una web en la que "entras" en un edificio

La web del reel no es un vídeo que se reproduce solo: es **un vídeo que avanza y retrocede con el scroll**. Por encima lleva textos que aparecen por capítulos y un HUD con aire de cámara de cine (esquinas, timecode, índice). El truco se reduce a tres piezas:

1. **Un recorrido de cámara continuo** (solar → torre que crece → fachada → terraza → interior), generado con IA de imagen y de vídeo.
2. **El vídeo troceado en imágenes** (unas 150–300 WebP) que se pintan en un `<canvas>` según el scroll.
3. **Una capa de diseño**: títulos grandes en mayúsculas con una palabra en serif cursiva, HUD en tipografía mono, grano y viñeta.

En esta carpeta tienes todo hecho:

| Archivo | Qué es |
|---|---|
| `index.html` | La web completa. **Sin vídeo** muestra una torre 3D procedural (Three.js) que se construye y en la que entras al hacer scroll. **Con vídeo** usa tus frames. |
| `extraer-frames.sh` | Convierte tu vídeo en la carpeta `frames/`. |
| `GUIA.md` | Esta guía. |

---

## Paso 1 — Storyboard (5 planos)

Escribe el recorrido como una sola toma de cámara. Cada plano es un capítulo de texto:

| # | Plano | Texto en pantalla |
|---|---|---|
| 1 | Solar vacío al atardecer, cámara a ras de suelo | NADA, *todavía.* |
| 2 | La torre se levanta planta a planta, la cámara sube | DE LA NADA, *una forma.* |
| 3 | Vista aérea dorada: una espina clara recorre la fachada | UNA COSTURA *de luz.* |
| 4 | La cámara se acerca a una terraza profunda | UNA SALA *al aire libre.* |
| 5 | La cámara cruza el ventanal y entra en el salón | LA CIUDAD, *en silencio.* |
| — | Final con botones | VÉALO *en persona.* |

> Clave: **cada plano empieza exactamente donde termina el anterior.** Por eso primero se generan las imágenes "fotograma clave" y luego los vídeos que las unen.

---

## Paso 2 — Genera los fotogramas clave (imagen IA)

Herramientas: Midjourney v7, Flux 1.1 Pro / Kontext, Nano Banana (Gemini), GPT-Image o Ideogram. Formato **16:9**, máxima resolución.

**Consistencia:** genera primero la imagen 3 (la torre terminada) y úsala como *referencia de imagen / style reference* en todas las demás, para que el edificio sea siempre el mismo. En Midjourney: `--sref` + `--cref`/omni-reference. En Flux Kontext o Nano Banana: sube la imagen y pide "la misma torre, ahora …".

**Bloque de estilo común** (pégalo al final de cada prompt):

```
architectural visualization, photorealistic, golden hour sunset, warm hazy light, 
35mm cinematic, subtle film grain, high-end real estate campaign, ultra detailed, 16:9
```

**Prompts:**

**K1 — Solar vacío**
```
Empty urban construction lot at sunset in a modern city, flat concrete ground, 
a few palm trees and low buildings around, distant office towers, camera at ground 
level looking at the center of the lot, nothing built yet, calm and quiet, 
[bloque de estilo]
```

**K2 — Estructura en construcción** (opcional, ayuda a la transición)
```
The same lot, a minimalist residential tower under construction: white concrete 
floor slabs and thin columns, first 6 floors, no facade yet, cranes absent, 
clean and architectural, same camera angle slightly higher, [bloque de estilo]
```

**K3 — Torre terminada (la imagen de referencia)**
```
A tall modern minimalist residential tower, 32 floors, dark tinted glass facade, 
thin pale stone floor slabs projecting as continuous deep balconies on every floor, 
a pale stone vertical spine zigzagging up the full height of the main facade, 
slim glass railings, warm interior lights starting to glow, surrounded by a modern 
city skyline, aerial three-quarter view from a drone, [bloque de estilo]
```

**K4 — La terraza**
```
Close-up of one balcony/loggia of the same tower near the top floors, deep sheltered 
outdoor room with pale stone floor and ceiling, floor-to-ceiling sliding glass doors 
open, warm living room visible inside, city at sunset reflected in the glass, 
camera hovering in front of the balcony, [bloque de estilo]
```

**K5 — El interior**
```
Interior of a luxury minimalist apartment living room inside the tower, warm wood 
slatted wall, built-in wooden shelving with books, low white linen sofa, dark walnut 
coffee table, rug, floor lamp, kitchen island in oak, soft warm cove lighting, 
floor-to-ceiling window with city view at dusk, eye-level camera, calm and serene, 
[bloque de estilo]
```

---

## Paso 3 — Une los planos con vídeo IA (primer y último fotograma)

Herramientas que aceptan **start frame + end frame**: Kling 2.x, Runway Gen-4 / Aleph, Google Veo 3, Luma Ray 2, Hailuo/MiniMax, Higgsfield. Duración: 5–10 s por tramo, 1080p, **sin audio**.

| Tramo | Inicio → Fin | Prompt de movimiento |
|---|---|---|
| A | K1 → K2 | `Slow cinematic dolly forward. The building rises from the ground floor by floor, slabs stacking up one after another. Smooth, continuous, no cuts.` |
| B | K2 → K3 | `The tower keeps growing to its full height while the camera rises and orbits around it like a drone. Glass facade appears, warm sunset light. One continuous shot.` |
| C | K3 → K4 | `Drone flies smoothly toward the upper floors and slows down in front of one deep balcony. Stable, cinematic, no shake.` |
| D | K4 → K5 | `The camera glides through the open glass doors into the living room and settles at eye level. Seamless transition from exterior to interior.` |

Consejos:
- Si el resultado "salta", genera varias versiones y quédate con la más fluida.
- Pide siempre *"one continuous shot, no cuts, smooth camera"*.
- Puedes usar el **último fotograma real** del tramo anterior como inicio del siguiente (expórtalo como imagen). Así la unión es perfecta.

---

## Paso 4 — Monta y exporta un solo vídeo

En CapCut, DaVinci Resolve o Premiere: une A+B+C+D, recorta pausas, iguala el color (cálido) y exporta:

- 1920×1080, 24–30 fps, **sin audio**, de 15 a 25 s en total.
- Para móvil, opcional: una segunda versión vertical 1080×1920.

---

## Paso 5 — Convierte el vídeo en frames

Necesitas `ffmpeg` (`brew install ffmpeg` en Mac, `winget install ffmpeg` en Windows).

```bash
cd experiencia-torre
chmod +x extraer-frames.sh
./extraer-frames.sh mi-recorrido.mp4 12 1920
# ✓ 240 frames en ./frames
```

Con 12 fps × 20 s salen unos 240 frames de 100–200 KB cada uno. Si pesa demasiado, baja a 10 fps o a 1280 px de ancho.

---

## Paso 6 — Conecta los frames a la web

Abre `index.html` y en `CONFIG` pon el número de frames:

```js
frames: { count: 240, path: i => `frames/frame_${String(i + 1).padStart(4, '0')}.webp` }
```

O sin tocar código: `index.html?frames=240`.

Después ajusta los textos y los momentos en que aparece cada capítulo (`data-in` / `data-out`, de 0 a 1) para que coincidan con tu vídeo. La duración total se controla con la altura de `#scrolly` (`900vh`): más alto = más lento.

---

## Paso 7 — Pruébala en local

Las imágenes y los módulos no cargan con `file://`, así que necesitas un servidor:

```bash
cd experiencia-torre
python3 -m http.server 8000
# abre http://localhost:8000
```

---

## Paso 8 — Publícala

Arrastra la carpeta a **Netlify Drop** (app.netlify.com/drop), o usa Vercel, Cloudflare Pages o GitHub Pages. Es estática: no necesita servidor.

---

## Cómo funciona el código (resumen)

```
scroll ──► progreso 0…1 (con inercia: prog += (target - prog) * 0.08)
            ├─► frame = round(progreso × (nFrames - 1)) ──► drawImage en <canvas> (cover)
            ├─► capítulos: opacidad / desenfoque / desplazamiento según data-in/out
            └─► HUD: timecode, índice activo, anillo de progreso
```

- **Canvas en vez de `<video>`**: hacer *seek* en un vídeo a cada scroll va a tirones. Con imágenes ya decodificadas el avance es instantáneo y funciona igual hacia atrás.
- **Precarga**: se cargan 12 frames, se muestra la web y el resto se carga por lotes. Si un frame aún no está, se pinta el más cercano.
- **Modo 3D** (sin vídeo): la misma barra de progreso mueve una cámara por una curva Catmull-Rom, levanta las 32 plantas una a una, dibuja la "costura", enciende las ventanas y entra en un salón modelado.

---

## Prompt para pedírselo a una IA de código (Claude, Cursor, v0, Lovable…)

```
Crea una landing page de una torre residencial de lujo en un solo index.html.

EXPERIENCIA
- Un <canvas> fijo a pantalla completa que muestra una secuencia de imágenes
  (frames/frame_0001.webp … frame_0240.webp) controlada por el scroll: un espaciador
  de 900vh define la duración; progreso 0–1 con inercia (lerp 0.08); el frame se pinta
  con drawImage simulando object-fit: cover; precarga progresiva con loader.
- 5 capítulos de texto abajo a la izquierda que aparecen/desaparecen según el progreso
  (fundido + desenfoque + desplazamiento vertical): título enorme en mayúsculas
  (sans grotesca ancha, peso 800) con una parte en serif cursiva dorada, kicker en mono
  "— 01 / La parcela" y un párrafo corto.
- HUD estilo cámara: esquinas en L, "MARCA / CIUDAD" arriba a la izquierda, timecode
  "TC 00:00:SS:FF" abajo a la izquierda ligado al progreso, índice de capítulos a la
  derecha con el activo resaltado, anillo SVG de progreso con la palabra SCROLL.
- Cabecera: logo, navegación numerada en mono (01 Proyecto, 02 Arquitectura,
  03 Residencias, 04 Ubicación) y botón píldora dorado "Agendar visita".
- Grano animado y viñeta encima del canvas.
- Tras la experiencia: sección de cifras con contadores (48 residencias, 32 plantas,
  entrega 2028, 115 m), marquesina infinita "RESIDENCIAS ✦ ARQUITECTURA ✦ …" y
  formulario de visita.

ESTILO: oscuro (#0c0c0e), texto marfil (#f4efe8), acento dorado (#f2c27b),
fuentes Archivo, Instrument Serif y JetBrains Mono. Minimalista, editorial, cinematográfico.
Responsive (en móvil se oculta el índice), respeta prefers-reduced-motion.
Sin frameworks; JavaScript vanilla.
```

Si quieres la versión 3D en lugar de vídeo, añade:

```
Si no hay frames, renderiza con Three.js una torre minimalista de 32 plantas (forjados
de piedra clara con terrazas de 3 m, vidrio oscuro reflectante con ventanas cálidas,
una espina blanca en zigzag en la fachada) en una ciudad de bloques al atardecer, con
cielo por shader y sombras. Con el scroll, las plantas se levantan una a una, la
cámara orbita como un dron por una curva Catmull-Rom y termina entrando por una
terraza a un salón con pared de listones de madera, sofá blanco y luz cálida.
```
