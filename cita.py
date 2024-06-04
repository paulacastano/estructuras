from datetime import datetime
from medico import Medico
from paciente import Paciente
from utilidades import es_valida_la_fecha_de_programacion

class Cita:
    fecha_solicitud: str #Fecha en la que se solicita la cita, formato: yyyy-mm-dd
    fecha_programacion: str #Fecha y hora en la que se programa la cita, formato: yyyy-mm-dd HH:MM
    paciente: Paciente = None #Instancia de la clase Paciente, representa al paciente que solicita la cita
    medico: Medico = None # Instancia de la clase Medico, representa al médico que atenderá la cita

    def __init__(self, fecha_programacion, medico, paciente): #Inicializa una nueva instancia de la clase Cita.
        es_valida_la_fecha_de_programacion(fecha_programacion) ## Verifica si la fecha de programación es válida
        self.fecha_solicitud = datetime.now().strftime("%Y-%m-%d %H:%M") #Asigna la fecha actual como fecha de solicitud, en el formato yyyy-mm-dd HH:MM
        self.fecha_programacion = fecha_programacion # Asigna la fecha y hora en la que se programa la cita
        self.medico = medico #Asigna la instancia del médico que atendera la cita
        self.paciente = paciente # Asigna la instancia del paciente que solicita la cita

    def __str__(self):  # Metodo que especifica como debera verse el objeto al convertirlo en una cadena
        return f'''
        -------------------------[Informacion de la cita]----------------------------
        > Fecha: {self.fecha_programacion}
        > Medico: {self.medico.get_nombre_completo()} ({self.medico.get_numero_de_registro_medico()})
        > Paciente: {self.paciente.get_nombre_completo()} ({self.paciente.get_documento_de_identidad()})
        > Solicitada el: {self.fecha_solicitud}
        > Consultorio: {self.medico.get_consultorio()}
        -----------------------------------------------------------------------------
        '''