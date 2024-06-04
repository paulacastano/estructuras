# tests/test_cita.py

import unittest
from datetime import datetime
from cita import Cita
from medico import Medico
from paciente import Paciente

class TestCita(unittest.TestCase):
    
    def setUp(self):
        # Configurar un médico y un paciente para las pruebas
        self.medico = Medico("Juan", "Lopez", "12345678", "Cardiología")
        self.paciente = Paciente("Maria", "Gonzalez", "1980-01-01", "cc", "98765432")
        self.fecha_programacion_valida = "2024-06-01 08:00"
    
    def test_creacion_cita(self):
        # Verificar que se puede crear una cita correctamente
        cita = Cita(self.fecha_programacion_valida, self.medico, self.paciente)
        self.assertEqual(cita.fecha_programacion, self.fecha_programacion_valida)
        self.assertEqual(cita.medico, self.medico)
        self.assertEqual(cita.paciente, self.paciente)

if __name__ == '__main__':
    unittest.main()