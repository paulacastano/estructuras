from paciente import Paciente
# from medico import Medico
# from planeador_de_citas import PlaneadorDeCitas

# paula = Paciente("Paula", "Castano", "2005-04-03", "CC", "123456789")
# camila = Paciente("Camila", "Restrepo", "2005-04-03", "CC", "10923545")
# sebastian = Paciente("Sebastian", "Martinez", "2005-04-03", "CC", "10923546")
# laura = Paciente("Laura", "Gomez", "1995-04-03", "CC", "10923547")

# carlos = Medico("Carlos", "Teyes", "234")
# luis = Medico("Luis", "Arango", "425")

# edad = paula.get_age()
# tipo_de_paciente = paula.get_tipo_de_paciente()

# planeador_de_citas = PlaneadorDeCitas([carlos, luis])

# try:
#     planeador_de_citas.asignar_cita("2024-06-01 07:00", "210", carlos, paula)
#     planeador_de_citas.asignar_cita("2024-06-01 08:00", "210", carlos, sebastian)
#     planeador_de_citas.asignar_cita("2024-06-01 09:00", "210", carlos, camila)
#     planeador_de_citas.cancelar_cita(paula)
#     planeador_de_citas.asignar_cita("2024-06-01 08:00", "210", luis, paula)
#     planeador_de_citas.asignar_cita("2024-06-01 07:00", "210", luis, laura)
# except Exception as e:
#     print(f"No pude asignar tu cita por: {e}")


# for cita in planeador_de_citas.citas:
#     print(cita)


def cmp(paciente_uno: Paciente, paciente_dos: Paciente):
    if paciente_uno.get_nombre_completo() < paciente_dos.get_nombre_completo():
        return True
    if paciente_uno.get_nombre_completo() == paciente_dos.get_nombre_completo():
        if paciente_uno.get_documento_de_identidad() < paciente_dos.get_documento_de_identidad():
            return True
    return False


def merge_sort(pacientes: list[Paciente]):
    if len(pacientes) > 1:
        # Encontrando la mitad de la lista de pacientes
        mid = len(pacientes) // 2

        # Dividiendo la lista por la mitad en dos partes
        left_half = pacientes[:mid]
        right_half = pacientes[mid:]

        # Llamado recursivo para ordenar el lado izquierdo
        merge_sort(left_half)

        # Llamado recursivo para ordenar el lado derecho
        merge_sort(right_half)

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

# Test the merge_sort function
if __name__ == "__main__":
    paula = Paciente("Paula", "Castano", "2005-04-03", "CC", "123456789")
    camila = Paciente("Camila", "Restrepo", "2005-04-03", "CC", "10923545")
    sebastian = Paciente("Sebastian", "Martinez", "2005-04-03", "CC", "10923546")
    laura = Paciente("Laura", "Gomez", "1995-04-03", "CC", "10923547")
    stiven = Paciente("Stiven", "Cardona", "1995-04-03", "CC", "10923543")
    pau = Paciente("Paula", "Cardona", "1995-04-03", "CC", "10923549")
    paulita = Paciente("Paula", "Castano", "1995-04-03", "CC", "10923548")
    arr = [paula, camila, laura, sebastian, stiven, pau, paulita]
    print("Given array is")
    for paciente in arr:
        print(paciente)
    merge_sort(arr)
    print("Sorted array is")
    for paciente in arr:
        print(paciente)
