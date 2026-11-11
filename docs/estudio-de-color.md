# Estudio de color · SeñalVal

## A quién le hablamos
Quien contrata un proyecto de señalización de alta exigencia no compra por impulso: **compara, justifica y responde de su elección**.

| Perfil | Qué busca al entrar en la web | Qué le transmite el color |
|---|---|---|
| Técnico de la Administración / órgano de contratación (justicia, sanidad, consejerías) | Solvencia, cumplimiento, documentación para el pliego | Sobriedad y seriedad institucional; nada de colores "comerciales" |
| Jefe de obra o de compras de constructora (Dragados, Vías…) | Un subcontratista que cumpla plazos y no dé problemas | Orden, precisión, fiabilidad técnica |
| Responsable de instalaciones / facility manager (Clece, residencias, oficinas) | Que funcione, que sea fácil y que esté disponible después | Claridad y limpieza: espacios ordenados |
| Dirección de marketing o de marca (Coca-Cola, Toyota, Mahou) | Que su marca quede impecable | Calidad visual, contención, fotos protagonistas |

Lo que tienen en común: **confianza antes que llamar la atención.** La web tiene que parecer la de una empresa que ya trabaja con instituciones, porque es así.

## Por qué blanco, azul noche y azul SeñalVal
- **Azul.** Es el color más asociado a la confianza, la seguridad y la competencia técnica, y el que usan la Administración y las grandes ingenierías y constructoras. Además, **es el color del logo de SeñalVal**: la web y la marca se refuerzan entre sí.
- **Azul noche en lugar de negro puro.** El negro puro resulta duro y "de moda". Un negro azulado (#0D1526) conserva la elegancia y el contraste, pero se ve más institucional y casa con el índigo del logo.
- **Mucho blanco.** Transmite orden y transparencia, que es justo lo que se espera de quien diseña sistemas de orientación. También deja que las fotos de los proyectos sean las protagonistas.
- **Un único color de acción.** Todos los botones son del mismo azul. El visitante entiende sin pensar dónde pulsar: menos dudas, más contactos.
- **Sin rojos, naranjas ni amarillos** en la interfaz: se asocian a ofertas, urgencia o avisos, y restan seriedad. El verde solo aparece en el icono de WhatsApp, porque ayuda a reconocerlo.

## Paleta
| Uso | Color | Hex | Contraste |
|---|---|---|---|
| Acción: botones y enlaces | Azul SeñalVal | `#0B5CAD` | 6,7:1 sobre blanco (AA) |
| Acción al pasar el ratón | Azul profundo | `#094D92` | — |
| Detalles sobre fondo oscuro | Azul cielo (logo) | `#6FA8DC` | 7,2:1 sobre azul noche (AAA) |
| Apoyo de marca | Índigo (logo) | `#3C4F86` | 7,9:1 sobre blanco |
| Fondos oscuros: portada, sectores, pie | Azul noche | `#0D1526` | blanco encima: 18:1 |
| Texto principal | Tinta | `#0B0F19` | 19:1 sobre blanco |
| Texto secundario | Gris pizarra | `#5B6475` | 6:1 sobre blanco (AA) |
| Fondos claros alternos | Gris niebla | `#F3F6FA` | — |
| Líneas y bordes | Gris línea | `#E3E8EF` | — |
| Fondo principal | Blanco | `#FFFFFF` | — |

Todas las combinaciones de texto cumplen **WCAG 2.1 AA** y la mayoría **AAA**. Es un requisito de accesibilidad que valoran los organismos públicos, y para una empresa que hace señalización accesible, predicar con el ejemplo.

## Ritmo de la página
Las secciones alternan **blanco → azul noche → blanco → gris niebla**. Así se marca el paso de un bloque a otro sin cansar la vista, y las zonas oscuras (portada, sectores, licitaciones, contacto) quedan para los mensajes de más peso.

## Dónde se cambia
Todos los colores están al principio de `css/styles.css` como variables (`--blue`, `--black`, `--ink`…). Si se cambia una, se actualiza toda la web.
