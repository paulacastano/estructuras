from cita import Cita
from paciente import Paciente


class HistorialDePaciente:
    paciente: Paciente = None
    historial_de_citas: list[Cita] = []
    cita_actual: Cita = None

    def __init__(self, paciente):
        self.paciente = paciente

    def __str__(self):
        print(f"Historial de {self.paciente.nombre}")
        for cita in self.historial_de_citas:
            print(cita)

    def asignar_cita(self, cita):
        if self.cita_actual:
            raise Exception('Ya tienes una cita asignada')
        self.cita_actual = cita
    
    def cancelar_cita(self):
        if not self.cita_actual:
            raise Exception('No tienes una cita asignada')
        self.cita_actual = None
    
    def archivar_cita(self):
        if self.cita_actual:
            self.historial_de_citas.append(self.cita_actual)
            self.cita_actual = None
        else:
            raise Exception('No tienes una cita asignada')
