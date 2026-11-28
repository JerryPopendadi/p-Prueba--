# THE FACES PARTNERS · Nueva campaña paso a paso

Archivos:
- `the-faces-partners-landing.html`: la página nueva.
- `TFP-PARTNERS-campana-v4.csv`: la campaña completa, sin precios.
- `negativas-v4.txt`: las palabras negativas.

Hazlo **desde el ordenador**: la app del móvil no permite subir archivos ni crear listas.

---

## Paso 1 · Crear la página (10 min)

1. WordPress → Páginas → Añadir nueva.
2. Título: `Spa Partnership in Bali | THE FACES PARTNERS`.
3. Enlace permanente (slug): `spa-partnership-bali`. Tiene que ser exactamente esto, porque los anuncios apuntan a https://thefacespeace.com/spa-partnership-bali/
4. Plantilla: **Elementor Canvas**. Así la página no muestra el menú del tema, y el visitante no se va a otras páginas.
5. Editar con Elementor → arrastra un widget **HTML** → pega todo el archivo `the-faces-partners-landing.html` → Publicar.
6. Limpia la caché, abre la página en el móvil y haz una prueba con tu email:
   - debe salir "Thank you!" con el botón para reservar la llamada;
   - debe llegar una fila al Excel, con Interest = `partnership_general` (o el nombre del proyecto, si pulsaste "Ask about this spa").

## Paso 2 · Subir la campaña (5 min)

1. Google Ads → Herramientas → **Acciones masivas → Cargas** → botón + → sube `TFP-PARTNERS-campana-v4.csv`.
2. Pulsa **Vista previa**. Si no hay errores, pulsa **Aplicar**.
3. Se crea la campaña **TFP | PARTNERS | SEARCH | EN**, **en pausa**, con:
   - presupuesto de 400.000 IDR al día (unos 22 €);
   - solo la red de Búsqueda de Google;
   - CPC manual de 45.000 IDR;
   - 4 grupos de anuncios con palabras clave de frase y exactas (nada de concordancia amplia);
   - 4 anuncios sin precios.

## Paso 3 · Ajustes que el archivo no puede hacer (10 min)

Abre la campaña nueva → **Configuración**:

1. **Redes:** quita "Socios de búsqueda" y "Red de Display", si aparecen marcadas.
2. **Ubicaciones:** pulsa "Introducir otra ubicación" y añade:
   - Indonesia, Singapur, Australia, Hong Kong, Emiratos Árabes Unidos;
   - Reino Unido, Alemania, Países Bajos, Suiza, Francia, Estados Unidos.
3. **Ubicaciones → Opciones de ubicación → Incluir:** elige **"Presencia: usuarios que están o suelen estar en las ubicaciones seleccionadas"**. Esto es muy importante: la opción por defecto ("Presencia o interés") muestra los anuncios a turistas de todo el mundo que solo buscan cosas sobre Bali.
4. **Idiomas:** inglés.
5. **Objetivos:** usa "Investor enquiry – Forminator 703" como conversión principal.
6. **Recomendaciones → Aplicación automática:** desactívala toda.

## Paso 4 · Palabras negativas (5 min)

1. Herramientas → Biblioteca compartida → **Listas de palabras clave negativas** → +.
2. Nombre: `TFP negativas`. Pega el contenido de `negativas-v4.txt`, una palabra por línea → Guardar.
3. Abre la lista → **Aplicar a campañas** → marca **TFP | PARTNERS | SEARCH | EN** y también las campañas antiguas que dejes activas.

## Paso 5 · Edad y extras (5 min)

1. Campaña nueva → **Audiencias → Datos demográficos → Edad** → excluye **18–24**.
2. **Recursos → +**, añade:
   - **Formulario para clientes potenciales:** ya tienes uno creado; añádelo a esta campaña.
   - **Enlaces de sitio** (sitelinks). Google pide que cada uno lleve a una página distinta:
     - "Our 4 spa projects" → https://thefacespeace.com/invest-in-a-spa-in-bali-3-projects-the-faces-invest/
     - "WATERFALL · Ubud" → https://thefacespeace.com/the-faces-invest-waterfall-bali/
     - "Book a call with founders" → https://thefacespeace.com/book-an-investor-meeting/
     - "THE FACES Ubud spa" → la página de Ubud que instalaste (the-faces-ubud-invest-v2)
   - **Texto destacado** (callouts):
     - Bali since 2013
     - Fully managed
     - Monthly reports
     - Registered shares

## Paso 6 · Activar y apagar lo viejo

1. **Pon en pausa** las campañas antiguas:
   - TFI 01 INVESTOR HOT;
   - TF INVEST UBUD;
   - TF INVEST WATERFALL;
   - cualquier Performance Max o campaña de Display.
2. **Elimina** la campaña "TFI | INVESTORS | SEARCH | EN" (la que subimos antes y está en pausa), porque sus anuncios tienen precios.
3. **Activa** TFP | PARTNERS | SEARCH | EN.

## Qué esperar

- **Días 1–3:** pocos clics, quizá 5–15 al día. Es lo correcto: ahora solo verán el anuncio personas que buscan un negocio.
- **Día 3:** mándame una captura de los **términos de búsqueda**. Añadimos más negativas si hace falta.
- **Semanas 1–2:** las primeras solicitudes reales.
- **Cuando haya unas 15 conversiones:** cambiamos la puja de CPC manual a "Maximizar conversiones".
- **Nunca actives:** concordancia amplia, Socios de búsqueda, Display ni las recomendaciones automáticas.
