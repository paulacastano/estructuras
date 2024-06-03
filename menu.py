import os
import csv
from medico import Medico
from clinica import Clinica


def clear_console():
    # For Windows
    if os.name == 'nt':
        _ = os.system('cls')
    # For Unix/Linux/Mac
    else:
        _ = os.system('clear')
        
carlos = Medico("Carlos", "Teyes", "234", "101")
luis = Medico("Luis", "Arango", "425", "102")
milena = Medico("Milena", "Restrepo", "231", "201")
lorena = Medico("Lorena", "Macias", "233", "202")
clinica = Clinica([carlos, luis, milena, lorena])

# Ruta al archivo CSV
ruta_archivo = 'pacientes.csv'

# Abrir y leer el archivo CSV
with open(ruta_archivo, newline='') as archivo_csv:
    lector_csv = csv.reader(archivo_csv)
    for fila in lector_csv:
        (nombre, apellido, fecha_de_nacimiento, tipo_de_documento, documento) = fila
        clinica.agregar_paciente(nombre, apellido, fecha_de_nacimiento, tipo_de_documento, documento)

while True:
    menu = f'''
        ----------------------------------------
        > Bienvenid@ al centro medico El Avila <
        > 1. Agregar paciente                  <
        > 2. Buscar paciente                   <
        > 3. Eliminar paciente                 <
        > 4. Agendar cita                      <
        > 5. Consultar cita actual             <
        > 6. Cancelar cita                     <
        > 7. Salir                             <
        ----------------------------------------
    '''
    print(menu)
    opcion_seleccionada = input("Seleccione una opción: ")
    clear_console()
    if opcion_seleccionada == '1':
        mensaje = f'''
        -------------------------------------------------
        > A continuacion agregue los datos del paciente <
        -------------------------------------------------
        '''
        print(mensaje)
        nombre = input("Ingrese el nombre: ")
        apellido = input("Ingrese el apellido: ")
        fecha_de_nacimiento = input("Ingrese la fecha de nacimiento con el formato (yyyy-mm-dd): ")
        tipo_de_documento = input("Ingrese el tipo de documento: ")
        numero_de_documento = input("Ingrese el numero de documento: ")
        clear_console()
        try:
            clinica.agregar_paciente(nombre, apellido, fecha_de_nacimiento, tipo_de_documento, numero_de_documento)
            print("Paciente agregado con exito 😘")
        except Exception as e:
            print(f"El paciente no se pudo crear por: {e}")
        finally:
            input("Presione la tecla ENTER para continuar")
            clear_console()
        

    elif opcion_seleccionada == '2':
        mensaje = f'''
        ---------------------------------------------------------
        >A continuacion ingrese los datos del paciente a buscar <
        ---------------------------------------------------------
        '''
        print(mensaje)
        documento = input("Ingrese el documento de identidad: ")
        clear_console()
        try:
            paciente = clinica.consultar_paciente(documento)
            if not paciente:
                raise Exception("Paciente no registrado")
            print(paciente)
        except Exception as e: 
            print(e)
        finally:
            input("Presione la tecla ENTER para continuar")
            clear_console()
        

    elif opcion_seleccionada == '3':
        mensaje = f'''
        ---------------------------------------------------
        > Usted se encuentra en el menu: Eliminar paciente <
        ---------------------------------------------------
        '''
        print(mensaje)
        
        documento = input("Ingrese el numero del documento del paciente a eliminar: ")
        clear_console()
        try:
            clinica.eliminar_paciente(documento)
            print("Paciente eliminado con exito")
        except Exception as e:
            print(f"El paciente no pudo ser eliminado por: {e}")
        finally:
            input("Presione la tecla ENTER para continuar")
            clear_console()

    elif opcion_seleccionada == '4':
        mensaje = f'''
        -------------------------------------------------------
        > Usted se encuentra en el menu: Agendar cita
         Nota: Nuestro horario laboral es de 7:00 a 12:00 pm
         seleccione un horario en ese rango                   <
        -------------------------------------------------------
        '''
        print(mensaje)
        documento = input("Ingrese el documento del paciente: ")
        registro = input("Ingrese el registro medico: ")
        fecha = input("Ingrese la fecha de la cita con el formato (yyyy-mm-dd hh:mm): ")
        try:
            cita = clinica.asignar_cita(fecha, documento, registro)
            print("😘 Cita agendada con exito")
        except Exception as e:
            print(f"La cita no pudo ser asignada por: {e}")
        finally:
            input("Presione la tecla ENTER para continuar")
            clear_console()
    elif opcion_seleccionada == '5':
        mensaje = f'''
        ---------------------------------------------------------
        > Usted se encuentra en el menu: Consultar cita actutal <
        ---------------------------------------------------------
        '''
        print(mensaje)
        documento = input("Ingrese el documento del paciente: ")
        try:
            cita = clinica.consultar_cita_por_documento(documento)
            if not cita:
                raise Exception("El paciente no tiene una cita asignada")
            print(cita)
        except Exception as e:
            print(e)
        finally:
            input("Presione la tecla ENTER para continuar")
            clear_console()
    elif opcion_seleccionada == '6':
        mensaje = f'''
        -------------------------------------------------
        > Usted se encuentra en el menu: Cancelar cita  <
        -------------------------------------------------
        '''
        print(mensaje)
        documento = input("Ingrese el documento del paciente: ")
        try:
            clinica.cancelar_cita(documento)
            print("Cita cancelada con exito")
        except Exception as e:
            print(e)
        finally:
            input("Presione la tecla ENTER para continuar")
            clear_console()
    else: 
        break

