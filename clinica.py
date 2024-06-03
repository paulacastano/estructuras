from medico import Medico
from pacientes_tda import PacientesTDA
from planeador_de_citas import PlaneadorDeCitas

"""
    Representa una clínica que contiene una lista de pacientes, una lista de médicos y un planeador de citas.
"""
class Clinica:
    pacientes: PacientesTDA #Una colección de pacientes registrados en la clínica
    medicos: list[Medico] #Una lista de instancias de la clase Medico, representan los médicos que trabajan en la clínica
    planeador_de_citas: PlaneadorDeCitas = None #Instancia de PlaneadorDeCitas para gestionar la programación de cita
    
    def __init__(self, lista_de_medicos): # Constructor que incializa una nueva instancia de la clase Clinica.
        self.pacientes = PacientesTDA()
        self.medicos = lista_de_medicos
        self.planeador_de_citas = PlaneadorDeCitas(lista_de_medicos)


    def agregar_paciente(self, nombre, apellido, birth_date, tipo_de_documento, documento_de_identidad):
        '''
        Este metodo agrega un nuevo paciente a la clínica, unicamente sino existe un paciente con el mismo documento de identidad.
        O levanta una excepcion si ya existe un paciente con el mismo documento de identidad en la clinica.
        '''
        paciente = self.pacientes.obtener_paciente(documento_de_identidad) #Busca si ya existe un paciente con el mismo documento de identidad
        if paciente: #Si el paciente ya existe, levanta una excepción
            raise Exception('El paciente ya existe')
        
        self.pacientes.agregar_paciente(nombre, apellido, birth_date, tipo_de_documento, documento_de_identidad) #Si el paciente no existe, agrega el nuevo paciente a la colección de pacientes
    
    def consultar_paciente(self, documento): #Metodo que consulta la información de un paciente en la clínica utilizando su documento de identidad
        return self.pacientes.obtener_paciente(documento) #Retorno la instancia del paciente correspondiente al documento de identidad proporcionado o None si el paciente no existe.

    def obtener_medico(self, registro) -> Medico: #Este metodo se utiliza para buscar y retornar un médico de la clínica usando su número de registro médico como criterio de búsqueda.
        for medico in self.medicos: #Itera sobre la lista de médicos
            if medico.get_numero_de_registro_medico() == registro: #Compara el número de registro de cada médico con el número de registro proporcionado
                return medico #Retorna el médico si encuentra una coincidencia
        return None #Si no se encuentra ningún médico con el número de registro proporcionado, retorna None
    
    def asignar_cita(self, fecha, documento_paciente, registro_medico):
        '''
        Este metodo asigna una cita para un paciente con un médico en la fecha especificada.
        O levanta una Exception: Si el paciente o el medico no estan registrados en la clínica.
        '''
        
        paciente = self.pacientes.obtener_paciente(documento_paciente) #Obtener el paciente con el documento proporcionado
        if not paciente: ## Si el paciente no está registrado, levantar una excepción
            raise Exception("Paciente no registrado")
        
        medico = self.obtener_medico(registro_medico) #Obtener el médico con el registro médico proporcionado
        if not medico: #Si el médico no está registrado, levantar una excepción
            raise Exception("El medico no se encuentra registrado")
        
        return self.planeador_de_citas.asignar_cita(fecha, medico, paciente) #Asigna la cita utilizando el planeador_de_citas y retornar el resultado

    def eliminar_paciente(self, documento):

        '''
        Este método elimina un paciente de la clínica utilizando su número de documento de identidad
        Recibe como parámetros el número de documento de identidad del paciente que se desea eliminar
        Levanta una Exception si el paciente no existe.
        '''
        paciente = self.pacientes.obtener_paciente(documento) #Obtener el paciente con el documento proporcionado
        if not paciente: #Si el paciente no existe, levantar una excepción
            raise Exception('El paciente no existe')
        
        try: # Intentar cancelar la cita del paciente, si existe alguna
            self.planeador_de_citas.cancelar_cita(paciente)
        except Exception: #Si levanta la excepcion de que el paciente  no tiene cita asignada, simplemente lo ignoramos
            pass
        self.pacientes.eliminar_paciente(paciente) #Elimina al paciente de la lista de pacientes
    
    def cancelar_cita(self, documento):
        '''
        Este método cancela la cita de un paciente en la clínica utilizando su número de documento de identidad.
        Recibe como parametro el documento de identidad del paciente.
        Levanta una Exception si el paciente no existe.
        '''
        paciente = self.pacientes.obtener_paciente(documento) #Obtener el paciente con el documento proporcionado
        if not paciente: #Si el paciente no existe, levanta una excepción
            raise Exception("El paciente no existe")
        
        self.planeador_de_citas.cancelar_cita(paciente) #Cancelar la cita del paciente utilizando el planeador_de_citas
    
    def consultar_cita_por_documento(self, documento: str):
        '''
        Este método consulta la cita actual de un paciente en la clínica utilizando su número de documento de identidad.
        Recibe como parámetros el documento de iidentidad del paciente que se desea consultar
        Retorna la cita actual del paciente.
        O levanta una Exception si el paciente no existe o si el paciente no tiene un historial médico.
        '''

        paciente = self.pacientes.obtener_paciente(documento) #Obtiene el paciente con el documento proporcionado
        if not paciente: #Si el paciente no existe, levanta una excepción
            raise Exception("El paciente no existe")
        
        historial_paciente = self.planeador_de_citas.get_historial_de_paciente(documento) #Obtener el historial médico del paciente
        if not historial_paciente: #Si el paciente no tiene historial médico, levanta una excepción
            raise Exception("El paciente aun no tiene un historial medico")
        
        return historial_paciente.cita_actual #Retornar la cita actual del paciente desde su historial médico