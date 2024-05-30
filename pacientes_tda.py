from paciente import Paciente

class PacientesTDA:
    pacientes: list[Paciente]
    
    def __init__(self):
        self.pacientes = []

    def agregar_paciente(self, nombre, apellido, birth_date, tipo_de_documento, documento_de_identidad):
        paciente = Paciente(nombre, apellido, birth_date, tipo_de_documento, documento_de_identidad)
        self.pacientes.append(paciente)
        self.merge_sort(self.pacientes)
    
    def obtener_paciente(self, documento: str) -> Paciente:
        return self.binary_search(documento)

    def binary_search(self, documento):
        if len(self.pacientes) == 0:
            return None
        
        hi = len(self.pacientes) - 1
        lo = 0
        while hi - lo > 1:
            mid = (hi + lo) // 2
            if self.pacientes[mid].get_documento_de_identidad() < documento:
                lo = mid
            else:
                hi = mid
            
        if self.pacientes[hi].get_documento_de_identidad() == documento:
            return self.pacientes[hi]
        
        return None
    
    def eliminar_paciente(self, paciente: Paciente):
        self.pacientes.remove(paciente)

    def cmp(self, paciente_uno: Paciente, paciente_dos: Paciente):
        if paciente_uno.get_documento_de_identidad() < paciente_dos.get_documento_de_identidad():
            return True
        return False
    
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
                if self.cmp(left_half[i], right_half[j]):
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