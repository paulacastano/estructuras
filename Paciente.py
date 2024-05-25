from enum import Enum
from datetime import date, datetime
from Cita import Cita

class TipoDePaciente(Enum):
    NEONATO = "neonato"
    INFANTE = "infate"
    JOVEN = "joven"
    JOVEN_ADULTO = "joven_adulto"
    ADULTO = "adulto"
    ADULTO_MAYOR = "adulto_mayor"

class TipoDeDocumento(Enum):
    TARJETA_DE_IDENTIDAD =  "Tarjeta de Identidad"
    CEDULA_DE_CIUDADANIA = "Cedula de ciudadania"


class Paciente:

    def __init__(self, nombre, apellido, birth_date):
        self.nombre = nombre
        self.apellido = apellido
        self.birth_date = birth_date
        self.edad = self.get_age(birth_date)
        self.tipo_de_paciente = self.get_tipo_de_paciente(self.edad)
        self.documento_de_identidad = self.get_documento_de_identidad(self.edad)
        self.historial_de_citas = []
        self.turno_asignado = None

    def compare_month_day(self, date_one, date_two): # (month, day), (month, day)
        if date_one[0] > date_two[0]:
            return True
        if date_one[0] == date_two[0]:
            if date_one[1] > date_two[1]:
                return True
        return False

    def get_age(self, birth_date):
        current_date = datetime.now()
        birth_date = datetime.strptime(birth_date, "%Y-%m-%d")
        edad = (current_date.year - birth_date.year) - self.compare_month_day((birth_date.month, birth_date.day), (current_date.month, current_date.day))
        return edad
    
    def get_documento_de_identidad(self, edad):
        if edad >= 18:
            return "Cedula de Ciudadania"
        else:
            return "Tarjeta de Identidad"
     
    def get_tipo_de_paciente(self, edad):
        if edad < 1:
            return "Neonato"
        elif edad < 12:
            return "Infante"
        elif edad < 18:
            return "Joven"
        elif edad < 35:
            return "Joven Adulto"
        elif edad < 65:
            return "Adulto"
        else:
            return "Adulto Mayor"


class main:
    paciente_one = Paciente("2005-04-03")
    dane = paciente_one.compare_month_day
    print(dane)


  