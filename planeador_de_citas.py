from datetime import datetime

from cita import Cita
from historial_paciente import HistorialDePaciente
from medico import Medico
from paciente import Paciente
from utilidades import es_valida_la_fecha_de_programacion


class PlaneadorDeCitas:

    '''
    Esta clase se encarga de manejar la logica de la asignacion de citas y la agenda de los medicos.
    Tiene como atributos:
    La lista que contendrá todas las citas médicas ordenadas.
    Un diccionario que mapea los números de documento de identidad de los pacientes a sus historiales médicos.
    Otro diccionario que mapea los números de registro médico de los médicos a las citas que tienen programadas.
    '''
    citas: list[Cita] = [] #Tendra todas las citas ordenadas 
    historial_de_pacientes: dict[str, HistorialDePaciente] = {} 
    gestion_de_medicos: dict[str,dict[str, Cita]] = {}

    def __init__(self, medicos: list[Medico]) -> None:

        '''
        Este es el constructor de la clase PlaneadorDeCitas.
        Se encarga de inicializar la gestión de médicos con un diccionario vacío para cada médico.
        Y recibe como parametos: Una lista de objetos Medico
        '''
        for medico in medicos: #Itera sobre la lista de médicos
            self.gestion_de_medicos[medico.get_numero_de_registro_medico()] = {} #Crea una entrada vacía en el diccionario gestion_de_medicos para cada médico
    
    def cmp(self, cita_uno: Cita, cita_dos: Cita):

        '''
        Este metodo se encarga de comparar dos citas basandose en sus fechas de programación.
        Recibe como parametros:
        La primera cita a comparar.
        La segunda cita a comparar.

        Retorna:
        - 1 si la fecha de programación de la primera cita es posterior a la de la segunda cita.
        - 0 si las fechas de programación de ambas citas son iguales.
        - -1 si la fecha de programación de la primera cita es anterior a la de la segunda cita.
        '''
        fecha_cita_uno = datetime.strptime(cita_uno.fecha_programacion, "%Y-%m-%d %H:%M") #Convierte las fechas de programación de las citas en objetos datetime
        fecha_cita_dos = datetime.strptime(cita_dos.fecha_programacion, "%Y-%m-%d %H:%M")
        if fecha_cita_uno < fecha_cita_dos: #Compara las fechas de programación de las citas
            return 1
        if fecha_cita_uno == fecha_cita_dos:
            return 0
        return -1
    
    #Busqueda binaria para encontrar donde esta la primera aparicion de una cita con fechas de programacion iguales (no misma cita)
    def lower_bound(self, cita: Cita) -> int:
        lo = 0
        hi = len(self.citas)
        while hi - lo > 1:
            mid = (lo + hi) // 2
            if self.cmp(self.citas[mid], cita) == 1:
                lo = mid
            else:
                hi = mid
        return lo
    
    #Busqueda binaria para encontrar donde esta la ultima aparicion de una cita con fechas de programacion iguales (no misma cita)
    def upper_bound(self, cita: Cita) -> int:
        lo = 0
        hi = len(self.citas)
        while hi - lo > 1:
            mid = (lo + hi) // 2
            if self.cmp(self.citas[mid], cita) >= 0:
                lo = mid
            else:
                hi = mid
        return hi
    
    def archivar_citas(self):

        '''
        Este metodo se encarga de archivar las citas que ya han pasado según la fecha actual.
        '''
        now = datetime.now()

        while len(self.citas) > 0 and now > datetime.strptime(self.citas[0].fecha_programacion, "%Y-%m-%d %H:%M"): #Mientras haya citas en la lista y la fecha actual sea mayor que la fecha de programación de la primera cita
            paciente = self.citas[0].paciente #Obtiene el paciente de la primera cita
            historial_del_paciente = self.historial_de_pacientes.get(paciente.documento_de_identidad, None) #Obtiene el historial del paciente, si existe
            historial_del_paciente.archivar_cita() # Archiva la cita en el historial del paciente           
            self.citas.pop(0) #Eliminar la cita de la lista de citas
            
    def cancelar_cita(self, paciente: Paciente):

        '''
        Este metodo cancela la cita actual de un paciente 
        Y recibe como parametro el paciente al cual se le desea cancelar la cita
        '''
        historial_del_paciente = self.historial_de_pacientes[paciente.documento_de_identidad] #Obtiene el historial del paciente
        if not historial_del_paciente.cita_actual: #Verificar si el paciente tiene una cita asignada
            raise Exception('No tienes una cita asignada')
        
        cita = historial_del_paciente.cita_actual #Obtiene la cita actual del historial del paciente

        medico = cita.medico # Se obtiene al medico de la cita
        fecha = cita.fecha_programacion #Se obtiene la fecha de la cita 
        historial_del_paciente.cancelar_cita() #Se cancela la cita en el historial del paciente
        self.gestion_de_medicos[medico.get_numero_de_registro_medico()][fecha] = None #Se Elimina la cita de la gestión de médicos
        self.citas.remove(cita) # Se elimina la cita de la lista de citas
    
    def get_historial_de_paciente(self, documento_de_identidad: str): #Me retorna el historial de un paciente segun el documento de identidad
        return self.historial_de_pacientes.get(documento_de_identidad, None) 

    def asignar_cita(self, fecha, medico: Medico, paciente: Paciente) -> Cita:

        '''
        Este metodo asigna una cita a un paciente con un médico en una fecha específica.
        Recibe como Parámetros:
        La fecha y hora de la cita en formato "yyyy-mm-dd HH:MM".
        El médico que atenderá la cita.
        El paciente que asistirá a la cita.
        Retorna:
        Cita: La cita asignada.
        ''' 

        es_valida_la_fecha_de_programacion(fecha) # Verifica que la fecha de programación sea válida
        self.archivar_citas() #Archiva citas pasadas
        now = datetime.now() # Se obtiene la fecha y hora actual
        
        if now > datetime.strptime(fecha, "%Y-%m-%d %H:%M"): #Verifica que la fecha de la cita no esté en el pasado
            raise Exception('No puedes programar una cita en el pasado')
        
        agenda_medico = self.gestion_de_medicos[medico.get_numero_de_registro_medico()] # Se obtiene la agenda del médico

        if fecha in agenda_medico and agenda_medico[fecha] != None: # Verifica que el médico no tenga otra cita a la misma hora
            raise Exception('El medico ya tiene una cita asignada a esa hora')
        
        if paciente.documento_de_identidad not in self.historial_de_pacientes: #Si el paciente no tiene historial, se crea uno nuevo
            self.historial_de_pacientes[paciente.documento_de_identidad] = HistorialDePaciente(paciente)
        
        historial_del_paciente = self.historial_de_pacientes[paciente.documento_de_identidad] # Se Obtiene el historial del paciente
        if historial_del_paciente.cita_actual: #Si el paciente ya tiene una cita asignada, lanza una excepción
            raise Exception('Ya tienes una cita asignada')

        nueva_cita = Cita(fecha, medico, paciente) #Crea una nueva instancia de Cita
        
        left = self.lower_bound(nueva_cita) #Encuentra la posición inferior donde insertar la nueva cita
        right = self.upper_bound(nueva_cita) #Encuentra la posición superior donde insertar la nueva cita
        
        if right - left >= len(self.gestion_de_medicos.keys()): # Verifica si hay disponibilidad de citas, si no la hay, lanza una excepción
            raise Exception('No hay disponibilidad de citas')

        historial_del_paciente.asignar_cita(nueva_cita) #Asigna la nueva cita al historial del paciente
        agenda_medico[fecha] = nueva_cita #Actualiza la agenda del médico con la nueva cita

        if len(self.citas) and self.cmp(nueva_cita, self.citas[0]) == 1: # Se inserta la nueva cita en la lista de citas ordenadas
            self.citas = [nueva_cita] + self.citas
        elif len(self.citas) and self.cmp(nueva_cita, self.citas[-1]) == -1:
            self.citas = self.citas + [nueva_cita]
        else: 
            self.citas = self.citas[:right] + [nueva_cita] + self.citas[right:]

        return nueva_cita #Devuelve la nueva cita asignada