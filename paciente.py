from datetime import datetime

from utilidades import es_valida_la_fecha_de_nacimiento, es_valido_el_tipo_de_documento

class Paciente:
    '''
    Clase que representa a un Paciente de la clinica y que recibe como atributos:
    El nombre del paciente
    El apellido del paciente
    La fecha de nacimiento del paciente
    El tipo de documento de identidad del paciente
    El documento de identidad del paciente
    '''    
    nombre: str
    apellido: str
    fecha_de_nacimiento: str
    tipo_de_documento: str
    documento_de_identidad: str

    def __init__(self, nombre, apellido, fecha_de_nacimiento, tipo_de_documento, documento_de_identidad):
        '''
        Constructor que inicializa una nueva instancia de la clase Paciente
        '''
        es_valida_la_fecha_de_nacimiento(fecha_de_nacimiento) #Verifica si la fecha de nacimiento es válida
        es_valido_el_tipo_de_documento(tipo_de_documento)#Verifica si el tipo de documento es valido 
        self.nombre = nombre
        self.apellido = apellido
        self.fecha_de_nacimiento = fecha_de_nacimiento
        self.documento_de_identidad = documento_de_identidad
        self.tipo_de_documento = tipo_de_documento
    
    def __str__(self): # Metodo que especifica como se debera verse el objeto al coonvertirlo en una cadena
        return f'''
        -------------------------[Informacion del paciente]----------------------------
        > Nombre: {self.get_nombre_completo()}
        > Documento: {self.get_tipo_de_documento()} ({self.get_documento_de_identidad()})
        > Edad: {self.get_age()}
        > Fecha de nacimiento: {self.get_fecha_de_nacimiento()}
        -------------------------------------------------------------------------------
        '''
    
    def compare_month_day(self, date_one, date_two):

        '''
        Metodo que compara 2 fechas
        date_one (tuple): Un tupla que representa la primera fecha
        date_two (tuple): Una tupla que representa la segunda fecha 

        '''
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

        '''
        Metodo que calcula la edad del Paciente segun su fecha de nacimiento y retorna
        la edad del paciente en años
        '''
        current_date = datetime.now() # Se obtiene la fecha actual
        fecha_de_nacimiento = datetime.strptime(self.fecha_de_nacimiento, "%Y-%m-%d") # Se convierte la fecha de nacimiento del paciente a un objeto datetime
        edad = (current_date.year - fecha_de_nacimiento.year) - self.compare_month_day((fecha_de_nacimiento.month, fecha_de_nacimiento.day), (current_date.month, current_date.day)) # Calcula la diferencia de años entre la fecha actual y la fecha de nacimiento
        return edad # Retorna la edad del paciente
     
    def get_tipo_de_paciente(self):

        '''
        Metodo que determina el tipo de paciente en base a su edad.
        Retorna el tipo de paciente como una cadena de caracteres
        '''
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

  
  