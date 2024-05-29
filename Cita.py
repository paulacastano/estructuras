import re

from datetime import datetime
from medico import Medico
from paciente import Paciente

'''
Esta funcion valida ...

'''
def es_valida_la_fecha_de_programacion(fecha_programacion):
    if not re.match("^[0-9]{4}-[0-9]{2}-[0-9]{2} [0-9]{2}:[0-9]{2}$", fecha_programacion):
        raise Exception('Formato de fecha no valido')

class Cita:
    fecha_solicitud: str # yyyy-mm-dd
    fecha_programacion: str # yyyy-mm-dd HH:MM
    paciente: Paciente = None
    medico: Medico = None

    def __init__(self, fecha_programacion, medico, paciente):
        es_valida_la_fecha_de_programacion(fecha_programacion)
        self.fecha_solicitud = datetime.now().strftime("%Y-%m-%d %H:%M")
        self.fecha_programacion = fecha_programacion
        self.medico = medico
        self.paciente = paciente

    def __str__(self): 
        return f'''
        -------------------------[Informacion de la cita]----------------------------
        > Fecha: {self.fecha_programacion}
        > Medico: {self.medico.get_nombre_completo()} ({self.medico.get_numero_de_registro_medico()})
        > Paciente: {self.paciente.get_nombre_completo()} ({self.paciente.get_documento_de_identidad()})
        > Solicitada el: {self.fecha_solicitud}
        > Consultorio: {self.medico.get_consultorio()}
        -----------------------------------------------------------------------------
        '''