import os
from medico import Medico
from clinica import Clinica
from paciente import Paciente

def clear_console():
    # For Windows
    if os.name == 'nt':
        _ = os.system('cls')
    # For Unix/Linux/Mac
    else:
        _ = os.system('clear')
        

if __name__ == "__main__":
    carlos = Medico("Carlos", "Teyes", "234")
    luis = Medico("Luis", "Arango", "425")
    clinica = Clinica([carlos, luis])
    while True:
        menu = f'''
            ----------------------------------------
            > Bienvenid@ al centro medico El Avila <
            > 1. Agregar paciente                  <
            > 2. Salir                             <
            ----------------------------------------
        '''
        print(menu)
        opcion_seleccionada = input("Seleccione una opcion: ")
        clear_console()
        if opcion_seleccionada == '1':
            f'''
            -------------------------------------------------
            > A continuacion agregue los datos del paciente <
            -------------------------------------------------
            '''
            nombre = input("Ingrese el nombre: ")
            apellido = input("Ingrese el apellido: ")
            fecha_de_nacimiento = input("Ingrese la fecha de nacimiento con el formato (yyyy-mm-dd): ")
            tipo_de_documento = input("Ingrese el tipo de documento: ")
            numero_de_documento = input("Ingrese el numero de documento: ")
            clear_console()
            try:
                clinica.agregar_paciente(nombre, apellido, fecha_de_nacimiento, tipo_de_documento, numero_de_documento)
            except Exception as e:
                print(f"El paciente no se pudo crear por: {e}")
                input("Presione la tecla ENTER para continuar")
                clear_console()
            

        if opcion_seleccionada != '1':
            break
