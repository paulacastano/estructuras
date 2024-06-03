from paciente import Paciente
from utilidades import es_valido_el_numero_de_documento

class PacientesTDA:
    '''
    Clase que representa una estructura de datos para almacenar pacientes.Y tiene como atributo
    una lista que contiene objetos de la clase Paciente.
    '''
    pacientes: list[Paciente]
    
    def __init__(self): #Contructor que inicializa una nueva instancia de la clase TDA vacia (sin pacientes)
        self.pacientes = [] #Este atributo almacenará objetos de la clase Paciente que se agreguen a la estructura de datos.

    def agregar_paciente(self, nombre, apellido, birth_date, tipo_de_documento, documento_de_identidad):
        '''
        Este metodo se utiliza para agregar un nuevo paciente a la lista de pacientes de la clase PacientesTDA
        '''
        es_valido_el_numero_de_documento(documento_de_identidad) #Primero verifica si el número de documento es válido
        paciente = Paciente(nombre, apellido, birth_date, tipo_de_documento, documento_de_identidad) #Crea un nuevo objeto de la clase Paciente con la información proporcionada
        self.pacientes.append(paciente) #Agrega el paciente a la lista de pacientes
        self.merge_sort(self.pacientes) ## Llama al método merge_sort para ordenar la lista de pacientes
    
    def obtener_paciente(self, documento: str) -> Paciente:
        '''
        Este metodo busca un paciente en la lista de pacientes utilizando una búsqueda binaria.
        Recibe como parametros:
        documento (str): El número de documento de identidad del paciente a buscar.
        Y retorna el objeto Paciente correspondiente al documento proporcionado, o None si no se encuentra.
        '''
        return self.binary_search(documento) #Llama al método binary_search para buscar el paciente por su numero de documento

    def binary_search(self, documento):

        '''
        Este metodo realiza una búsqueda binaria en la lista de pacientes para encontrar un paciente con un número de documento específico.
        Recibe como parámetros:
        El documento (str): El número de documento de identidad del paciente a buscar.
        Y Retorna:
        El objeto Paciente correspondiente al documento proporcionado, o None si no se encuentra.
        '''
        if len(self.pacientes) == 0: #Verifica si la lista de pacientes está vacía
            return None
        
        hi = len(self.pacientes) - 1 #Inicializa los índices de inicio (lo) y fin (hi) para la búsqueda binaria
        lo = 0
        while hi - lo > 1: #Realiza la búsqueda binaria
            mid = (hi + lo) // 2
            if self.pacientes[mid].get_documento_de_identidad() < documento: ## Compara el número de documento de identidad del paciente en el índice medio con el documento buscado
                lo = mid
            else:
                hi = mid

        if self.pacientes[hi].get_documento_de_identidad() == documento: #Verifica si se encontro el paciente con el documento buscado
            return self.pacientes[hi]
        elif self.pacientes[lo].get_documento_de_identidad() == documento:
            return self.pacientes[lo]
        
        return None #Retorna None si el paciente no se encontró
    
    def eliminar_paciente(self, paciente: Paciente):

        '''
        Elimina un paciente de la lista de pacientes.
        Recibe como parámetros:
        El objeto Paciente que se desea eliminar de la lista.
        '''
        self.pacientes.remove(paciente) #Utiliza el metodo remove para eliminar el paciente de la lista

    def cmp(self, paciente_uno: Paciente, paciente_dos: Paciente):

        '''
        Este metodo Compara dos pacientes basándose en sus números de documento de identidad.
        Recibe como parametros:
        El primer paciente a comparar.
        El segundo paciente a comparar.

        Retorna:
        True si el número de documento de identidad del primer paciente es menor que el del segundo paciente, False de lo contrario
        '''
        if paciente_uno.get_documento_de_identidad() < paciente_dos.get_documento_de_identidad(): # Compara los números de documento de identidad de los pacientes
            return True
        return False # Retorna False si el número de documento de identidad del primer paciente no es menor que el del segundo paciente
    
    def merge_sort(self, pacientes: list[Paciente]):

        '''
        Este metodo merge_sort implementa el algoritmo de ordenamiento Merge Sort para ordenar una lista de pacientes. 
        Y recibe como parametros:
        La lista de pacientes que se ordenara.
        '''
        #Verifica si la lista tiene más de un elemento
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

            #Indices para recorrer los subarreglos y la lista original
            i = j = k = 0

            #Combina los subarreglos ordenados en un solo arreglo ordenado
            while i < len(left_half) and j < len(right_half):
                if self.cmp(left_half[i], right_half[j]):
                    pacientes[k] = left_half[i]
                    i += 1
                else:
                    pacientes[k] = right_half[j]
                    j += 1
                k += 1

            #Copia los elementos restantes de left_half
            while i < len(left_half):
                pacientes[k] = left_half[i]
                i += 1
                k += 1

            #Copia los elementos restantes de right_half
            while j < len(right_half):
                pacientes[k] = right_half[j]
                j += 1
                k += 1