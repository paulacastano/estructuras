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
    nombre: str
    apellido: str
    documento_de_identidad: TipoDeDocumento
    birth_date: str
    edad:int
    historial_de_citas: list[Cita]
    turno_asignado: Cita
    tipo_de_paciente: TipoDePaciente

def __init__(birth_date):
    self.birth_date = birth_date

def compare_month_day(date_one, date_two): # (month, day), (month, day)
    if date_one[0] > date_two[0]:
        return True
    if date_one[0] == date_two[0]:
        if date_one[1] > date_two[1]:
            return True
    return False
        

def get_age(birth_date):
    current_date = datetime.now()
    birth_date = datetime.strptime(birth_date,"%Y-%m-%d")
    edad = (current_date.year - birth_date.year) - compare_month_day((birth_date.month, birth_date.day), (current_date.month, current_date.day)) # si y solo si 


class Main:
    
    paciente_one = Paciente("2005-04-03")
    dane = paciente_one.

    

  