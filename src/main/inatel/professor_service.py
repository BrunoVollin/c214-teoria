'''
Contém a classe ProfessorService, que comunica com o banco de dados e retorna dados dos professores.
'''

from abc import abstractmethod


class ProfessorService():
    '''
    Classe que representa a camada de serviço de professores. Será mockada.
    '''

    @abstractmethod
    def busca(self, id_num: int) -> str:
        '''
        Método abstrato de busca de um professor. Será mockado.
        '''

    @abstractmethod
    def professor_existe(self, id_num: int) -> bool:
        '''
        Método abstrato para verificar a existência de um professor. Será mockado.
        '''
