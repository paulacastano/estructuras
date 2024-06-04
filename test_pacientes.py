# tests/test_paciente.py

import unittest
from paciente import Paciente

class TestPaciente(unittest.TestCase):
    
    def test_get_tipo_de_paciente(self):
        # Paciente neonato
        paciente_neonato = Paciente("Bebe", "RecienNacido", "2023-12-01", "cc", "12345678")
        self.assertEqual(paciente_neonato.get_tipo_de_paciente(), "neonato")

        # Paciente infante
        paciente_infante = Paciente("Nino", "Pequeno", "2015-06-01", "ti", "87654321")
        self.assertEqual(paciente_infante.get_tipo_de_paciente(), "infante")

        # Paciente joven
        paciente_joven = Paciente("Adolescente", "Joven", "2010-01-01", "cc", "56789012")
        self.assertEqual(paciente_joven.get_tipo_de_paciente(), "joven")

        # Paciente joven_adulto
        paciente_joven_adulto = Paciente("Joven", "Adulto", "1990-01-01", "pp", "09876543")
        self.assertEqual(paciente_joven_adulto.get_tipo_de_paciente(), "joven_adulto")

        # Paciente adulto
        paciente_adulto = Paciente("Adulto", "Mayor", "1980-01-01", "cc", "11223344")
        self.assertEqual(paciente_adulto.get_tipo_de_paciente(), "adulto")

        # Paciente adulto_mayor
        paciente_adulto_mayor = Paciente("Anciano", "Mayor", "1950-01-01", "ti", "44332211")
        self.assertEqual(paciente_adulto_mayor.get_tipo_de_paciente(), "adulto_mayor")

if __name__ == '__main__':
 unittest.main()
