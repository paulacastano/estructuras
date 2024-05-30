from medico import Medico
from pacientes_tda import PacientesTDA
from planeador_de_citas import PlaneadorDeCitas

class Clinica:
    pacientes: PacientesTDA
    medicos: list[Medico]
    planeador_de_citas: PlaneadorDeCitas = None
    
    def __init__(self, lista_de_medicos):
        self.pacientes = PacientesTDA()
        self.medicos = lista_de_medicos
        self.planeador_de_citas = PlaneadorDeCitas(lista_de_medicos)


    def agregar_paciente(self, nombre, apellido, birth_date, tipo_de_documento, documento_de_identidad):
        paciente = self.pacientes.obtener_paciente(documento_de_identidad)
        if paciente:
            raise Exception('El paciente ya existe')
        
        self.pacientes.agregar_paciente(nombre, apellido, birth_date, tipo_de_documento, documento_de_identidad)
    
    def consultar_paciente(self, documento):
        return self.pacientes.obtener_paciente(documento)

    def obtener_medico(self, registro) -> Medico:
        for medico in self.medicos:
            if medico.get_numero_de_registro_medico() == registro:
                return medico
        return None
    
    def asignar_cita(self, fecha, documento_paciente, registro_medico):
        paciente = self.pacientes.obtener_paciente(documento_paciente)
        if not paciente:
            raise Exception("Paciente no registrado")
        
        medico = self.obtener_medico(registro_medico)
        if not medico:
            raise Exception("El medico no se encuentra registrado")
        
        return self.planeador_de_citas.asignar_cita(fecha, medico, paciente)

    def eliminar_paciente(self, documento):
        paciente = self.pacientes.obtener_paciente(documento)
        if not paciente:
            raise Exception('El paciente no existe')
        
        try:
            self.planeador_de_citas.cancelar_cita(paciente)
        except Exception:
            pass
        self.pacientes.eliminar_paciente(paciente)
    
    def cancelar_cita(self, documento):
        paciente = self.pacientes.obtener_paciente(documento)
        if not paciente:
            raise Exception("El paciente no existe")
        
        self.planeador_de_citas.cancelar_cita(paciente)
    
    def consultar_cita_por_documento(self, documento: str):
        paciente = self.pacientes.obtener_paciente(documento)
        if not paciente:
            raise Exception("El paciente no existe")
        
        historial_paciente = self.planeador_de_citas.get_historial_de_paciente(documento)
        if not historial_paciente:
            raise Exception("El paciente aun no tiene un historial medico")
        
        return historial_paciente.cita_actual