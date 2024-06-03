from cita import Cita
from paciente import Paciente


class HistorialDePaciente:

    '''
    Esta clase representa el historial médico de un paciente en la clínica,
    incluyendo su historial de citas y la cita actual, si la tiene.
    '''
    paciente: Paciente = None #El paciente asociado con este historial
    historial_de_citas: list[Cita] = [] #Lista de citas anteriores del paciente
    cita_actual: Cita = None # La cita actual del paciente, si la tiene

    def __init__(self, paciente):
        '''
        Constructor que inicializa una nueva instancia del historial médico de un paciente,
        y que recibe como parametro al paciente asociado con este historial
        '''
        self.paciente = paciente

    def __str__(self):

        '''
        Retorna una representación en cadena del historial médico del paciente.
        Muestra el historial de citas del paciente.
        '''
        print(f"Historial de {self.paciente.nombre}")
        for cita in self.historial_de_citas:
            print(cita)

    def asignar_cita(self, cita):
        '''
        Metodo que asigna una cita al paciente.
        Recibe como parámetros cita (Cita): La cita que se asignará al paciente.
        Levanta una excepción si el paciente ya tiene una cita asignada.
        '''
        if self.cita_actual:
            raise Exception('Ya tienes una cita asignada')
        self.cita_actual = cita
     
    def cancelar_cita(self):

        '''
        Metodo que cancela la cita actual del paciente en el historial médico.
        '''
        if not self.cita_actual: #Verifica si el paciente tiene una cita asignada
            raise Exception('No tienes una cita asignada')
        self.cita_actual = None #Cancela la cita actual
    
    def archivar_cita(self):
        '''
        Este método archiva la cita actual del paciente en el historial de citas y la elimina de la cita actual.
        Levanta una Exception si el paciente no tiene una cita asignada.
        '''
        if self.cita_actual: #Verifica si el paciente tiene una cita asignada
            self.historial_de_citas.append(self.cita_actual) #Si hay una cita asignada, la agrega al historial de citas
            self.cita_actual = None #Elimina la cita actual del paciente
        else: #Si no hay una cita asignada, levanta una excepción
            raise Exception('No tienes una cita asignada')
