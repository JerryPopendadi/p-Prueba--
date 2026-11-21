# MALBO Innovation · Vídeo para la web inmersiva con Gemini Pro y ChatGPT Pro

El objetivo es **un único recorrido de cámara realista**: solar vacío → la torre se levanta → vista aérea al atardecer → terraza → salón. Ese vídeo se trocea en imágenes y la web lo mueve con el scroll.

**Reparto recomendado**
- **Imágenes clave:** Gemini (Nano Banana). Es el mejor para mantener *el mismo edificio* entre imágenes ("la misma torre, ahora…"). ChatGPT es la alternativa o te sirve para comparar.
- **Vídeo:** **Google Flow** (labs.google/flow, entra con tu cuenta de Gemini Pro) con Veo, en el modo **Frames to Video**: subes la imagen de inicio y la de fin, y Veo crea el movimiento entre las dos. Sora (ChatGPT Pro) sirve para probar alternativas o para tramos que solo necesitan imagen de inicio.

> Las apps cambian a menudo de nombre y de menús. Si algo no coincide, busca la opción "imagen a vídeo" o "fotograma inicial / final".

---

## 0. Reglas para que parezca REAL (no render)

Añade siempre este bloque al final de cada prompt de imagen:

```
Real architectural photograph, shot on a full-frame camera with a 24mm tilt-shift lens,
golden hour sunset, warm low sun, soft atmospheric haze, natural reflections in the glass,
true-to-life materials (concrete, stone, glass, oak), subtle imperfections, realistic scale,
editorial real-estate campaign, photorealistic, 16:9, no text, no logos, no watermark,
not a 3D render, not CGI, not illustration
```

Trucos:
- Escribe como si describieras **una foto**: cámara, objetivo, hora del día, materiales.
- Evita las palabras *render, 3D, CGI, futuristic*: empujan al aspecto falso.
- Pide siempre **16:9** y la mayor resolución posible.
- Mantén siempre **la misma hora (atardecer)** y **el mismo lado de la luz**.

---

## 1. Imágenes clave (Gemini → Nano Banana)

**Orden:** crea primero **K3 (la torre terminada)**. Después, en la misma conversación, adjúntala y pide las demás diciendo "la misma torre". Así el edificio no cambia.

### K3 · La torre terminada (la imagen madre)
```
A tall modern minimalist residential tower of 32 floors in a contemporary city.
Dark tinted glass facade, thin pale limestone floor slabs that project 3 meters as
continuous deep balconies on every floor, slim frameless glass railings, a pale stone
vertical spine that zigzags up the full height of the main facade. Warm interior lights
just starting to glow in some apartments. Surrounding mid-rise buildings, wide avenue,
distant skyline. Aerial three-quarter view from a drone at 80 meters.
[bloque de realismo]
```

### K1 · El solar vacío
Adjunta K3 y escribe:
```
Same location and same light as the attached image, but BEFORE construction: the tower
does not exist yet. An empty flat concrete construction lot with subtle tire marks,
a few young trees at the edges, the same surrounding buildings and avenue. Camera at
street level, 1.6 m high, looking at the center of the empty lot. Calm, quiet.
[bloque de realismo]
```

### K2 · Estructura a media altura
```
Same location and light as the attached image. The same tower under construction:
only the first 12 floors exist as bare pale concrete slabs and slim columns, no glass yet,
clean site, no cranes in frame. Camera slightly above street level, same angle as the
empty-lot image. [bloque de realismo]
```

### K4 · La terraza
```
Close-up of one deep balcony near the top floors of the attached tower, seen from a drone
hovering 8 meters in front of it. Pale limestone floor and ceiling, slim glass railing,
floor-to-ceiling sliding glass doors fully open, a warm minimalist living room visible
inside, sunset city reflected in the glass. [bloque de realismo]
```

### K5 · El salón
```
Interior of the apartment behind that balcony. Luxury minimalist living room: warm oak
slatted wall, built-in walnut shelving with a few books and ceramics, low white linen
sofa, dark walnut coffee table, wool rug, brass floor lamp, oak kitchen island in the
background, soft warm cove lighting, floor-to-ceiling window with the city at dusk.
Eye-level camera at 1.5 m, 24mm lens. [bloque de interior]
```
`[bloque de interior]`: `Real interior photograph, Architectural Digest style, natural light mixed with warm 2700K lamps, realistic textures, photorealistic, 16:9, no text, not a 3D render.`

✅ **Envíame las 5 imágenes aquí en el chat** y las reviso: coherencia del edificio, luz, encuadre. Te digo cuáles repetir.

---

## 2. Vídeos (Google Flow → Veo → "Frames to Video")

1. Entra en **labs.google/flow** y crea un proyecto nuevo.
2. Elige **Frames to Video**, formato **16:9** y la mejor calidad disponible.
3. Sube la imagen de **inicio** y la de **fin** de cada tramo y pega el prompt.
4. Genera 2–4 variantes y quédate con la más fluida.
5. **Descarga en la máxima resolución** (MP4).

| Tramo | Inicio → Fin | Prompt |
|---|---|---|
| A | K1 → K2 | `One continuous shot. The camera slowly dollies forward at street level while the building rises from the ground, concrete floor slabs stacking up one after another. Smooth, steady, realistic, golden hour. No cuts, no people, no text.` |
| B | K2 → K3 | `One continuous drone shot. The tower keeps rising to its full height while the camera ascends and orbits around it. The glass facade and balconies appear floor by floor. Smooth cinematic motion, realistic sunset light. No cuts.` |
| C | K3 → K4 | `One continuous drone shot flying smoothly toward the upper floors, slowing down and stopping in front of one deep balcony. Stable, cinematic, no shake, no cuts.` |
| D | K4 → K5 | `The camera glides gently through the open glass doors into the living room and settles at eye level. Seamless, continuous move from exterior to interior. Warm light, realistic. No cuts.` |

**Para que los tramos encajen perfectamente:** del vídeo A descarga el **último fotograma** (o haz una captura de pantalla al final) y úsalo como **inicio** del tramo B. Haz lo mismo en cada unión.

**Alternativa con Sora (ChatGPT Pro):** sube la imagen de inicio, pega el mismo prompt y añade "ending on a view similar to [describe K siguiente]". Sora no siempre respeta un fotograma final exacto, así que úsalo como plan B.

Ajustes en Veo: **sin audio**, o con audio que luego quitamos. Si te deja elegir duración, 8 s por tramo.

---

## 3. Pásame los vídeos

Tienes dos opciones:

- **A) GitHub (recomendada para vídeos):** en github.com abre el repositorio → rama `claude/bold-maxwell-012wzy` → carpeta `experiencia-torre` → **Add file → Upload files** → crea la carpeta `clips/` y sube `A.mp4`, `B.mp4`, `C.mp4` y `D.mp4`. La web de GitHub admite hasta 25 MB por archivo.
- **B) Aquí en el chat**, si la app te deja adjuntar vídeos.

Cuando estén, yo:
1. Uno los 4 tramos, igualo el color y quito el audio.
2. Saco unos 240 frames WebP optimizados.
3. Los conecto a la web y ajusto cuándo aparece cada texto.
4. Hago una versión ligera para móvil.
5. Lo subo todo al repositorio.

---

## 4. (Opcional) Pieza para Instagram, como el reel

Graba la pantalla del portátil mientras haces scroll en la web, con la mano en el trackpad, igual que el vídeo de referencia. Texto superior sugerido:

> **¿Y si pudieras entrar en una web?**
> Pie: *No es solo una web. Es una experiencia. — MALBO Innovation*
