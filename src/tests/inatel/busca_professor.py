'''
Contém a classe de teste de BuscaProfessor.
'''

import unittest
from src.main.inatel.busca_professor import BuscaProfessor
from src.tests.inatel.mock.professor_service import MockProfessorService


class TesteBuscaProfessor(unittest.TestCase):
    '''
    Classe de teste de BuscaProfessor.
    '''

    def setUp(self):
        professor_service = MockProfessorService()
        self.busca_professor = BuscaProfessor(professor_service)

    def teste_busca_professor_chris(self):
        '''
        Testa a busca do professor Chris.
        '''
        chris = self.busca_professor.busca_professor(1)
        self.assertEqual("Chris", chris.get_nome())
        self.assertEqual("15:30", chris.get_horario_atendimento())
        self.assertEqual("Integral", chris.get_periodo())

    def teste_busca_professor_marcelo(self):
        '''
        Testa a busca do professor Marcelo.
        '''
        marcelo = self.busca_professor.busca_professor(2)
        self.assertEqual("Marcelo", marcelo.get_nome())
        self.assertEqual("13:30", marcelo.get_horario_atendimento())
        self.assertEqual("Noturno", marcelo.get_periodo())

    def teste_busca_professor_renzo(self):
        '''
        Testa a busca do professor RenZo.
        '''
        renzo = self.busca_professor.busca_professor(3)
        self.assertEqual("RenZo", renzo.get_nome())
        self.assertEqual("17:30", renzo.get_horario_atendimento())
        self.assertEqual("Integral", renzo.get_periodo())

    def teste_busca_professor_padrao(self):
        '''
        Testa a busca do professor padrão.
        '''
        padrao = self.busca_professor.busca_professor(-1)
        self.assertEqual("Guilherme", padrao.get_nome())
        self.assertEqual("17:30", padrao.get_horario_atendimento())
        self.assertEqual("Integral", padrao.get_periodo())

    def teste_busca_professor_valido(self):
        '''
        Testa a verificação da existência de um professor.
        '''
        professor_valido = self.busca_professor.verifica_professor_existe(1)
        self.assertTrue(professor_valido)

    def teste_busca_professor_invalido(self):
        '''
        Testa a verificação da não-existência de um professor.
        '''
        professor_invalido = self.busca_professor.verifica_professor_existe(-1)
        self.assertFalse(professor_invalido)
