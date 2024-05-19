class Cita:
    def __init__(self, fecha_solicitud, fecha_programacion, hora_asignacion, consultorio, medico, paciente):
        self.fecha_solicitud = fecha_solicitud
        self.fecha_programacion = fecha_programacion
        self.hora_asignacion = hora_asignacion
        self.consultorio = consultorio
        self.medico = medico
        self.paciente = paciente
        self.estado = EstadoCita.NO_DISPONIBLE

    def __str__(self):
        return f"Cita: {self.fecha_programacion} {self.hora_asignacion} con {self.medico} para {self.paciente.nombre} {self.paciente.apellido}"