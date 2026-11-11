# -*- coding: utf-8 -*-
"""Contenido de las guías técnicas de SeñalVal.

Cada referencia normativa cita la norma por su nombre oficial. Los plazos y duraciones se presentan
como orientativos y así se indica en el texto. Revisar la versión vigente de cada norma antes de
cada reedición.
"""
U = 'https://senalval.es/wp-content/uploads/'

GUIAS = [
# =====================================================================================
dict(
slug='guia-planificar-senalizacion-edificio-publico',
keys=['La señalización es un sistema con siete niveles de información, no un conjunto de carteles.', 'Al menos nueve normas afectan a un edificio público: CTE (DB SUA y DB SI), RIPCI, RD 485/1997, UNE e ISO de señalización, accesibilidad y protección de datos.', 'Un inventario codificado permite reponer cualquier señal años después con el mismo estándar.'],
photo=U + '2026/02/ROTULO-POETA-JOAN-MARAGALL-A-MEDIAS.jpg', photo_caption='Montaje de letras corpóreas en una sede judicial de Madrid. Proyecto SeñalVal.',
num='01',
title='Cómo planificar la señalización de un edificio público',
subtitle='Fases, normativa, agentes implicados y errores que conviene evitar',
cover=U + '2026/02/ROTULO-PLAZA-DE-CASTILLA.jpg',
cover_caption='Tribunal de Instancia · Plaza de Castilla, Madrid. Proyecto SeñalVal.',
intro='''Un edificio público se recorre bajo presión: un ciudadano que llega tarde a una vista, un familiar que busca una habitación, un proveedor que tiene que encontrar el muelle de carga. La señalización no es un conjunto de carteles, sino <b>un sistema de orientación</b> que tiene que funcionar para todos, cumplir la normativa y mantenerse coherente durante años. Esta guía resume cómo plantearlo desde el principio.''',
sections=[
 dict(h='La señalización como sistema', body='''
<p>Los problemas de orientación casi nunca se deben a que falte un cartel, sino a que <b>la información no sigue una lógica</b>: nomenclaturas distintas en cada planta, flechas que se contradicen, directorios desactualizados. Planificar significa definir antes de fabricar <b>qué se dice, dónde y con qué jerarquía</b>.</p>
<table class="t">
<thead><tr><th>Nivel</th><th>Función</th><th>Ejemplos</th></tr></thead>
<tbody>
<tr><td>1 · Identificación del edificio</td><td>Que el edificio se reconozca desde el exterior</td><td>Letras corpóreas en fachada, monolitos, tótems</td></tr>
<tr><td>2 · Direccional exterior</td><td>Llevar a los accesos correctos</td><td>Accesos peatonales, aparcamiento, entrada de proveedores</td></tr>
<tr><td>3 · Directorio general</td><td>Primera decisión al entrar</td><td>Directorio de vestíbulo con plantas y servicios</td></tr>
<tr><td>4 · Directorio de planta</td><td>Confirmar y repartir en cada nivel</td><td>Directorio en desembarco de ascensores y escaleras</td></tr>
<tr><td>5 · Direccional interior</td><td>Guiar en los puntos de decisión</td><td>Banderolas, colgantes, señales de pared</td></tr>
<tr><td>6 · Identificación de dependencias</td><td>Confirmar la llegada</td><td>Placas de sala, despacho, servicio</td></tr>
<tr><td>7 · Normativa y seguridad</td><td>Cumplir y proteger</td><td>Evacuación, extintores, prohibiciones, videovigilancia</td></tr>
</tbody></table>
<p class="note">Regla práctica: una misma dependencia debe llamarse <b>igual</b> en el directorio, en las flechas y en la placa de la puerta.</p>
'''),
 dict(h='Normativa que afecta al proyecto', body='''
<p>Un proyecto de señalización en un edificio público toca varias normas a la vez. Estas son las de referencia en España:</p>
<table class="t">
<thead><tr><th>Norma</th><th>Qué regula para la señalización</th></tr></thead>
<tbody>
<tr><td><b>Código Técnico de la Edificación</b> (Real Decreto 314/2006) · DB SUA 9</td><td>Señalización de los elementos accesibles: entradas, itinerarios, ascensores, aseos, plazas de aparcamiento.</td></tr>
<tr><td><b>CTE · DB SI</b> (Sección SI 3, apdo. 7, y SI 4, apdo. 2)</td><td>Señalización de los medios de evacuación y de las instalaciones manuales de protección contra incendios.</td></tr>
<tr><td><b>Real Decreto 513/2017</b> · Reglamento de instalaciones de protección contra incendios (RIPCI)</td><td>Señalización de los equipos de protección contra incendios.</td></tr>
<tr><td><b>Real Decreto 485/1997</b> · Señalización de seguridad y salud en el trabajo</td><td>Colores y formas de seguridad: prohibición, advertencia, obligación, salvamento y lucha contra incendios.</td></tr>
<tr><td><b>UNE-EN ISO 7010</b></td><td>Pictogramas normalizados de seguridad.</td></tr>
<tr><td><b>UNE 23033-1, UNE 23034 y UNE 23035</b></td><td>Señalización de seguridad contra incendios, de vías de evacuación y fotoluminiscente.</td></tr>
<tr><td><b>UNE 170002:2009</b></td><td>Requisitos de accesibilidad para la rotulación.</td></tr>
<tr><td><b>Real Decreto 193/2023</b></td><td>Condiciones básicas de accesibilidad para el acceso y la utilización de bienes y servicios a disposición del público.</td></tr>
<tr><td><b>Ley Orgánica 3/2018</b> de Protección de Datos (art. 22)</td><td>Cartel informativo obligatorio en las zonas videovigiladas.</td></tr>
</tbody></table>
'''),
 dict(h='Las cinco fases del proyecto', body='''
<div class="steps">
<div class="step"><span>1</span><h4>Estudio y consultoría</h4><p>Visita técnica, recorridos reales de los usuarios, inventario de lo existente, requisitos del organismo y de la normativa.</p><p class="d">Entregable: informe de necesidades e inventario.</p></div>
<div class="step"><span>2</span><h4>Diseño y proyecto</h4><p>Plan de señalización sobre planos, nomenclatura única, manual gráfico, tipologías, mensajes y prototipos.</p><p class="d">Entregable: planos de ubicación, fichas por tipología, muestras.</p></div>
<div class="step"><span>3</span><h4>Fabricación</h4><p>Producción con control de calidad: medidas, colores, contrastes, relieve y braille cuando procede.</p><p class="d">Entregable: fichas técnicas de materiales.</p></div>
<div class="step"><span>4</span><h4>Instalación</h4><p>Por fases y franjas horarias si el edificio está en uso, con la documentación PRL y CAE en regla.</p><p class="d">Entregable: acta de instalación y reportaje fotográfico.</p></div>
<div class="step"><span>5</span><h4>Mantenimiento</h4><p>Inventario vivo para reponer, ampliar o actualizar elementos con el mismo estándar.</p><p class="d">Entregable: inventario final codificado.</p></div>
</div>
<p class="note">Los plazos dependen del tamaño del edificio, del número de elementos y de los tiempos de aprobación del organismo. Conviene reservar en el calendario un periodo específico para la <b>validación de prototipos</b>: es la fase que más retrasos evita después.</p>
'''),
 dict(h='Quién interviene', body='''
<ul class="cols">
<li><b>Organismo o propiedad.</b> Define necesidades, valida nomenclatura y aprueba el diseño.</li>
<li><b>Dirección facultativa.</b> Compatibiliza la señalización con la obra, los acabados y la normativa del edificio.</li>
<li><b>Coordinación de seguridad y salud.</b> Coordina la actividad cuando coinciden varias empresas (Real Decreto 171/2004, que desarrolla el art. 24 de la Ley 31/1995 de Prevención de Riesgos Laborales).</li>
<li><b>Mantenimiento del edificio.</b> Conoce los cambios de uso y será quien pida reposiciones.</li>
<li><b>Usuarios.</b> Personal y ciudadanos: sus recorridos reales son el mejor dato del proyecto.</li>
<li><b>Empresa de señalización.</b> Un único responsable del diseño a la instalación evita que el resultado se pierda entre proveedores.</li>
</ul>
'''),
 dict(h='Instalar en un edificio en uso', body='''
<p>Los edificios públicos rara vez se cierran para señalizar. Eso obliga a planificar la instalación con el mismo cuidado que el diseño:</p>
<ul class="check">
<li>Calendario por zonas y franjas horarias acordado con el organismo.</li>
<li>Documentación de prevención y coordinación de actividades empresariales (CAE) entregada antes de empezar.</li>
<li>Trabajos en altura conforme al Real Decreto 2177/2004, con medios auxiliares adecuados.</li>
<li>Retirada de la señalización antigua, reparación del paramento y limpieza final.</li>
<li>Señalización provisional mientras se sustituye la definitiva, para que nadie se pierda durante la obra.</li>
</ul>
'''),
 dict(h='Inventario y mantenimiento', body='''
<p>La señalización cambia porque el edificio cambia: servicios que se trasladan, despachos que se renombran, normativa que se actualiza. Un <b>inventario codificado</b> permite reponer cualquier pieza años después con exactamente el mismo resultado.</p>
<table class="t t--compact">
<thead><tr><th>Campo de la ficha</th><th>Ejemplo</th></tr></thead>
<tbody>
<tr><td>Código</td><td>P2-DIR-03</td></tr>
<tr><td>Ubicación</td><td>Planta 2, desembarco de ascensores, pared norte</td></tr>
<tr><td>Tipología</td><td>Directorio de planta</td></tr>
<tr><td>Material y acabado</td><td>Aluminio composite, impresión directa, laminado mate</td></tr>
<tr><td>Medidas y fijación</td><td>600 × 900 mm, fijación oculta</td></tr>
<tr><td>Contenido</td><td>Texto validado y versión</td></tr>
<tr><td>Fecha de instalación</td><td>Mes y año</td></tr>
</tbody></table>
'''),
 dict(h='Errores frecuentes', body='''
<ol class="errors">
<li><b>Fabricar sin nomenclatura cerrada.</b> Cada cambio posterior supone rehacer piezas.</li>
<li><b>Señalizar desde el plano y no desde el recorrido.</b> Los puntos de decisión reales no siempre coinciden con los del plano.</li>
<li><b>Demasiada información en cada señal.</b> Una señal que intenta decirlo todo no se lee.</li>
<li><b>Olvidar la accesibilidad hasta el final.</b> El contraste, el relieve y la altura de colocación se deciden en el diseño, no en la instalación.</li>
<li><b>Mezclar proveedores sin un responsable.</b> Distintos acabados, tipografías y criterios en un mismo edificio.</li>
<li><b>No prever el mantenimiento.</b> Sin inventario, cada reposición es un proyecto nuevo.</li>
</ol>
'''),
],
case=dict(
 title='Caso real · Sedes judiciales de Madrid',
 text='''SeñalVal ha ejecutado el cambio de identificación a la denominación <b>«Tribunal de Instancia»</b> en sedes judiciales y edificios públicos de la Comunidad de Madrid, como las de Plaza de Castilla y Poeta Joan Maragall. Servicio llave en mano: retirada de los rótulos anteriores, limpieza de fachada (hidrolimpieza si procede), reparación de desperfectos e instalación de letras corpóreas de PVC negro con frente de aluminio composite o lacado, con coordinación y documentación PRL/CAE cuando el organismo lo requiere.''',
 imgs=[U + '2026/02/ROTULO-PLAZA-DE-CASTILLA-LEJOS.jpg', U + '2026/02/ROTULO-POETA-JOAN-MARAGALL.jpg', U + '2026/04/NAVALCARNERO-1536x1152.jpg'],
),
checklist=['Plano del edificio y usos actualizados', 'Listado de dependencias con nomenclatura definitiva', 'Requisitos de accesibilidad (CTE DB SUA 9, UNE 170002)', 'Señalización de evacuación y PCI (CTE DB SI, RD 513/2017)', 'Manual de identidad del organismo', 'Muestras o prototipos a validar', 'Plan de instalación por fases y horarios', 'Documentación PRL y CAE exigida', 'Inventario codificado como entregable', 'Condiciones de mantenimiento y reposición'],
sources=['Real Decreto 314/2006, por el que se aprueba el Código Técnico de la Edificación (DB SUA y DB SI).', 'Real Decreto 513/2017, Reglamento de instalaciones de protección contra incendios.', 'Real Decreto 485/1997, disposiciones mínimas en materia de señalización de seguridad y salud en el trabajo.', 'Real Decreto 171/2004, por el que se desarrolla el artículo 24 de la Ley 31/1995, de Prevención de Riesgos Laborales, en materia de coordinación de actividades empresariales.', 'Real Decreto 2177/2004, disposiciones mínimas de seguridad y salud para la utilización de equipos de trabajo en trabajos temporales en altura.', 'Real Decreto 193/2023, condiciones básicas de accesibilidad y no discriminación de las personas con discapacidad para el acceso y utilización de los bienes y servicios a disposición del público.', 'Ley Orgánica 3/2018, de Protección de Datos Personales y garantía de los derechos digitales (art. 22).', 'UNE 170002:2009 · UNE-EN ISO 7010 · UNE 23033-1 · UNE 23034 · UNE 23035.'],
),
# =====================================================================================
dict(
slug='guia-senalizacion-accesible-criterios-normativa',
keys=['El CTE (DB SUA 9) fija qué elementos accesibles se señalizan y cómo: SIA, braille en ascensores, pictogramas de aseos entre 0,80 y 1,20 m.', 'ISO 21542 recomienda al menos 30 puntos de diferencia de reflectancia luminosa (LRV) entre texto, fondo y pared.', 'Pictogramas normalizados: UNE-EN ISO 7010 para seguridad e ISO 7001 para información al público.'],
photo=U + '2022/10/PLACA-VESTUARIO-MASCULINO-1024x768.jpg', photo_caption='Placa de identificación con pictograma en altorrelieve y braille. Proyecto SeñalVal.',
num='02',
title='Señalización accesible: criterios y normativa',
subtitle='Contraste, tipografía, altura, relieve y braille para que la señalización funcione para todos',
cover=U + '2022/10/PLACA-VESTUARIOS-1024x768.jpg',
cover_caption='Placa de identificación en altorrelieve y braille. Proyecto SeñalVal.',
intro='''La señalización accesible no es una versión especial para unos pocos: es <b>señalización mejor hecha</b>. Un buen contraste ayuda a quien tiene baja visión, pero también a quien lee con prisa o con poca luz. Un pictograma claro ayuda a quien no habla el idioma. En España, además, es una obligación recogida en el Código Técnico de la Edificación y en la normativa de accesibilidad.''',
sections=[
 dict(h='El marco legal', body='''
<table class="t">
<thead><tr><th>Norma</th><th>Alcance</th></tr></thead>
<tbody>
<tr><td><b>Real Decreto Legislativo 1/2013</b> · Ley General de derechos de las personas con discapacidad</td><td>Establece la accesibilidad universal como condición obligatoria de entornos, bienes y servicios.</td></tr>
<tr><td><b>CTE · DB SUA 9</b> (Real Decreto 314/2006)</td><td>Qué elementos accesibles deben señalizarse en cada uso y cómo.</td></tr>
<tr><td><b>Real Decreto 193/2023</b></td><td>Condiciones básicas de accesibilidad de los bienes y servicios a disposición del público, incluida la información y la señalización.</td></tr>
<tr><td><b>Orden TMA/851/2021</b></td><td>Accesibilidad de los espacios públicos urbanizados, incluida su señalización.</td></tr>
<tr><td><b>UNE 170002:2009</b></td><td>Requisitos de accesibilidad para la rotulación: legibilidad, ubicación, información táctil.</td></tr>
<tr><td><b>UNE 41501:2002</b></td><td>Símbolo Internacional de Accesibilidad (SIA).</td></tr>
<tr><td><b>ISO 21542:2021</b></td><td>Accesibilidad y usabilidad del entorno construido (referencia internacional).</td></tr>
</tbody></table>
'''),
 dict(h='Qué pide el CTE (DB SUA 9)', body='''
<p>El Documento Básico de Seguridad de Utilización y Accesibilidad establece, entre otros, estos requisitos de señalización:</p>
<ul class="check">
<li>Las <b>entradas accesibles</b>, los itinerarios, las plazas de aparcamiento y los servicios accesibles se señalizan con el <b>Símbolo Internacional de Accesibilidad</b> (SIA), cuyas características fija la norma UNE 41501.</li>
<li>Los <b>ascensores accesibles</b> se señalizan mediante SIA y cuentan con indicación en <b>braille y arábigo en altorrelieve</b> del número de planta en la jamba derecha, en sentido salida de la cabina.</li>
<li>Los <b>servicios higiénicos de uso general</b> se señalizan con pictogramas normalizados de sexo en altorrelieve y contraste cromático, a una altura <b>entre 0,80 y 1,20 m</b>, junto al marco, a la derecha de la puerta y en el sentido de la entrada.</li>
<li>Las <b>bandas señalizadoras visuales y táctiles</b> son de color contrastado con el pavimento, con relieve de <b>3 ± 1 mm en interiores y 5 ± 1 mm en exteriores</b>.</li>
<li>Las características de la información táctil (relieve, braille) se remiten a la norma <b>UNE 170002</b>.</li>
</ul>
<p class="note">La tabla 2.1 del DB SUA 9 indica qué elementos accesibles deben señalizarse según el uso del edificio (residencial público, docente, administrativo, sanitario, comercial…). Es el punto de partida de cualquier proyecto.</p>
'''),
 dict(h='Los cuatro criterios de diseño', body='''
<div class="grid4">
<div class="card"><h4>Legible</h4><p>Tipografía sin remates, de trazo uniforme, con mayúsculas y minúsculas. Tamaño de letra proporcional a la distancia de lectura. Mensajes breves.</p></div>
<div class="card"><h4>Contrastada</h4><p>Contraste cromático entre texto y fondo, y entre la señal y la pared. ISO 21542 recomienda una diferencia de reflectancia luminosa (LRV) de al menos <b>30 puntos</b>.</p></div>
<div class="card"><h4>Táctil</h4><p>Altorrelieve y braille en las señales que se leen al tacto (puertas, ascensores, aseos), según UNE 170002, situadas siempre en la misma posición.</p></div>
<div class="card"><h4>Previsible</h4><p>Misma ubicación, mismo formato y misma nomenclatura en todo el edificio. La coherencia es lo que permite orientarse sin ayuda.</p></div>
</div>
<p class="note">Acabados <b>mate</b>: los reflejos de los acabados brillantes reducen la legibilidad, sobre todo para personas con baja visión y en zonas con mucha luz natural.</p>
'''),
 dict(h='Pictogramas: usar los normalizados', body='''
<p>Un pictograma inventado obliga a interpretarlo; uno normalizado se reconoce sin pensar. Para seguridad y evacuación son obligatorios los de <b>UNE-EN ISO 7010</b>. Para información al público (aseos, ascensor, información, cafetería…) la referencia es <b>ISO 7001</b>. El texto debe acompañar al pictograma cuando el mensaje no es universal.</p>
<table class="t t--compact">
<thead><tr><th>Color de seguridad (RD 485/1997)</th><th>Significado</th></tr></thead>
<tbody>
<tr><td><span class="sw" style="background:#C8102E"></span> Rojo</td><td>Prohibición, peligro-alarma, material y equipos de lucha contra incendios</td></tr>
<tr><td><span class="sw" style="background:#F2C200"></span> Amarillo o amarillo anaranjado</td><td>Advertencia</td></tr>
<tr><td><span class="sw" style="background:#1F5FAD"></span> Azul</td><td>Obligación</td></tr>
<tr><td><span class="sw" style="background:#00843D"></span> Verde</td><td>Salvamento o auxilio, situación de seguridad</td></tr>
</tbody></table>
'''),
 dict(h='Residencias y centros sociosanitarios', body='''
<p>En entornos donde viven personas mayores o con deterioro cognitivo, la señalización tiene un papel terapéutico además de informativo:</p>
<ul class="check">
<li>Iconos grandes y figurativos en puertas (habitación, baño, comedor) junto al texto.</li>
<li>Códigos de color por zonas o plantas para reforzar la memoria del recorrido.</li>
<li>Contraste alto entre puerta y pared en los espacios que el residente debe encontrar.</li>
<li>Materiales lisos y resistentes a la limpieza y desinfección frecuentes.</li>
</ul>
'''),
],
case=dict(
 title='Caso real · Residencia de Clece en Burgos',
 text='''SeñalVal instaló en una residencia de Clece en Burgos vinilos con <b>iconografía clara</b> en las puertas de entrada, interiores y despachos, pensados para que residentes, familias y personal se orienten de un vistazo. En otros proyectos de SeñalVal, las placas de identificación incorporan <b>altorrelieve y braille</b> para su lectura táctil.''',
 imgs=[U + '2025/02/FOTO-ICONO-PUERTA-INTERIOR-ENTRADA-768x1024.jpg', U + '2025/02/FOTO-ICONO-Y-FLOR-DESPACHO-768x1024.jpg', U + '2022/10/PLACA-VESTUARIO-FEMENINO-1024x768.jpg'],
),
checklist=['Revisar la tabla 2.1 del DB SUA 9 para el uso del edificio', 'SIA (UNE 41501) en entradas, itinerarios, ascensores, aseos y plazas accesibles', 'Braille y altorrelieve del número de planta en ascensores accesibles', 'Pictogramas de aseos en altorrelieve, entre 0,80 y 1,20 m, a la derecha de la puerta', 'Contraste LRV ≥ 30 puntos entre texto, fondo y pared', 'Tipografía sin remates, acabados mate', 'Pictogramas UNE-EN ISO 7010 (seguridad) e ISO 7001 (información)', 'Información táctil según UNE 170002, siempre en la misma posición', 'Bandas señalizadoras: 3 ± 1 mm interior, 5 ± 1 mm exterior', 'Validar con usuarios reales antes de fabricar la serie'],
sources=['Real Decreto Legislativo 1/2013, Texto Refundido de la Ley General de derechos de las personas con discapacidad y de su inclusión social.', 'Real Decreto 314/2006, Código Técnico de la Edificación · Documento Básico SUA, Sección SUA 9 «Accesibilidad».', 'Real Decreto 193/2023, condiciones básicas de accesibilidad y no discriminación para el acceso y utilización de los bienes y servicios a disposición del público.', 'Orden TMA/851/2021, documento técnico de condiciones básicas de accesibilidad y no discriminación para el acceso y la utilización de los espacios públicos urbanizados.', 'Real Decreto 485/1997, señalización de seguridad y salud en el trabajo (Anexo II, colores de seguridad).', 'UNE 170002:2009 Requisitos de accesibilidad para la rotulación · UNE 41501:2002 Símbolo de accesibilidad para la movilidad.', 'ISO 21542:2021 Building construction — Accessibility and usability of the built environment.', 'UNE-EN ISO 7010 Símbolos gráficos de seguridad · ISO 7001 Símbolos de información pública.'],
),
# =====================================================================================
dict(
slug='guia-materiales-senalizacion',
keys=['No hay un material mejor: hay un material adecuado para cada uso, entorno y vida útil.', 'En costa o ambientes industriales, acero AISI 316; en sanidad, superficies lisas y resistentes a desinfectantes.', 'La reacción al fuego se clasifica según UNE-EN 13501-1 y, en fachadas, la condiciona el CTE DB SI 2.'],
photo=U + '2025/02/FOTO-DIRECTORIO-PLANTA-2-768x1024.jpg', photo_caption='Directorio de planta en aluminio composite con impresión directa · Salamanca. Proyecto SeñalVal.',
num='03',
title='Materiales: qué elegir según uso y entorno',
subtitle='Aluminio, composite, metacrilato, PVC, acero y vinilo comparados para interior y exterior',
cover=U + '2025/09/ROTULO-AZOTEA-2-1024x768.jpg',
cover_caption='Rótulo de azotea con vinilo de alta resistencia · San Sebastián. Proyecto SeñalVal.',
intro='''El material decide cuánto dura una señal, cómo envejece, cuánto cuesta mantenerla y si cumple la normativa del lugar donde se instala. No hay un material mejor que otro: hay <b>un material adecuado para cada uso</b>. Esta guía compara los más habituales en proyectos profesionales y explica cómo elegir.''',
sections=[
 dict(h='Comparativa de materiales', body='''
<table class="t t--mat">
<thead><tr><th>Material</th><th>Uso ideal</th><th>Int.</th><th>Ext.</th><th>Puntos fuertes</th><th>A tener en cuenta</th></tr></thead>
<tbody>
<tr><td><b>Aluminio composite</b> (ACM, tipo Dibond)</td><td>Directorios, placas, carteles, rótulos planos</td><td>●</td><td>●</td><td>Ligero, rígido, plano; admite impresión directa</td><td>Elegir núcleo según reacción al fuego exigida</td></tr>
<tr><td><b>Aluminio extruido o lacado</b></td><td>Monolitos, tótems, banderolas, sistemas modulares</td><td>●</td><td>●</td><td>Muy duradero; piezas intercambiables</td><td>Mayor coste inicial</td></tr>
<tr><td><b>Metacrilato</b> (PMMA)</td><td>Placas de despacho, directorios, rótulos retroiluminados</td><td>●</td><td>◐</td><td>Acabado premium; muy buena transmisión de luz</td><td>Se raya; en exterior, calidad colada y protección UV</td></tr>
<tr><td><b>PVC espumado</b></td><td>Señalética interior económica, letras corpóreas</td><td>●</td><td>◐</td><td>Ligero, fácil de mecanizar, económico</td><td>Menos rígido; puede deformarse con el calor</td></tr>
<tr><td><b>Acero inoxidable</b> AISI 304 / 316</td><td>Placas institucionales, letras corpóreas, zonas de alto tránsito</td><td>●</td><td>●</td><td>Antivandálico, imagen institucional, fácil limpieza</td><td>En ambiente marino o industrial, AISI 316</td></tr>
<tr><td><b>Vinilo</b></td><td>Cristaleras, paredes, vehículos, rótulos de corte</td><td>●</td><td>●</td><td>Versátil, rápido de instalar y renovar</td><td>Durabilidad según calidad (monomérico, polimérico, cast)</td></tr>
<tr><td><b>Fotoluminiscente</b></td><td>Evacuación y equipos contra incendios</td><td>●</td><td>—</td><td>Visible sin suministro eléctrico</td><td>Debe cumplir UNE 23035</td></tr>
</tbody></table>
<p class="legend">● adecuado · ◐ con condiciones · — no habitual</p>
'''),
 dict(h='Claves por material', body='''
<div class="grid2">
<div class="card"><h4>Aluminio composite</h4><p>Dos láminas de aluminio con un núcleo intermedio. Es el material más versátil para señalética plana: admite impresión directa en alta definición, corte a medida y uso exterior. El núcleo puede ser de polietileno o ignífugo (FR / mineral); su clasificación de reacción al fuego se expresa en Euroclases según <b>UNE-EN 13501-1</b>.</p></div>
<div class="card"><h4>Acero inoxidable</h4><p>El AISI 304 cubre la mayoría de usos interiores y exteriores urbanos. El <b>AISI 316</b> incorpora molibdeno, que mejora su resistencia a la corrosión, y es la elección para costa, piscinas o entornos industriales.</p></div>
<div class="card"><h4>Metacrilato</h4><p>Ofrece el acabado más elegante en interiores y una transmisión luminosa muy alta en su versión transparente, lo que lo hace ideal para rótulos retroiluminados. En exterior conviene metacrilato colado con protección UV.</p></div>
<div class="card"><h4>Vinilo</h4><p>Su vida útil depende de la gama: los <b>monoméricos</b> se usan en aplicaciones de corta duración, los <b>poliméricos</b> en media duración y los <b>cast</b> (fundidos) en larga duración y superficies curvas, como los vehículos. La durabilidad concreta la indica la ficha técnica de cada fabricante.</p></div>
</div>
'''),
 dict(h='Cómo elegir según el entorno', body='''
<table class="t">
<thead><tr><th>Entorno</th><th>Recomendación</th></tr></thead>
<tbody>
<tr><td>Exterior con sol y lluvia</td><td>Aluminio composite o lacado, vinilos y tintas con protección UV, tornillería inoxidable.</td></tr>
<tr><td>Costa o ambiente industrial</td><td>Acero inoxidable AISI 316, aluminio lacado, fijaciones inoxidables.</td></tr>
<tr><td>Hospitales y residencias</td><td>Superficies lisas y no porosas, resistentes a la limpieza y a los desinfectantes; esquinas redondeadas.</td></tr>
<tr><td>Alto tránsito o riesgo de vandalismo</td><td>Acero inoxidable, fijación oculta antirrobo, laminado antigrafiti.</td></tr>
<tr><td>Espacios que cambian a menudo</td><td>Sistemas modulares con piezas intercambiables y vinilos fáciles de sustituir.</td></tr>
<tr><td>Fachadas</td><td>Letras corpóreas o rótulos en aluminio, acero o PVC con frente de composite; con LED si debe verse de noche.</td></tr>
</tbody></table>
'''),
 dict(h='Normativa que condiciona el material', body='''
<ul class="check">
<li><b>Reacción al fuego.</b> Se clasifica según UNE-EN 13501-1. En fachadas, el Documento Básico DB SI 2 del CTE fija exigencias para los sistemas constructivos de fachada; si un rótulo forma parte de ese sistema, su material debe cumplirlas. Conviene validarlo con la dirección facultativa.</li>
<li><b>Señalización de evacuación y contra incendios.</b> Fotoluminiscente conforme a UNE 23035, con pictogramas UNE-EN ISO 7010.</li>
<li><b>Videovigilancia.</b> El cartel informativo es obligatorio según el art. 22 de la Ley Orgánica 3/2018 de Protección de Datos. Debe ser visible y estar colocado antes de entrar en la zona vigilada.</li>
<li><b>Accesibilidad.</b> Acabados mate y relieve táctil cuando lo exijan el DB SUA 9 y la UNE 170002.</li>
</ul>
'''),
],
case=dict(
 title='Casos reales · Composite, dibond y vinilo',
 text='''En <b>Salamanca</b>, SeñalVal fabricó directorios generales, directorios de planta y placas de áreas en <b>aluminio composite con impresión directa</b>. Para la <b>Fundación Laboral de la Construcción</b>, carteles de zona videovigilada en el mismo material, aptos para exterior. En <b>San Sebastián</b>, un rótulo de azotea con <b>vinilo de alta resistencia</b>, visible desde lejos, y placas de dibond.''',
 imgs=[U + '2025/02/FOTO-DIRECTORIO-GENERAL-768x1024.jpg', U + '2025/02/FOTO-CARTEL-1-768x1024.jpg', U + '2025/09/ROTULO-AZOTEA-1024x768.jpg'],
),
checklist=['¿Interior, exterior o ambos?', '¿Ambiente marino, industrial o sanitario?', '¿Riesgo de vandalismo o alto tránsito?', '¿Debe verse de noche (retroiluminación)?', '¿Exigencia de reacción al fuego (UNE-EN 13501-1, CTE DB SI)?', '¿Señalización de evacuación (UNE 23035)?', '¿Requisitos táctiles o de contraste (DB SUA 9, UNE 170002)?', '¿Cada cuánto cambiará el contenido?', 'Vida útil esperada frente a presupuesto', 'Ficha técnica del fabricante para cada material'],
sources=['UNE-EN 13501-1 Clasificación en función del comportamiento frente al fuego de los productos de construcción.', 'Real Decreto 314/2006, Código Técnico de la Edificación · DB SI (Seguridad en caso de incendio) y DB SUA.', 'UNE 23035 Seguridad contra incendios. Señalización fotoluminiscente · UNE-EN ISO 7010.', 'Ley Orgánica 3/2018, de Protección de Datos Personales y garantía de los derechos digitales (art. 22, videovigilancia).', 'UNE 170002:2009 Requisitos de accesibilidad para la rotulación.', 'Fichas técnicas de los fabricantes de cada material (durabilidad, resistencia UV, reacción al fuego).'],
),
]
