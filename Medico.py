class Medico:
    nombre: str
    apellido: str
    numero_de_registro_medico: int

    def __init__(self, nombre, apellido, numero_de_registro_medico):
        self.nombre = nombre
        self.apellido = apellido
        self.numero_de_registro_medico = numero_de_registro_medico
    
    def get_nombre_completo(self) -> str:
        return f"{self.nombre} {self.apellido}"

    def get_nombre(self) -> str:
        return self.nombre
    
    def set_nombre(self, nombre: str):
        self.nombre = nombre

    def get_apellido(self) -> str:
        return self.apellido
    
    def set_apellido(self, apellido: str):
        self.apellido = apellido

    def get_numero_de_registro_medico(self) -> int:
        return self.numero_de_registro_medico
    
    def set_numero_de_registro_medico(self, numero_de_registro_medico: int):
        self.numero_de_registro_medico = numero_de_registro_medico