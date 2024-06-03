import re
from datetime import datetime

def es_valida_la_fecha_de_programacion(fecha_programacion):
    if not re.match("^[0-9]{4}-[0-9]{2}-[0-9]{2} [0-9]{2}:[0-9]{2}$", fecha_programacion):
        raise Exception('Formato de fecha no valido')

    horas = int(fecha_programacion[11:13])
    minutos = fecha_programacion[14:]

    if (horas < 7 or horas > 12) or minutos != '00':
        raise Exception('Horario de fecha no valido')
    
def es_valida_la_fecha_de_nacimiento(fecha_naciemiento):
    if not re.match("^[0-9]{4}-[0-9]{2}-[0-9]{2}$", fecha_naciemiento):
        raise Exception('Formato de fecha no valido')

    now = datetime.now()
    fecha_referencia = datetime.strptime(fecha_naciemiento, '%Y-%m-%d')
    if fecha_referencia > now:
        raise Exception('Fecha de nacimiento no puede ser en el futuro')


def es_valido_el_tipo_de_documento(tipo_de_documento):
    if not tipo_de_documento in ['cc','ti','pp']:
        raise Exception('Tipo de documento no valido')

def es_valido_el_numero_de_documento(documento):
    if len(documento) == 0:
        raise Exception('El documento no puede estar vacio')
    
    if documento[0] == '0':
        raise Exception('El documento no puede empezar por 0')
