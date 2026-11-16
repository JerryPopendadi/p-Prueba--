# -*- coding: utf-8 -*-
from extras_a import EXTRAS_A
from extras_b import EXTRAS_B
EXTRAS = {**EXTRAS_A, **EXTRAS_B}
for _k, _v in EXTRAS.items():
    _v.setdefault('faq_title', 'Preguntas frecuentes sobre ' + _v['focus'])

TITLES = {
 'senaletica-madrid-edificios-publicos-empresas': 'Señalética para edificios en Madrid: sedes públicas y empresas',
 'senaletica-burgos-empresas-residencias': 'Señalética para empresas en Burgos: residencias, industria y comercios',
 'senaletica-castilla-y-leon-provincias': 'Empresa de señalética en Castilla y León: proyectos en las nueve provincias',
 'senaletica-organismos-publicos-valladolid': 'Señalización de edificios públicos en Valladolid: qué tener en cuenta',
 'placas-senaletica-valladolid': 'Placas de señalética para puertas y despachos: tipos y materiales',
 'senaletica-residencias-mayores-valladolid': 'Señalética para residencias de mayores: guía práctica',
 'senaletica-braille-valladolid': 'Placas en braille: cómo deben ser y qué exige la normativa',
 'senaletica-lamas-slatz-sistema-modular': 'Sistema modular de señalética: lamas Slatz que se actualizan en minutos',
 'senaletica-especial-valladolid': 'Señalética a medida: soluciones únicas para espacios especiales',
 'licitacion-publica-senalizacion-como-preparar-oferta': 'Licitación pública de señalización: cómo preparar una oferta ganadora',
 'carteles-videovigilancia-normativa': 'Cartel de zona videovigilada: qué exige la normativa y cómo debe ser',
}
for _k, _t in TITLES.items():
    EXTRAS[_k]['title'] = _t
