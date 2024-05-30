import re

def es_valida_la_fecha_de_programacion(fecha_programacion):
    if not re.match("^[0-9]{4}-[0-9]{2}-[0-9]{2} [0-9]{2}:[0-9]{2}$", fecha_programacion):
        raise Exception('Formato de fecha no valido')
    
def es_valida_la_fecha_de_nacimiento(fecha_programacion):
    if not re.match("^[0-9]{4}-[0-9]{2}-[0-9]{2}$", fecha_programacion):
        raise Exception('Formato de fecha no valido')

def es_valido_el_tipo_de_documento(tipo_de_documento):
    if not tipo_de_documento in ['cc','ti','pp']:
        raise Exception('Tipo de documento no valido')