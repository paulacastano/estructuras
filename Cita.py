from datetime import datetime
from Medico import Medico

class Cita:
    fecha_de_solicitud: datetime
    fecha_de_programacion: datetime
    numero_de_consultorio: str
    medico_asignado: Medico
    paciente_asignado = None



print("hola")