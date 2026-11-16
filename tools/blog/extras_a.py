# -*- coding: utf-8 -*-
# Mejoras SEO por entrada (1-16): palabra clave, título y descripción SEO, párrafo inicial,
# sección nueva (con enlace externo a la fuente oficial) y texto alternativo de la imagen.
B = 'https://www.boe.es/buscar/act.php?id='
CTE, RD485, LOPD, LCSP, RIPCI, RD193, RDL1, RD171 = (B + 'BOE-A-2006-5515', B + 'BOE-A-1997-8668', B + 'BOE-A-2018-16673', B + 'BOE-A-2017-12902',
    B + 'BOE-A-2017-6606', B + 'BOE-A-2023-7417', B + 'BOE-A-2013-12632', B + 'BOE-A-2004-1848')
CTEWEB, AEPD, INSST = 'https://www.codigotecnico.org/', 'https://www.aepd.es/', 'https://www.insst.es/'

EXTRAS_A = {
'senalizacion-sedes-judiciales-tribunales-de-instancia': dict(
 focus='señalización de sedes judiciales',
 seo_title='Señalización de sedes judiciales | SeñalVal',
 metadesc='Señalización de sedes judiciales para los Tribunales de Instancia: letras de fachada, directorios y placas sin cerrar el edificio. Casos reales en Madrid.',
 intro='La **señalización de sedes judiciales** vive un momento de cambio en toda España. Por eso conviene planificarla bien: un juzgado recibe cada día a ciudadanos, abogados y funcionarios que necesitan orientarse rápido.',
 section='''## Señalización de sedes judiciales: normativa que hay que respetar
Además de la imagen institucional, la señalización de sedes judiciales debe cumplir varias normas técnicas. En primer lugar, el [Código Técnico de la Edificación]({CTE}) exige señalizar los elementos accesibles y los recorridos de evacuación. Asimismo, los equipos contra incendios se señalizan según el [Reglamento de instalaciones de protección contra incendios]({RIPCI}).

Por otro lado, la obra se hace con el edificio en uso. En consecuencia, hay que coordinar a todas las empresas presentes, tal y como pide el [Real Decreto 171/2004]({RD171}) sobre coordinación de actividades empresariales.

Por todo ello, el orden de trabajo importa:
- Primero, inventario de lo existente y validación de la nueva nomenclatura.
- Después, fabricación de letras, directorios y placas.
- Finalmente, instalación por fases y entrega del inventario.

De este modo, el organismo recibe un sistema completo y coherente. Además, cada sede queda documentada para futuras reposiciones. Si quiere ver otros edificios de la Administración, consulte nuestra página de [señalética para organismos públicos](/senaletica-organismos-publicos).''',
 img2_alt='Señalización de sedes judiciales: montaje de letras corpóreas «Tribunal de Instancia» en Madrid'),

'senalizacion-aeropuertos-estaciones-wayfinding': dict(
 focus='señalización de aeropuertos y estaciones',
 seo_title='Señalización de aeropuertos y estaciones | SeñalVal',
 metadesc='Señalización de aeropuertos y estaciones: jerarquía de mensajes, pictogramas, visibilidad nocturna y mantenimiento para orientar a miles de viajeros.',
 intro='La **señalización de aeropuertos y estaciones** tiene un reto único: orientar a miles de personas por hora que, además, suelen tener prisa. Por eso cada mensaje debe ser breve, claro y estar en el lugar exacto.',
 section='''## Señalización de aeropuertos y estaciones: seguridad y evacuación
Aunque el viajero se fija sobre todo en andenes y salidas, la señalización de aeropuertos y estaciones también protege. En primer lugar, los recorridos de evacuación se señalizan según el [Código Técnico de la Edificación]({CTE}). Asimismo, los equipos contra incendios siguen el [Reglamento de instalaciones de protección contra incendios]({RIPCI}).

Por otra parte, en zonas de trabajo y talleres de mantenimiento se aplica el [Real Decreto 485/1997]({RD485}) de señalización de seguridad. Así, colores y pictogramas significan lo mismo en todo el recinto.

Por eso, conviene coordinar desde el principio tres capas de información:
- Orientación del viajero: destinos, servicios y conexiones.
- Seguridad: evacuación, extintores y salidas.
- Operación: zonas restringidas, muelles y accesos técnicos.

De este modo, ninguna señal contradice a otra. Además, el mantenimiento resulta más sencillo, porque todas siguen el mismo sistema. Si le interesa el concepto general, lea nuestra guía sobre [qué es el wayfinding](/que-es-wayfinding).''',
 img2_alt='Señalización de aeropuertos y estaciones: cajón luminoso de dársena en la estación de Palencia'),

'senalizacion-accesible-normativa-espana': dict(
 focus='señalización accesible',
 seo_title='Señalización accesible: normativa y braille | SeñalVal',
 metadesc='Señalización accesible en España: qué exigen el CTE DB SUA 9, la UNE 170002 y el RD 193/2023. Braille, altorrelieve, contraste y altura de colocación.',
 intro='La **señalización accesible** es hoy una obligación legal y, además, una forma de hacer edificios más fáciles para todos. A continuación explicamos qué exige la normativa española y cómo aplicarla en un proyecto real.',
 section='''## Señalización accesible: dónde consultar la normativa oficial
Antes de redactar un proyecto, conviene leer las fuentes originales. Por ejemplo, el [Código Técnico de la Edificación]({CTE}) incluye el Documento Básico SUA, cuya sección 9 trata la accesibilidad. Además, el portal oficial del [CTE]({CTEWEB}) publica los documentos básicos actualizados y sus comentarios.

Por otro lado, el [Real Decreto Legislativo 1/2013]({RDL1}) fija la accesibilidad universal como principio general. Asimismo, el [Real Decreto 193/2023]({RD193}) concreta las condiciones básicas de accesibilidad de bienes y servicios a disposición del público.

En la práctica, la señalización accesible se resume en pocas reglas:
- Primero, contraste alto entre texto, fondo y pared.
- Después, tipografía clara y mensajes breves.
- Además, altorrelieve y braille donde la señal se lee con la mano.
- Finalmente, la misma posición en todo el edificio.

Por eso, lo más eficaz es incluirla desde el diseño y no al final de la obra. Así se evitan cambios caros. Si necesita placas táctiles, vea nuestra [señalética en braille](/senaletica-en-braile). Además, en residencias le será útil nuestra guía de [señalética para residencias](/senaletica-residencias-mayores-valladolid).''',
 img2_alt='Señalización accesible: placa de aluminio con texto en braille y altorrelieve'),

'licitacion-publica-senalizacion-como-preparar-oferta': dict(
 focus='licitación pública de señalización',
 seo_title='Licitación pública de señalización | SeñalVal',
 metadesc='Licitación pública de señalización: cómo preparar la memoria técnica, acreditar la solvencia y evitar los errores que excluyen una oferta.',
 intro='La **licitación pública de señalización** es la vía habitual por la que las administraciones renuevan la señalética de sus edificios. Sin embargo, muchas ofertas se quedan fuera por detalles formales. Por eso vale la pena prepararlas con método. Además, una buena memoria técnica marca la diferencia. Así, la empresa demuestra que ha entendido el edificio.',
 section='''## Licitación pública de señalización: la ley que lo regula todo
Cada licitación pública de señalización siguen la [Ley 9/2017 de Contratos del Sector Público]({LCSP}). Por eso conviene conocer sus conceptos básicos: procedimiento, solvencia, criterios de adjudicación y plazos.

En primer lugar, la ley distingue entre criterios evaluables mediante fórmula y criterios que dependen de un juicio de valor. Así, el precio suele valorarse con fórmula, mientras que la memoria técnica se puntúa por su calidad.

Además, en edificios públicos en uso se exige coordinar a las empresas presentes, según el [Real Decreto 171/2004]({RD171}). Por consiguiente, tener lista la documentación de prevención acelera el inicio de los trabajos.

Por último, la señalización ofertada debe cumplir la normativa técnica:
- Accesibilidad según el [Código Técnico de la Edificación]({CTE}).
- Evacuación y equipos contra incendios según el [RIPCI]({RIPCI}).
- Señalización de seguridad según el [Real Decreto 485/1997]({RD485}).

De este modo, la oferta demuestra solvencia técnica real. Además, conviene explicar el [precio de la señalética](/precio-proyecto-senaletica-edificio) por elementos. Si el edificio es judicial, lea también nuestro artículo sobre [señalización de sedes judiciales](/senalizacion-sedes-judiciales-tribunales-de-instancia).''',
 img2_alt='Licitación pública de señalización: señalética para edificios de organismos públicos'),

'senalizacion-evacuacion-fotoluminiscente-normativa': dict(
 focus='señalización fotoluminiscente',
 seo_title='Señalización fotoluminiscente: normativa | SeñalVal',
 metadesc='Señalización fotoluminiscente de evacuación: qué exigen el CTE, el RIPCI y las normas UNE, dónde colocarla, qué tamaño elegir y cómo mantenerla.',
 intro='La **señalización fotoluminiscente** es la que sigue guiando a las personas cuando falla la luz en una emergencia. Por eso la normativa la exige en recorridos y salidas de evacuación de la mayoría de edificios.',
 section='''## Señalización fotoluminiscente: normas oficiales que la regulan
Para diseñar bien la señalización fotoluminiscente conviene consultar las fuentes. En primer lugar, el [Código Técnico de la Edificación]({CTE}) recoge en su Documento Básico SI la señalización de los medios de evacuación. Asimismo, el [Reglamento de instalaciones de protección contra incendios]({RIPCI}) regula la señalización de extintores, bocas de incendio y pulsadores.

Además, en lugares de trabajo se aplica el [Real Decreto 485/1997]({RD485}), que define los colores de seguridad. Así, el verde indica salvamento y el rojo, equipos contra incendios.

Por eso, una revisión completa del edificio comprueba:
- Primero, que cada salida y cada cambio de dirección tienen su señal.
- Después, que ninguna señal queda tapada por mobiliario.
- Además, que el tamaño es adecuado a la distancia de lectura.
- Finalmente, que las señales dañadas se sustituyen.

De este modo, la señalización fotoluminiscente cumple su función cuando de verdad hace falta. También puede repasar el significado de colores y formas en nuestra guía de [señales de seguridad](/senales-seguridad-colores-iso-7010).''',
 img2_alt='Señalización fotoluminiscente: señal de salida de evacuación en un edificio público'),

'precio-proyecto-senaletica-edificio': dict(
 focus='precio de la señalética',
 seo_title='Precio de la señalética de un edificio | SeñalVal',
 metadesc='Precio de la señalética de un edificio: qué factores lo deciden (piezas, materiales, diseño e instalación) y cómo comparar presupuestos de forma justa.',
 intro='El **precio de la señalética** depende de muchas variables, y por eso dos presupuestos para el mismo edificio pueden ser muy distintos. A continuación explicamos qué lo encarece, qué lo abarata y cómo comparar.',
 section='''## Precio de la señalética: costes que no se ven a primera vista
Además de las piezas, el precio de la señalética incluye trabajos que no siempre aparecen en un presupuesto rápido. Por ejemplo, la retirada de la señalización antigua y la reparación del paramento. Asimismo, en edificios públicos puede ser necesaria documentación de prevención y coordinación, según el [Real Decreto 171/2004]({RD171}).

Por otro lado, la normativa también influye en el coste. Así, las placas táctiles que pide el [Código Técnico de la Edificación]({CTE}) requieren un proceso de fabricación específico. Del mismo modo, la señalización de evacuación sigue el [RIPCI]({RIPCI}) y debe tener el tamaño adecuado.

Por eso, antes de comparar precios conviene preguntar:
- Primero, si incluye diseño, fabricación e instalación.
- Después, si incluye la retirada de lo antiguo.
- Además, qué material exacto se oferta.
- Finalmente, qué garantía y qué plan de reposición ofrece.

De este modo, el precio de la señalética se compara de forma justa. Por otra parte, el material influye mucho: compare opciones en [placas de señalética](/placas-senaletica-valladolid). Si su edificio es de la Administración, le resultará útil nuestro artículo sobre [licitaciones de señalización](/licitacion-publica-senalizacion-como-preparar-oferta).''',
 img2_alt='Precio de la señalética: señalización en vinilo de un taller de formación'),

'empresa-senaletica-valladolid': dict(
 focus='empresa de señalética en Valladolid',
 seo_title='Empresa de señalética en Valladolid | SeñalVal',
 metadesc='Empresa de señalética en Valladolid: diseñamos, fabricamos e instalamos placas, directorios, rótulos y vinilos para empresas e instituciones.',
 intro='SeñalVal es una **empresa de señalética en Valladolid** que diseña, fabrica e instala desde su propio taller en la ciudad. Así, un solo equipo responde del resultado de principio a fin. Conozca nuestra [señalética en Valladolid](/) y los proyectos que la avalan.',
 section='''## Una empresa de señalética en Valladolid que cumple la normativa
Como empresa de señalética en Valladolid, aplicamos las mismas normas que en el resto de España. En primer lugar, los edificios de uso público siguen el [Código Técnico de la Edificación]({CTE}) en accesibilidad y evacuación. Asimismo, los lugares de trabajo aplican el [Real Decreto 485/1997]({RD485}) de señalización de seguridad.

Por otra parte, muchas empresas y organismos vallisoletanos instalan cámaras de seguridad. En ese caso, el cartel de zona videovigilada es obligatorio según la [Ley Orgánica 3/2018]({LOPD}).

Por eso, en cada proyecto revisamos:
- Primero, qué señalización obliga la normativa en su edificio.
- Después, qué necesita realmente el visitante para orientarse.
- Además, qué imagen quiere transmitir la empresa.
- Finalmente, cómo mantener todo actualizado con el tiempo.

De este modo, como empresa de señalética en Valladolid, entregamos un trabajo útil, legal y coherente con su marca. Además, al estar en la ciudad, atendemos reposiciones con rapidez. Si su sector es público, vea nuestra [señalética para organismos públicos en Valladolid](/senaletica-organismos-publicos-valladolid).''',
 img2_alt='Empresa de señalética en Valladolid: directorio de planta en vinilo en un centro de formación'),

'senaletica-madrid-edificios-publicos-empresas': dict(
 focus='señalética para edificios en Madrid',
 seo_title='Señalética para edificios en Madrid | SeñalVal',
 metadesc='Señalética para edificios en Madrid: sedes judiciales, oficinas y sedes corporativas. Diseño, fabricación e instalación con equipo propio.',
 intro='La **señalética para edificios en Madrid** tiene que estar a la altura de sedes grandes, con mucho público y una imagen exigente. Por eso trabajamos allí con el mismo método que en Valladolid.',
 section='''## Señalética para edificios en Madrid: normativa y coordinación
En sedes grandes, la señalética para edificios en Madrid debe coordinarse con varias normas a la vez. En primer lugar, la accesibilidad y la evacuación siguen el [Código Técnico de la Edificación]({CTE}). Además, los equipos contra incendios se señalizan según el [RIPCI]({RIPCI}).

Por otra parte, en sedes públicas y oficinas con muchas empresas trabajando a la vez, la instalación exige coordinar actividades, como establece el [Real Decreto 171/2004]({RD171}). Por consiguiente, entregamos la documentación de prevención antes de empezar.

Así organizamos un proyecto de señalética para edificios en Madrid:
- Primero, visita técnica y propuesta con planos de ubicación.
- Después, aprobación del diseño y de los prototipos.
- A continuación, fabricación en nuestro taller.
- Finalmente, instalación por fases, sin interrumpir la actividad.

De este modo, el cliente tiene un único interlocutor durante todo el proceso. Además, cada pieza queda inventariada para futuras reposiciones. Vea también nuestra página de [señalética en Madrid](/senaletica-madrid), con más trabajos realizados en la capital.''',
 img2_alt='Señalética para edificios en Madrid: rótulo de aluminio en Parque Norte'),

'senaletica-burgos-empresas-residencias': dict(
 focus='señalética para empresas en Burgos',
 seo_title='Señalética para empresas en Burgos | SeñalVal',
 metadesc='Señalética para empresas en Burgos, residencias y comercios: placas, directorios, vinilos y rótulos pensados para el clima de Burgos.',
 intro='La **señalética para empresas en Burgos** es una de nuestras especialidades fuera de Valladolid. Además, al estar a poco más de una hora, podemos visitar, instalar y reponer con rapidez.',
 section='''## Señalética para empresas en Burgos: qué obliga la normativa
Además de la imagen, la señalética para empresas en Burgos debe cumplir la normativa estatal. Por ejemplo, las residencias y edificios de uso público siguen el [Código Técnico de la Edificación]({CTE}) en accesibilidad y evacuación. Asimismo, las naves y talleres de la provincia aplican el [Real Decreto 485/1997]({RD485}) de señalización de seguridad.

Por otra parte, si un negocio tiene cámaras, debe colocar el cartel de zona videovigilada que exige la [Ley Orgánica 3/2018]({LOPD}). Así evita sanciones y, además, informa correctamente a sus clientes.

Por eso, cuando preparamos un proyecto de señalética para empresas en Burgos, revisamos:
- Primero, la señalización obligatoria del edificio.
- Después, la orientación de visitantes y residentes.
- Además, el material adecuado para heladas y humedad.
- Finalmente, las ordenanzas si el local está en el casco histórico.

De este modo, el resultado es útil, legal y duradero. También puede ver nuestra [señalética en Burgos](/top-soluciones) y el [mejor servicio de señalética en Burgos](/mejor-servicio-de-senaletica-en-burgos).''',
 img2_alt='Señalética para empresas en Burgos: vinilos de orientación en una residencia'),

'senaletica-castilla-y-leon-provincias': dict(
 slug='empresa-senaletica-castilla-y-leon',
 focus='empresa de señalética en Castilla y León',
 seo_title='Empresa de señalética en Castilla y León | SeñalVal',
 metadesc='Empresa de señalética en Castilla y León con taller en Valladolid: proyectos en Burgos, Salamanca, Palencia, Zamora y el resto de provincias.',
 intro='Ser una **empresa de señalética en Castilla y León** exige recorrer una comunidad muy extensa. Por eso nuestro taller en Valladolid, en el centro de la región, es una ventaja: llegamos rápido a cualquier provincia.',
 section='''## Empresa de señalética en Castilla y León: una normativa común
Aunque cada provincia es distinta, como empresa de señalética en Castilla y León seguimos las mismas normas estatales. En primer lugar, el [Código Técnico de la Edificación]({CTE}) regula la accesibilidad y la evacuación de los edificios. Además, el [Real Decreto 193/2023]({RD193}) fija las condiciones de accesibilidad de los servicios al público.

Por otra parte, los organismos públicos de la región contratan según la [Ley de Contratos del Sector Público]({LCSP}). Por consiguiente, conocer sus procedimientos ahorra tiempo a todos.

Así trabajamos en cada provincia:
- Primero, visita técnica desde Valladolid.
- Después, propuesta con planos y prototipos.
- A continuación, fabricación en nuestro taller.
- Finalmente, instalación con equipo propio y mantenimiento.

De este modo, como empresa de señalética en Castilla y León, ofrecemos un único responsable. Además, el mismo equipo atiende las reposiciones años después. Vea nuestra página de [señalética en Castilla y León](/senaletica-castilla-y-leon) con más proyectos.''',
 img2_alt='Empresa de señalética en Castilla y León: directorio de planta en Salamanca'),

'senaletica-organismos-publicos-valladolid': dict(
 slug='senalizacion-edificios-publicos-valladolid',
 focus='señalización de edificios públicos en Valladolid',
 seo_title='Señalización de edificios públicos en Valladolid | SeñalVal',
 metadesc='Señalización de edificios públicos en Valladolid: atención al ciudadano, accesibilidad, licitaciones e instalación con el edificio abierto.',
 intro='La **señalización de edificios públicos en Valladolid** tiene un objetivo claro: que el ciudadano encuentre el servicio que busca a la primera. Por eso, en Valladolid, sede de la Junta y de muchas administraciones, es un trabajo especialmente exigente.',
 section='''## Señalización de edificios públicos en Valladolid: el marco legal
Además de la imagen institucional, la señalización de edificios públicos en Valladolid debe cumplir varias normas. En primer lugar, el [Código Técnico de la Edificación]({CTE}) regula la accesibilidad y la evacuación. Asimismo, el [Real Decreto 193/2023]({RD193}) exige condiciones de accesibilidad en los servicios al público.

Por otra parte, la contratación sigue la [Ley 9/2017 de Contratos del Sector Público]({LCSP}). Por consiguiente, la empresa adjudicataria debe aportar documentación técnica y de seguridad en plazo.

Así planteamos cada proyecto:
- Primero, análisis de los servicios y de los flujos de ciudadanos.
- Después, propuesta coherente con el manual de identidad del organismo.
- A continuación, fabricación con materiales duraderos.
- Finalmente, instalación sin interrumpir la atención al público.

De este modo, la señalización de edificios públicos mejora la atención y transmite una imagen ordenada. Además, queda documentada para futuros cambios. Vea más ejemplos de nuestra [señalética para organismos públicos](/senaletica-organismos-publicos).''',
 img2_alt='Señalización de edificios públicos en Valladolid: interior de un edificio de la Administración'),

'placas-senaletica-valladolid': dict(
 focus='placas de señalética',
 seo_title='Placas de señalética para puertas y despachos | SeñalVal',
 metadesc='Placas de señalética en Valladolid para despachos, puertas, habitaciones y aseos: acero, metacrilato, aluminio y braille. Fabricación e instalación.',
 intro='Las **placas de señalética** son la pieza más numerosa de cualquier edificio. Por eso elegir bien su formato y su material marca la diferencia entre un espacio ordenado y uno que parece improvisado. Además, una placa bien elegida dura años. Así se ahorra en reposiciones.',
 section='''## Placas de señalética que cumplen la normativa
Además del diseño, las placas de señalética de un edificio público deben cumplir la normativa de accesibilidad. En primer lugar, el [Código Técnico de la Edificación]({CTE}) pide pictogramas en altorrelieve en los aseos de uso general. Asimismo, el [Real Decreto 193/2023]({RD193}) refuerza la accesibilidad de los servicios al público.

Por otra parte, en lugares de trabajo, las placas de seguridad siguen el [Real Decreto 485/1997]({RD485}). Así, cada color y cada forma tienen un significado concreto.

Por eso, al encargar placas conviene decidir:
- Primero, qué puertas necesitan información táctil.
- Después, qué nombres van a cambiar con el tiempo.
- Además, qué material encaja con la imagen del edificio.
- Finalmente, cómo se van a fijar para que no se arranquen.

De este modo, las placas de señalética duran años y se actualizan con facilidad. Vea también nuestras [placas en Valladolid](/portfolio/placas/placas-publicitarias-valladolid). Si necesita placas táctiles, vea nuestra guía de [señalética en braille en Valladolid](/senaletica-braille-valladolid).''',
 img2_alt='Placas de señalética: placa de área en aluminio composite con impresión directa'),

'senaletica-salamanca': dict(
 focus='señalética en Salamanca',
 seo_title='Señalética en Salamanca: directorios y placas | SeñalVal',
 metadesc='Señalética en Salamanca: directorios generales y de planta, placas de área y señalización de oficinas en aluminio composite. Un proyecto real.',
 intro='La **señalética en Salamanca** combina dos mundos: un casco histórico protegido y un tejido de oficinas y universidades en crecimiento. Por eso cada proyecto se plantea de forma distinta.',
 section='''## Señalética en Salamanca: normativa y patrimonio
Además del diseño, la señalética en Salamanca debe respetar dos tipos de normas. Por un lado, las municipales, que protegen el patrimonio del casco histórico. Por otro lado, las estatales, como el [Código Técnico de la Edificación]({CTE}), que regula accesibilidad y evacuación.

Asimismo, los edificios de servicios al público deben cumplir el [Real Decreto 193/2023]({RD193}) de accesibilidad. Por consiguiente, las placas táctiles y el contraste adecuado son imprescindibles en oficinas de atención.

Así abordamos un proyecto de señalética en Salamanca:
- Primero, visita y consulta de la ordenanza si hay fachada.
- Después, diseño con la identidad del cliente.
- A continuación, fabricación en aluminio composite u otro material.
- Finalmente, instalación con equipo propio desde Valladolid.

De este modo, el resultado es útil, legal y respetuoso con el entorno. Además, el mismo equipo atiende las reposiciones. Vea el proyecto completo de [directorios en Salamanca](/senaletica-realizada-en-aluminio-composite-con-impresion-directa-para-un-cliente-de-salamanca).''',
 img2_alt='Señalética en Salamanca: placa banderola de área en aluminio composite'),

'senaletica-palencia-estacion-autobuses': dict(
 focus='señalética en Palencia',
 seo_title='Señalética en Palencia: estación de autobuses | SeñalVal',
 metadesc='Señalética en Palencia: rótulos y cajones luminosos para la estación de autobuses y soluciones para empresas, comercios y organismos de la provincia.',
 intro='La **señalética en Palencia** tiene en la estación de autobuses uno de sus proyectos más visibles. Además, es un buen ejemplo de cómo orientar a mucha gente en poco tiempo.',
 section='''## Señalética en Palencia: seguridad y normativa
Además de orientar, la señalética en Palencia debe cumplir la normativa de seguridad. En primer lugar, los edificios con público siguen el [Código Técnico de la Edificación]({CTE}) en evacuación y accesibilidad. Asimismo, los equipos contra incendios se señalizan según el [RIPCI]({RIPCI}).

Por otra parte, en estaciones y edificios públicos la contratación sigue la [Ley de Contratos del Sector Público]({LCSP}). Por consiguiente, la documentación técnica tiene que estar lista desde la oferta.

Así trabajamos la señalética en Palencia:
- Primero, estudio de los recorridos del público.
- Después, diseño de mensajes cortos y pictogramas claros.
- A continuación, fabricación de rótulos y cajones luminosos.
- Finalmente, instalación sin interrumpir el servicio.

De este modo, viajeros, clientes y personal se orientan sin esfuerzo. Además, Palencia está a menos de una hora de nuestro taller. Vea también los [rótulos de la estación de autobuses de Palencia](/rotulos-de-la-estacion-de-autobuses-de-palencia).''',
 img2_alt='Señalética en Palencia: cajón luminoso de dársena en la estación de autobuses'),

'senaletica-hospitales-centros-de-salud': dict(
 focus='señalética para hospitales',
 seo_title='Señalética para hospitales y centros de salud | SeñalVal',
 metadesc='Señalética para hospitales y centros de salud: recorridos, códigos de color, accesibilidad, materiales higiénicos y mantenimiento por fases.',
 intro='La **señalética para hospitales** tiene que funcionar bajo presión: pacientes nerviosos, familias que buscan una habitación y personal con prisa. Por eso cada detalle cuenta. Además, un buen sistema reduce las preguntas en admisión. Así, el personal gana tiempo para lo importante.',
 section='''## Señalética para hospitales: normativa de accesibilidad y evacuación
Además de orientar, la señalética para hospitales debe cumplir normas exigentes. En primer lugar, el [Código Técnico de la Edificación]({CTE}) regula la accesibilidad y la evacuación de los edificios sanitarios. Asimismo, el [Real Decreto 193/2023]({RD193}) refuerza la accesibilidad de los servicios al público.

Por otra parte, las zonas técnicas y de trabajo aplican el [Real Decreto 485/1997]({RD485}) de señalización de seguridad. Así, laboratorios, almacenes y cuartos técnicos señalizan sus riesgos.

Por eso, un proyecto completo de señalética para hospitales incluye:
- Primero, la orientación de pacientes y visitas.
- Después, la señalización accesible con braille y contraste.
- Además, la evacuación y los equipos contra incendios.
- Finalmente, la seguridad en zonas de personal.

De este modo, el centro gana en eficiencia y en seguridad. Además, un sistema modular facilita los cambios constantes de servicios. Vea ejemplos en [señalización hospitalaria](/senalizacion-hospitalaria).''',
 img2_alt='Señalética para hospitales: señalización interior de un botiquín'),

'senaletica-residencias-mayores-valladolid': dict(
 focus='señalética para residencias de mayores',
 seo_title='Señalética para residencias de mayores | SeñalVal',
 metadesc='Señalética para residencias de mayores en Valladolid: iconos grandes, colores por zonas, placas accesibles y materiales fáciles de limpiar.',
 intro='La **señalética para residencias de mayores** no es solo informativa: además, ayuda a los residentes a moverse con autonomía y da tranquilidad a las familias. Por eso merece un diseño específico.',
 section='''## Señalética para residencias de mayores: accesibilidad
Además de ser cálida, la señalética para residencias de mayores debe cumplir la normativa. En primer lugar, el [Código Técnico de la Edificación]({CTE}) exige señalizar los aseos accesibles y los recorridos de evacuación. Asimismo, el [Real Decreto Legislativo 1/2013]({RDL1}) establece la accesibilidad universal como principio.

Por otra parte, las residencias son centros de trabajo para su personal. Por consiguiente, las zonas de servicio aplican el [Real Decreto 485/1997]({RD485}) de señalización de seguridad.

Así diseñamos la señalética para residencias de mayores:
- Primero, iconos grandes y figurativos junto al texto.
- Después, colores por plantas o zonas.
- Además, placas táctiles en aseos y zonas comunes.
- Finalmente, materiales lisos y resistentes a la desinfección.

De este modo, residentes, familias y personal se orientan sin esfuerzo. Además, todo queda documentado para futuros cambios. Vea más proyectos de [señalética para residencias en Valladolid](/senaletica-para-residencias).''',
 img2_alt='Señalética para residencias de mayores: señal de sala de estar'),
}
for _v in EXTRAS_A.values():
    _v['section'] = _v['section'].format(CTE=CTE, RD485=RD485, LOPD=LOPD, LCSP=LCSP, RIPCI=RIPCI, RD193=RD193, RDL1=RDL1, RD171=RD171, CTEWEB=CTEWEB, AEPD=AEPD, INSST=INSST)
