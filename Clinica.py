from medico import Medico
from paciente import Paciente
from planeador_de_citas import PlaneadorDeCitas

def cmp(paciente_uno: Paciente, paciente_dos: Paciente):
    if paciente_uno.get_nombre_completo() < paciente_dos.get_nombre_completo():
        return True
    if paciente_uno.get_nombre_completo() == paciente_dos.get_nombre_completo():
        if paciente_uno.get_documento_de_identidad() < paciente_dos.get_documento_de_identidad():
            return True
    return False

class Clinica:
    pacientes: list[Paciente]
    medicos: list[Medico]
    planeador_de_citas: PlaneadorDeCitas = None
    
    def __init__(self, lista_de_medicos):
        self.pacientes = []
        self.medicos = lista_de_medicos
        self.planeador_de_citas = PlaneadorDeCitas(lista_de_medicos)

    def merge_sort(self, pacientes: list[Paciente]):
        if len(pacientes) > 1:
            # Encontrando la mitad de la lista de pacientes
            mid = len(pacientes) // 2

            # Dividiendo la lista por la mitad en dos partes
            left_half = pacientes[:mid]
            right_half = pacientes[mid:]

            # Llamado recursivo para ordenar el lado izquierdo
            self.merge_sort(left_half)

            # Llamado recursivo para ordenar el lado derecho
            self.merge_sort(right_half)

            i = j = k = 0

            # Copiando los datos en listas temporales que se llaman left_half[] y right_half[]
            while i < len(left_half) and j < len(right_half):
                if cmp(left_half[i], right_half[j]):
                    pacientes[k] = left_half[i]
                    i += 1
                else:
                    pacientes[k] = right_half[j]
                    j += 1
                k += 1

            # termina de copiar los que hacen falta
            while i < len(left_half):
                pacientes[k] = left_half[i]
                i += 1
                k += 1

            while j < len(right_half):
                pacientes[k] = right_half[j]
                j += 1
                k += 1

    def agregar_paciente(self, nombre, apellido, birth_date, tipo_de_documento, documento_de_identidad):
        paciente = self.obtener_paciente(documento_de_identidad)
        if paciente:
            raise Exception('El paciente ya existe')
        
        paciente = Paciente(nombre, apellido, birth_date, tipo_de_documento, documento_de_identidad)
        self.pacientes.append(paciente)
    
    def obtener_medico(self, registro) -> Medico:
        for medico in self.medicos:
            if medico.get_numero_de_registro_medico() == registro:
                return medico
        return None

    def obtener_paciente(self, documento) -> Paciente:
        for paciente in self.pacientes:
            if paciente.documento_de_identidad == documento:
                return paciente
        return None
    
    def asignar_cita(self, fecha, documento_paciente, registro_medico):
        paciente = self.obtener_paciente(documento_paciente)
        if not paciente:
            raise Exception("Paciente no registrado")
        
        medico = self.obtener_medico(registro_medico)
        if not medico:
            raise Exception("El medico no se encuentra registrado")
        
        return self.planeador_de_citas.asignar_cita(fecha, medico, paciente)

    def eliminar_paciente(self, documento):
        paciente = self.obtener_paciente(documento)
        if not paciente:
            raise Exception('El paciente no existe')
        
        try:
            self.planeador_de_citas.cancelar_cita(paciente)
        except Exception:
            pass
        self.pacientes.remove(paciente)
    
    def cancelar_cita(self, documento):
        paciente = self.obtener_paciente(documento)
        if not paciente:
            raise Exception("El paciente no existe")
        
        self.planeador_de_citas.cancelar_cita(paciente)
    
    def consultar_cita_por_documento(self, documento: str):
        paciente = self.obtener_paciente(documento)
        if not paciente:
            raise Exception("El paciente no existe")
        
        historial_paciente = self.planeador_de_citas.get_historial_de_paciente(documento)
        if not historial_paciente:
            raise Exception("El paciente aun no tiene un historial medico")
        
        return historial_paciente.cita_actual