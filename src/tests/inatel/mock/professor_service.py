'''
Contém a classe mockada de ProfessorService.
'''

from src.main.inatel.professor_service import ProfessorService
from src.tests.inatel.constants.professor import *


class MockProfessorService(ProfessorService):
    '''
    Classe mockada de ProfessorService.
    '''

    def busca(self, id_num: int) -> str:
        '''
        Busca o professor pelo id.
        '''
        if id_num == 1:
            return CHRIS
        if id_num == 2:
            return MARCELO
        if id_num == 3:
            return RENZO
        return PADRAO

    def professor_existe(self, id_num: int) -> bool:
        '''
        Verifica se o professor existe.
        '''
        lista_professores = []
        lista_professores.append(1)
        lista_professores.append(2)
        lista_professores.append(3)
        for professor in lista_professores:
            if professor == id_num:
                return True
        return False
