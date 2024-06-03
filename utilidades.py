import os
import re
from datetime import datetime

def es_valida_la_fecha_de_programacion(fecha_programacion):
    '''
    Este método verifica si fecha de programación es válida.

    Parámetros:
    fecha_programacion (str): La fecha y hora de la cita en formato "yyyy-mm-dd HH:MM".

    Lanza una excepción si:
    - El formato de la fecha no es válido.
    - La hora no está en el rango de 7 AM a 12 PM o si los minutos no son '00'.

    '''
    if not re.match("^[0-9]{4}-[0-9]{2}-[0-9]{2} [0-9]{2}:[0-9]{2}$", fecha_programacion): #Verifica que el formato de la fecha sea "yyyy-mm-dd HH:MM"
        raise Exception('Formato de fecha no valido')

    horas = int(fecha_programacion[11:13]) #Extrae las horas de la cadena de fecha
    minutos = fecha_programacion[14:] #Extrae los minutos de la cadena de fecha

    if (horas < 7 or horas > 12) or minutos != '00': #Verifica que la hora esté entre las 7 AM y las 12 PM y que los minutos sean '00'
        raise Exception('Horario de fecha no valido')
    
def es_valida_la_fecha_de_nacimiento(fecha_naciemiento):

    '''
    Este método verifica que la fecha de nacimiento sea válida.

    Parámetros:
    fecha_naciemiento (str): La fecha de nacimiento en formato "yyyy-mm-dd".

    Lanza una excepción si:
    - El formato de la fecha no es válido.
    - La fecha de nacimiento es una fecha futura.
    '''
    if not re.match("^[0-9]{4}-[0-9]{2}-[0-9]{2}$", fecha_naciemiento): #Verifica que el formato de la fecha sea "yyyy-mm-dd"
        raise Exception('Formato de fecha no valido')

    now = datetime.now() #Obtiene la fecha y hora actual
    fecha_referencia = datetime.strptime(fecha_naciemiento, '%Y-%m-%d') #Convierte la cadena de fecha de nacimiento en un objeto datetime
    if fecha_referencia > now: #Verifica que la fecha de nacimiento no sea una fecha futura
        raise Exception('Fecha de nacimiento no puede ser en el futuro')


def es_valido_el_tipo_de_documento(tipo_de_documento):
    
    '''
    Este método verifica que el tipo de documento sea válido.

    Parámetros:
    tipo_de_documento (str): El tipo de documento, que debe ser uno de los siguientes: 'cc', 'ti', 'pp'.

    Lanza una excepción si:
    El tipo de documento no es válido.
    '''
    if not tipo_de_documento in ['cc','ti','pp']: #Verifica que el tipo de documento sea 'cc', 'ti' o 'pp'
        raise Exception('Tipo de documento no valido')

def es_valido_el_numero_de_documento(documento):

    '''
    Este método verifica que el número de documento sea válido.

    Parámetros:
    El número de documento que debe cumplir con las siguientes reglas:
    1. No puede estar vacío.
    2. No puede empezar por '0'.

    Lanza una excepción si:
    - El documento está vacío.
    - El documento empieza por '0'.
    '''
    if len(documento) == 0:
        raise Exception('El documento no puede estar vacio')
    
    if documento[0] == '0':
        raise Exception('El documento no puede empezar por 0')

def clear_console(): #Este método limpia la consola de acuerdo al sistema operativo.
    # For Windows
    if os.name == 'nt':
        _ = os.system('cls')
    # For Unix/Linux/Mac
    else:
        _ = os.system('clear')