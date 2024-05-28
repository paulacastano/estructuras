import re
from datetime import datetime

def es_valida_la_fecha_de_nacimiento(fecha_programacion):
    if not re.match("^[0-9]{4}-[0-9]{2}-[0-9]{2}$", fecha_programacion):
        raise Exception('Formato de fecha no valido')

def es_valido_el_tipo_de_documento(tipo_de_documento):
    if not tipo_de_documento in ['cc','ti','pp']:
        raise Exception('Tipo de documento no valido')

class Paciente:
    nombre: str
    apellido: str
    fecha_de_nacimiento: str
    tipo_de_documento: str
    documento_de_identidad: str

    def __init__(self, nombre, apellido, fecha_de_nacimiento, tipo_de_documento, documento_de_identidad):
        es_valida_la_fecha_de_nacimiento(fecha_de_nacimiento)
        es_valido_el_tipo_de_documento(tipo_de_documento)
        self.nombre = nombre
        self.apellido = apellido
        self.fecha_de_nacimiento = fecha_de_nacimiento
        self.documento_de_identidad = documento_de_identidad
        self.tipo_de_documento = tipo_de_documento
    
    def __str__(self): 
        return f'''
        -------------------------[Informacion de la cita]----------------------------
        > Nombre: {self.get_nombre_completo()}
        > Documento: {self.get_tipo_de_documento()} ({self.get_documento_de_identidad()})
        > Fecha de naciemiento: {self.get_fecha_de_nacimiento()}
        -----------------------------------------------------------------------------
        '''
    
    def compare_month_day(self, date_one, date_two):
        if date_one[0] > date_two[0]:
            return True
        if date_one[0] == date_two[0]:
            if date_one[1] > date_two[1]:
                return True
        return False
    
    def get_nombre_completo(self) -> str:
        return f"{self.nombre} {self.apellido}"

    def get_nombre(self) -> str:
        return self.nombre

    def set_nombre(self, nombre: str):
        self.nombre = nombre
    
    def get_apellido(self) -> str:
        return self.apellido

    def set_apellido(self, apellido: str):
        self.apellido = apellido

    def get_fecha_de_nacimiento(self) -> str:
        return self.fecha_de_nacimiento
    
    def set_fecha_de_nacimiento(self, fecha_de_nacimiento: str):
        self.fecha_de_nacimiento = fecha_de_nacimiento

    def get_tipo_de_documento(self) -> str:
        return self.tipo_de_documento
    
    def set_tipo_de_documento(self, tipo_de_documento: str):
        self.tipo_de_documento = tipo_de_documento

    def get_documento_de_identidad(self) -> str:
        return self.documento_de_identidad
    
    def set_documento_de_identidad(self, documento_de_identidad: str):
        self.documento_de_identidad = documento_de_identidad

    def get_age(self) -> int:
        current_date = datetime.now()
        fecha_de_nacimiento = datetime.strptime(self.fecha_de_nacimiento, "%Y-%m-%d")
        edad = (current_date.year - fecha_de_nacimiento.year) - self.compare_month_day((fecha_de_nacimiento.month, fecha_de_nacimiento.day), (current_date.month, current_date.day))
        return edad
     
    def get_tipo_de_paciente(self):
        edad = self.get_age()
        if edad < 1:
            return "neonato"
        
        if edad < 12:
            return "infante"
        
        if edad < 18:
            return "joven"
        
        if edad < 35:
            return "joven_adulto"
        
        if edad < 65:
            return "adulto"
        
        return "adulto_mayor"

  
  