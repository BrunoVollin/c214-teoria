"""
Contains the tests for the inatel.busca_professor module.
"""

import unittest
from src.main.inatel.busca_professor import BuscaProfessor
from src.tests.inatel.mock.professor_service import MockProfessorService


class TesteBuscaProfessor(unittest.TestCase):
    """
    Test cases for the inatel.busca_professor module.
    """

    def setUp(self):
        professor_service = MockProfessorService()
        self.busca_professor = BuscaProfessor(professor_service)

    def teste_busca_professor_chris(self):
        """
        Tests if the professor Chris is found.
        """
        professor = self.busca_professor.busca_professor(0)
        self.assertEqual("Chris", professor.get_nome())
        self.assertEqual("15:30", professor.get_horario_atendimento())
        self.assertEqual("Integral", professor.get_periodo())

    def teste_busca_professor_marcelo(self):
        """
        Tests if the professor Marcelo is found.
        """
        professor = self.busca_professor.busca_professor(1)
        self.assertEqual("Marcelo", professor.get_nome())
        self.assertEqual("13:30", professor.get_horario_atendimento())
        self.assertEqual("Noturno", professor.get_periodo())

    def teste_busca_professor_renzo(self):
        """
        Tests if the professor RenZo is found.
        """
        professor = self.busca_professor.busca_professor(2)
        self.assertEqual("RenZo", professor.get_nome())
        self.assertEqual("17:30", professor.get_horario_atendimento())
        self.assertEqual("Integral", professor.get_periodo())

    def teste_busca_professor_invalido(self):
        """
        Tests if an exception is raised a the professor is not found.
        """
        with self.assertRaises(ValueError):
            self.busca_professor.busca_professor(-1)

    def teste_busca_professor_campos_nao_vazios(self):
        """
        Tests if not a single field is blank.
        """
        for num in range(0, 3):
            professor = self.busca_professor.busca_professor(num)
            self.assertNotEqual("", professor.get_nome())
            self.assertNotEqual("", professor.get_horario_atendimento())
            self.assertNotEqual("", professor.get_periodo())

    def teste_verifica_professor_existente(self):
        """
        Tests if a professor exists.
        """
        for num in range(0, 3):
            prof_exists = self.busca_professor.verifica_professor_existe(num)
            self.assertTrue(prof_exists)

    def teste_verifica_professor_inexistente(self):
        """
        Tests if a professor does not exist.
        """
        prof_exists = self.busca_professor.verifica_professor_existe(-1)
        self.assertFalse(prof_exists)
