from datetime import datetime

from cita import Cita
from historial_paciente import HistorialDePaciente
from medico import Medico
from paciente import Paciente
from utilidades import es_valida_la_fecha_de_programacion

class PlaneadorDeCitas:
    citas: list[Cita] = []
    historial_de_pacientes: dict[str, HistorialDePaciente] = {}
    gestion_de_medicos: dict[str,dict[str, Cita]] = {}

    def __init__(self, medicos: list[Medico]) -> None:
        for medico in medicos:
            self.gestion_de_medicos[medico.get_numero_de_registro_medico()] = {}
    
    def cmp(self, cita_uno: Cita, cita_dos: Cita):
        fecha_cita_uno = datetime.strptime(cita_uno.fecha_programacion, "%Y-%m-%d %H:%M")
        fecha_cita_dos = datetime.strptime(cita_dos.fecha_programacion, "%Y-%m-%d %H:%M")
        if fecha_cita_uno < fecha_cita_dos:
            return 1
        if fecha_cita_uno == fecha_cita_dos:
            return 0
        return -1
    
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
    
    def upper_bound(self, cita: Cita) -> int:
        lo = 0
        hi = len(self.citas)
        while hi - lo > 1:
            mid = (lo + hi) // 2
            if cmp(self.citas[mid], cita) >= 0:
                lo = mid
            else:
                hi = mid
        return hi
    
    def archivar_citas(self):
        now = datetime.now()

        while len(self.citas) > 0 and now > datetime.strptime(self.citas[0].fecha_programacion, "%Y-%m-%d %H:%M"):
            paciente = self.citas[0].paciente
            historial_del_paciente = self.historial_de_citas.get(paciente.documento_de_identidad, None)
            historial_del_paciente.archivar_cita()            
            self.citas.pop(0)
            
    def cancelar_cita(self, paciente: Paciente):
        historial_del_paciente = self.historial_de_pacientes[paciente.documento_de_identidad]
        if not historial_del_paciente.cita_actual:
            raise Exception('No tienes una cita asignada')
        
        cita = historial_del_paciente.cita_actual

        medico = cita.medico
        fecha = cita.fecha_programacion
        historial_del_paciente.cancelar_cita()
        self.gestion_de_medicos[medico.get_numero_de_registro_medico()][fecha] = None
        self.citas.remove(cita)

    def get_historial_de_paciente(self, documento_de_identidad: str):
        return self.historial_de_pacientes.get(documento_de_identidad, None)

    def asignar_cita(self, fecha, medico: Medico, paciente: Paciente) -> Cita:
        es_valida_la_fecha_de_programacion(fecha)
        self.archivar_citas()
        now = datetime.now()
        
        if now > datetime.strptime(fecha, "%Y-%m-%d %H:%M"):
            raise Exception('No puedes programar una cita en el pasado')
        
        agenda_medico = self.gestion_de_medicos[medico.get_numero_de_registro_medico()]
        if fecha in agenda_medico and agenda_medico[fecha] != None:
            raise Exception('El medico ya tiene una cita asignada a esa hora')
        
        if paciente.documento_de_identidad not in self.historial_de_pacientes:
            self.historial_de_pacientes[paciente.documento_de_identidad] = HistorialDePaciente(paciente)
        
        historial_del_paciente = self.historial_de_pacientes[paciente.documento_de_identidad]
        if historial_del_paciente.cita_actual:
            raise Exception('Ya tienes una cita asignada')

        nueva_cita = Cita(fecha, medico, paciente)
        
        left = self.lower_bound(nueva_cita)
        right = self.upper_bound(nueva_cita)
        
        if right - left >= len(self.gestion_de_medicos.keys()):
            raise Exception('No hay disponibilidad de citas')

        historial_del_paciente.asignar_cita(nueva_cita)
        agenda_medico[fecha] = nueva_cita

        if len(self.citas) and self.cmp(nueva_cita, self.citas[0]) == 1:
            self.citas = [nueva_cita] + self.citas
        elif len(self.citas) and self.cmp(nueva_cita, self.citas[-1]) == -1:
            self.citas = self.citas + [nueva_cita]
        else: 
            self.citas = self.citas[:right] + [nueva_cita] + self.citas[right:]

        return nueva_cita