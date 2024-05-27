from paciente import Paciente
from medico import Medico
from planeador_de_citas import PlaneadorDeCitas

paula = Paciente("Paula", "Castano", "2005-04-03", "CC", "123456789")
camila = Paciente("Camila", "Restrepo", "2005-04-03", "CC", "10923545")
sebastian = Paciente("Sebastian", "Martinez", "2005-04-03", "CC", "10923546")
laura = Paciente("Laura", "Gomez", "1995-04-03", "CC", "10923547")

carlos = Medico("Carlos", "Teyes", "234")
luis = Medico("Luis", "Arango", "425")

edad = paula.get_age()
tipo_de_paciente = paula.get_tipo_de_paciente()

planeador_de_citas = PlaneadorDeCitas([carlos, luis])

try:
    planeador_de_citas.asignar_cita("2024-06-01 07:00", "210", carlos, paula)
    planeador_de_citas.asignar_cita("2024-06-01 08:00", "210", carlos, sebastian)
    planeador_de_citas.asignar_cita("2024-06-01 09:00", "210", carlos, camila)
    planeador_de_citas.cancelar_cita(paula)
    planeador_de_citas.asignar_cita("2024-06-01 08:00", "210", luis, paula)
    planeador_de_citas.asignar_cita("2024-06-01 07:00", "210", luis, laura)
except Exception as e:
    print(f"No pude asignar tu cita por: {e}")


for cita in planeador_de_citas.citas:
    print(cita)
