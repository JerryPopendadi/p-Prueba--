# MALBO · Ampliación de interiores: dormitorio principal + baño en suite

El recorrido nuevo sigue después del salón: **salón → dormitorio principal → baño en suite**.

Archivo de partida: `ultimo-fotograma-salon.jpg` (el último fotograma del vídeo actual). Úsalo como **imagen de referencia** en Gemini y como **fotograma inicial** en Flow para que no se note el corte.

---

## 1. Imágenes (Gemini · Nano Banana)

Adjunta `ultimo-fotograma-salon.jpg` en la misma conversación en la que pidas cada imagen.

### K6 · Dormitorio principal
```
Same apartment as the attached image, same interior design language: warm light oak,
oak slatted wall panels, pale travertine, warm cove lighting in a recessed ceiling,
same golden hour light and same city skyline. Now show the master bedroom.
A low king-size bed with an upholstered headboard in light boucle fabric set against a
full-height oak slatted wall, crisp white and sand-colored linen bedding with a soft
throw, two floating walnut bedside tables with small sculptural ceramic lamps glowing
warm, a wool rug, a lounge chair in cream boucle by the window, floor-to-ceiling glass
with sheer linen curtains gently open to the city at sunset, a glimpse of the balcony.
Calm, serene, uncluttered. Eye-level camera at 1.4 m, 24mm lens, centered composition
from the foot of the bed.
Real interior photograph, Architectural Digest style, natural sunset light mixed with
warm 2700K lamps, realistic textures and imperfections, photorealistic, 16:9,
no text, no people, not a 3D render, not CGI.
```

### K7 · Baño en suite
```
Same apartment and same design language as the attached images. Now show the en-suite
master bathroom. Floor-to-ceiling pale travertine walls and floor, a freestanding
sculptural stone bathtub placed in front of a large window with the city at sunset,
a long floating oak vanity with a travertine countertop and two brushed brass faucets,
a wide frameless mirror with soft backlighting, a walk-in shower behind a frameless
glass panel with a brass rain shower head, warm linear light in a recessed ceiling
niche, folded linen towels, a small branch in a ceramic vase. Spa-like, calm, minimal.
Eye-level camera at 1.4 m, 24mm lens, symmetrical composition looking toward the bathtub
and the window.
Real interior photograph, Architectural Digest style, warm sunset light, realistic
reflections on stone and brass, photorealistic, 16:9, no text, no people,
not a 3D render, not CGI.
```

Si la imagen sale "demasiado perfecta", añade: `subtle real-life imperfections, slight lens vignetting, natural shadows`.

Mándame K6 y K7 antes de pasar al vídeo y compruebo que encajan con el salón.

---

## 2. Vídeos (Google Flow → Veo → Frames to Video, 16:9)

### Tramo E · Salón → dormitorio
- **Inicio:** `ultimo-fotograma-salon.jpg`
- **Fin:** K6
```
One continuous, slow, stabilized gimbal shot inside the apartment. The camera turns
gently to the left, past the oak slatted wall and the shelving, glides through a wide
open oak doorway along a short softly lit corridor, and enters the master bedroom,
settling at the foot of the bed facing the window. Warm sunset light, lamps glowing.
Realistic, smooth, no cuts, no people, no text.
```

### Tramo F · Dormitorio → baño
- **Inicio:** el **último fotograma real** del tramo E (no K6), para que la unión sea perfecta
- **Fin:** K7
```
One continuous, slow gimbal shot. From the foot of the bed the camera turns gently to
the right and glides through an open pocket door into the travertine en-suite bathroom,
slowly moving forward toward the freestanding bathtub in front of the window with the
city at sunset. Soft reflections on stone and brass. Realistic, smooth, no cuts,
no people, no text.
```

### (Opcional) Tramo G · Plano final
- **Inicio:** último fotograma del tramo F
```
The camera slowly pushes toward the window above the bathtub and the view opens to the
city at dusk as lights come on. Calm final shot. Realistic, smooth, no cuts.
```

Consejos:
- Genera 2–4 variantes por tramo y quédate con la que **no deforme los muebles**.
- Si la cámara va demasiado rápida, añade `very slow camera movement`.
- Descarga en la máxima calidad y mándamelos (aquí o en GitHub `experiencia-torre/clips/`).

---

## 3. Lo que hago yo después

- Uno E y F (y G, si lo haces) detrás del salón con fundidos cortos.
- Añado dos capítulos de texto:
  - **06 / El descanso:** "DORMIR *sobre la ciudad.*" — Lino, roble y la ciudad apagándose al otro lado del cristal.
  - **07 / El baño:** "PIEDRA, *agua y luz.*" — Travertino de suelo a techo y una bañera frente al atardecer.
- Reparto el scroll para que cada estancia tenga su tiempo y actualizo el enlace del móvil.
