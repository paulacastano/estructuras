from datetime import datetime
from Medico import Medico


class Clinica:
    def __init__(self):
        self.pacientes = []
        self.citas = []
        self.medicos = {}

    def agregar_paciente(self, paciente):
        self.pacientes.append(paciente)

    def obtener_paciente(self, documento):
        for paciente in self.pacientes:
            if paciente.documento_de_identidad == documento:
                return paciente
        return None

    def actualizar_paciente(self, documento, nuevos_datos):
        paciente = self.obtener_paciente(documento)
        if paciente:
            paciente.nombre = nuevos_datos.get('nombre', paciente.nombre)
            paciente.apellido = nuevos_datos.get('apellido', paciente.apellido)
            paciente.birth_date = nuevos_datos.get('birth_date', paciente.birth_date)
            paciente.edad = paciente.get_age(paciente.birth_date)
            paciente.tipo_de_paciente = paciente.get_tipo_de_paciente(paciente.edad)
            paciente.documento_de_identidad = paciente.get_documento_de_identidad(paciente.edad)
            return True
        return False

    def eliminar_paciente(self, documento):
        paciente = self.obtener_paciente(documento)
        if paciente:
            self.pacientes.remove(paciente)
            return True
        return False

    def programar_cita(self, cita):
        paciente = self.obtener_paciente(cita.paciente.documento_de_identidad)
        if paciente and not paciente.turno_asignado:
            self.citas.append(cita)
            paciente.turno_asignado = cita
            return True
        return False

    def cancelar_cita(self, documento):
        paciente = self.obtener_paciente(documento)
        if paciente and paciente.turno_asignado:
            cita = paciente.turno_asignado
            cita.estado = EstadoCita.DISPONIBLE
            paciente.turno_asignado = None
            return True
        return False

    def agregar_medico(self, nombre, horarios):
        self.medicos[nombre] = horarios

    def disponibilidad_medico(self, nombre, fecha, hora):
        if nombre in self.medicos:
            return (fecha, hora) in self.medicos[nombre]
        return False

    def ordenar_citas_por_fecha(self):
        def get_key(cita):
            return datetime.strptime(cita.fecha_programacion + ' ' + cita.hora_asignacion, "%Y-%m-%d %H:%M")
        
        self.citas.sort(key=get_key)

    def buscar_cita(self, fecha, hora):
        def get_key(cita):
            return datetime.strptime(cita.fecha_programacion + ' ' + cita.hora_asignacion, "%Y-%m-%d %H:%M")
        
        def binary_search(arr, x):
            l = 0
            r = len(arr) - 1
            while l <= r:
                mid = l + (r - l) // 2
                mid_date = get_key(arr[mid])
                x_date = datetime.strptime(x, "%Y-%m-%d %H:%M")
                if mid_date == x_date:
                    return arr[mid]
                elif mid_date < x_date:
                    l = mid + 1
                else:
                    r = mid - 1
            return None
        
        self.ordenar_citas_por_fecha()
        cita_buscada = binary_search(self.citas, f"{fecha} {hora}")
        return cita_buscada
