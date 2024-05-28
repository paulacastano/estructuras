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

    def obtener_paciente(self, documento) -> Paciente:
        for paciente in self.pacientes:
            if paciente.documento_de_identidad == documento:
                return paciente
        return None

    def actualizar_paciente(self, documento, nuevos_datos: dict):
        paciente = self.obtener_paciente(documento)
        if not paciente:
            raise Exception('El paciente no existe')
        
        paciente.nombre = nuevos_datos.get('nombre', paciente.nombre)
        paciente.apellido = nuevos_datos.get('apellido', paciente.apellido)
        paciente.fecha_de_nacimiento = nuevos_datos.get('birth_date', paciente.fecha_de_nacimiento)

    def eliminar_paciente(self, documento):
        paciente = self.obtener_paciente(documento)
        if not paciente:
            raise Exception('El paciente no existe')
        
        self.pacientes.remove(paciente)
        

    # def programar_cita(self, cita):
    #     paciente = self.obtener_paciente(cita.paciente.documento_de_identidad)
    #     if paciente and not paciente.turno_asignado:
    #         self.citas.append(cita)
    #         paciente.turno_asignado = cita
    #         return True
    #     return False

    # def cancelar_cita(self, documento):
    #     paciente = self.obtener_paciente(documento)
    #     if paciente and paciente.turno_asignado:
    #         cita = paciente.turno_asignado
    #         cita.estado = EstadoCita.DISPONIBLE
    #         paciente.turno_asignado = None
    #         return True
    #     return False

    # def agregar_medico(self, nombre, horarios):
    #     self.medicos[nombre] = horarios

    # def disponibilidad_medico(self, nombre, fecha, hora):
    #     if nombre in self.medicos:
    #         return (fecha, hora) in self.medicos[nombre]
    #     return False

    # def ordenar_citas_por_fecha(self):
    #     def get_key(cita):
    #         return datetime.strptime(cita.fecha_programacion + ' ' + cita.hora_asignacion, "%Y-%m-%d %H:%M")
        
    #     self.citas.sort(key=get_key)

    # def buscar_cita(self, fecha, hora):
    #     def get_key(cita):
    #         return datetime.strptime(cita.fecha_programacion + ' ' + cita.hora_asignacion, "%Y-%m-%d %H:%M")
        
    #     def binary_search(arr, x):
    #         l = 0
    #         r = len(arr) - 1
    #         while l <= r:
    #             mid = l + (r - l) // 2
    #             mid_date = get_key(arr[mid])
    #             x_date = datetime.strptime(x, "%Y-%m-%d %H:%M")
    #             if mid_date == x_date:
    #                 return arr[mid]
    #             elif mid_date < x_date:
    #                 l = mid + 1
    #             else:
    #                 r = mid - 1
    #         return None
        
    #     self.ordenar_citas_por_fecha()
    #     cita_buscada = binary_search(self.citas, f"{fecha} {hora}")
    #     return cita_buscada