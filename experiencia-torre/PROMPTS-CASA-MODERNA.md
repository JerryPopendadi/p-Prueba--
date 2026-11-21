# MALBO · Nueva experiencia: "Casa Horizonte" (villa moderna)

**Concepto:** una villa moderna y minimalista de dos plantas en una ladera con vistas al mar. Volumen inferior de hormigón blanco y travertino; volumen superior en voladizo, revestido de listones de roble; grandes cristaleras y piscina desbordante. Siempre al atardecer.

**Recorrido:** solar vacío → construcción → casa terminada → la cámara da la vuelta (fachada, aérea, piscina) → interiores → terraza final → plantas con explicación.

---

## 0 · Reglas para que todo sea coherente

1. **Crea primero K3 (la casa terminada)** en Gemini. Esa imagen es la "madre".
2. En la **misma conversación**, adjunta K3 para cada imagen siguiente y empieza el prompt con *"Same house as the attached image"*.
3. Mantén siempre **la misma hora (atardecer), la misma orientación del sol y los mismos materiales**.
4. Formato **16:9**, máxima resolución.

### Bloque de realismo (pégalo al final de cada imagen exterior)
```
Real architectural photograph, full-frame camera, 24mm tilt-shift lens, golden hour
sunset, warm low sun from the left, soft Mediterranean haze, true-to-life materials
(white board-formed concrete, pale travertine, natural oak, bronze-framed glass),
subtle imperfections, realistic scale and landscaping, editorial luxury real-estate
campaign, photorealistic, 16:9, no text, no logos, no watermark, not a 3D render,
not CGI, not illustration
```

### Bloque de interior
```
Real interior photograph, Architectural Digest style, warm sunset light through large
windows mixed with warm 2700K lamps, natural oak, pale travertine, white plaster,
linen and boucle textiles, realistic textures and imperfections, calm and uncluttered,
photorealistic, 16:9, no text, no people, not a 3D render, not CGI
```

---

## 1 · Exteriores e imágenes clave (Gemini · Nano Banana)

### K3 · La casa terminada (crear PRIMERO)
```
A modern minimalist two-storey luxury villa on a gentle hillside overlooking the
Mediterranean sea. Ground floor: a long low volume in white board-formed concrete and
pale travertine with floor-to-ceiling bronze-framed sliding glass walls. Upper floor:
a horizontal box clad in vertical natural oak slats, cantilevering 5 meters over the
entrance, with a deep framed window. Flat roofs with thin edges, a long infinity pool
running along the garden side, olive trees and native grasses, a gravel driveway,
warm lights just turning on inside. Front three-quarter view at eye level from the
driveway. [bloque de realismo]
```

### K1 · El solar vacío
```
Same location, same light and same sea view as the attached image, but BEFORE
construction: the house does not exist. An empty gently sloping plot of dry earth
with a few old olive trees, wild grasses, low stone boundary walls and survey stakes
with string marking the footprint. Camera at the same position and angle, eye level
from where the driveway will be. Quiet, expectant. [bloque de realismo]
```

### K2 · La construcción
```
Same location, light and camera angle as the attached images. The same villa under
construction: bare white concrete structure with floor slabs, columns and the
dramatic cantilever already cast, steel rebar on the roof edge, timber formwork,
no glass or cladding yet, the pool excavated but empty, a clean construction site,
no people, no cranes in frame. [bloque de realismo]
```

### K4 · Vista aérea (inicio de la vuelta)
```
Same house as the attached image. Aerial drone view from 40 meters at a three-quarter
angle showing the full composition: the oak-clad upper box cantilevering over the
concrete base, the long infinity pool, the garden with olive trees, the driveway,
and the sea and coastline behind at sunset. [bloque de realismo]
```

### K5 · Lado de la piscina (la vuelta continúa)
```
Same house as the attached image, now seen from the garden side at low eye level
across the infinity pool. Huge sliding glass walls fully open to the double-height
living room, warm interior glow, the pool edge disappearing into the sea view on
the right, teak loungers, olive tree, golden sunset reflected in the water.
[bloque de realismo]
```

---

## 2 · Interiores

### K6 · Entrada y escalera
```
Same house and materials as the attached images. The entrance hall: a sculptural
floating staircase in pale travertine treads with a slim bronze handrail rising along
a full-height board-formed concrete wall, an oak pivot front door, a long travertine
bench, a single ceramic vase with olive branches, a skylight washing light down the
wall. Eye-level camera, 24mm. [bloque de interior]
```

### K7 · Salón de doble altura
```
Same house and materials as the attached images. Double-height living room with a
6-meter glass wall fully open to the pool terrace and the sea at sunset. Low modular
ivory boucle sofa, travertine coffee table, a long linear fireplace in a board-formed
concrete wall, oak floor, a sculptural paper pendant light, a large abstract artwork.
Eye-level camera looking toward the sea. [bloque de interior]
```

### K8 · Cocina y comedor
```
Same house and materials as the attached images. Open kitchen and dining area: a
monolithic travertine island with brushed bronze tap, flush oak cabinetry up to the
ceiling, a solid oak dining table for eight with woven chairs, a linear pendant light,
sliding glass opening to an outdoor dining terrace with olive trees and sea view.
[bloque de interior]
```

### K9 · Dormitorio principal (planta alta, dentro del voladizo)
```
Same house and materials as the attached images. Master bedroom inside the cantilevered
oak volume: a low bed with linen bedding facing a frameless panoramic window that frames
the sea at sunset like a painting, oak slatted walls, travertine floor, a cream boucle
armchair, ceramic bedside lamps glowing warm. [bloque de interior]
```

### K10 · Baño principal
```
Same house and materials as the attached images. Master bathroom fully clad in pale
travertine, a freestanding carved stone bathtub in front of a tall window with the
sea view, double floating oak vanity with bronze taps, backlit mirror, walk-in shower
behind frameless glass, a skylight above. Spa-like and calm. [bloque de interior]
```

### K11 · Terraza superior (plano final)
```
Same house as the attached images. The rooftop terrace of the upper floor at blue hour
just after sunset: built-in travertine bench with linen cushions, a low fire bowl
glowing, potted olive tree, slim glass balustrade, the infinity pool and garden lit
below, the sea and coastline lights in the distance. Camera at standing eye level
looking toward the horizon. [bloque de realismo]
```

---

## 3 · Vídeos (Google Flow → Veo → "Frames to Video", 16:9)

Inicio = imagen de la izquierda · Fin = imagen de la derecha. Para que los tramos encajen perfectamente, usa como inicio de cada tramo **el último fotograma real** del vídeo anterior.

| # | Tramo | Prompt |
|---|---|---|
| V1 | K1 → K2 | `One continuous shot, slow dolly forward at eye level. The house begins to build itself from the ground: foundations, columns and concrete slabs rising and the cantilever extending out, like an elegant time-lapse. Golden hour, realistic, no people, no cuts.` |
| V2 | K2 → K3 | `One continuous shot. The construction completes in an elegant time-lapse: glass walls slide into place, oak cladding wraps the upper volume, the pool fills with water, the garden grows, interior lights turn on. Camera holds steady then slowly pushes in. No cuts.` |
| V3 | K3 → K4 | `One continuous drone shot. The camera rises smoothly from eye level and starts orbiting to the right around the villa, revealing the pool and the sea. Cinematic, stable, golden hour. No cuts.` |
| V4 | K4 → K5 | `The drone continues its orbit around the house and descends gently to the garden side, gliding low over the infinity pool toward the open glass walls. Smooth and continuous, no cuts.` |
| V5 | K5 → K7 | `The camera glides across the pool terrace and through the fully open glass wall into the double-height living room, settling at eye level. Seamless exterior-to-interior move, warm light. No cuts, no people.` |
| V6 | K7 → K8 | `Slow gimbal shot. The camera turns gently to the left from the living room and glides into the open kitchen and dining area. Calm, continuous, realistic. No cuts.` |
| V7 | K8 → K6 | `The camera moves from the kitchen into the entrance hall and slowly rises alongside the floating travertine staircase toward the upper floor. Smooth, continuous, no cuts.` |
| V8 | K6 → K9 | `From the top of the stairs the camera glides along a short oak corridor and enters the master bedroom, slowing in front of the panoramic window framing the sea. No cuts.` |
| V9 | K9 → K10 | `The camera turns gently and passes through an open pocket door into the travertine master bathroom, moving slowly toward the stone bathtub and the window. No cuts.` |
| V10 | K10 → K11 | `The camera exits to the rooftop terrace as day turns to blue hour; the fire bowl glows and the coastline lights appear. Final slow push toward the horizon. No cuts.` |

Consejos:
- Genera 2–4 variantes por tramo y quédate con la que **no deforme** la casa ni los muebles.
- Si va rápido, añade `very slow camera movement`.
- Descarga siempre en la máxima calidad.

---

## 4 · Plantas y explicación

Gemini puede dibujar los planos, pero suele inventarse las letras. Pídelos **sin texto**: yo añado los nombres y los metros en la web y los hago interactivos, como en la torre.

### P1 · Planta baja
```
Clean minimalist architectural floor plan, top-down orthographic view, thin black lines
on pure white background, wall thickness shown in solid black, furniture drawn as simple
outlines, subtle light grey hatching for terraces and pale blue for the pool. Ground
floor of a modern villa: entrance hall with straight staircase, double-height living
room opening to a long pool terrace, open kitchen with island and dining area, guest
bedroom or study with bathroom, guest WC, laundry, two-car garage, infinity pool 14 x 4 m
along the garden side. No text, no labels, no dimensions, no logos, high resolution.
```

### P2 · Planta alta
```
Same drawing style as the attached floor plan. Upper floor of the same villa: landing
from the staircase with a void overlooking the double-height living room, master suite
in the cantilevered volume with walk-in wardrobe and large bathroom with freestanding
tub, two further bedrooms each with its own bathroom, and a 60 m² rooftop terrace with
built-in bench and fire bowl. No text, no labels, no dimensions.
```

### P3 · Axonometría explicativa (opcional, muy visual)
```
Exploded axonometric architectural diagram of the same villa: roof, upper floor and
ground floor separated vertically with thin dashed guide lines, minimal white model
style with oak texture on the upper volume and pale stone on the ground floor, the pool
in soft blue, plain white background, soft shadows. No text, no labels.
```

### Explicación para la web (ES)
- **Parcela:** 1.200 m² en ladera, orientada al mar.
- **Superficie construida:** 380 m² en dos plantas + 60 m² de terraza superior.
- **Planta baja · 220 m²:** recibidor con escalera escultórica, salón de doble altura abierto a la piscina, cocina con isla y comedor, dormitorio de invitados o despacho con baño, aseo, lavadero y garaje para dos coches.
- **Planta alta · 160 m²:** suite principal en el voladizo con vestidor y baño, dos dormitorios con baño propio y acceso a la terraza superior.
- **Exterior:** piscina desbordante de 14 × 4 m, porche, comedor exterior y jardín mediterráneo con olivos.
- **Materiales:** hormigón visto, travertino, roble natural y carpintería de bronce.

---

## 5 · Capítulos de texto para la web (los traduzco a EN y RU)

| Escena | Título |
|---|---|
| Solar | **NADA,** *todavía.* |
| Construcción | **DE LA TIERRA,** *una forma.* |
| Casa terminada | **UNA CASA** *que mira al mar.* |
| Vuelta aérea | **HORIZONTE** *en cada ángulo.* |
| Piscina | **EL AGUA** *se funde con el mar.* |
| Salón | **DOBLE ALTURA,** *doble luz.* |
| Cocina | **EL CORAZÓN** *de la casa.* |
| Escalera | **PIEDRA** *que flota.* |
| Dormitorio | **DESPERTAR** *frente al mar.* |
| Baño | **PIEDRA,** *agua y luz.* |
| Terraza | **CUANDO CAE** *la noche.* |

---

## 6 · Qué me mandas y qué hago yo

**Tú me mandas:** las 11 imágenes clave, los 10 vídeos y las 2 o 3 plantas.

**Yo hago:**
- Monto el recorrido completo.
- Creo una web nueva con el mismo estilo: portada a pantalla completa, textos grandes y ES / EN / RU.
- Añado una sección de **plantas interactivas** (al tocar cada estancia ves su nombre y sus metros) y la **ficha técnica** con la explicación.
