'''
Contém a classe BuscaProfessor, que realiza operações de busca e retorna dados dos professores.
'''

import json
from src.main.inatel.professor_service import ProfessorService
from src.main.inatel.professor import Professor

class BuscaProfessor():
    '''
    Classe com funções de busca de um professor no banco de dados.
    '''

    def __init__(self, professor_service: ProfessorService):
        self.professor_service = professor_service

    def busca_professor(self, id_num: int) -> Professor:
        '''
        Busca um professor pelo seu id e retorna um objeto Professor.
        '''
        professor_json = self.professor_service.busca(id_num)
        objeto_json = json.loads(professor_json)

        return Professor(objeto_json['nomeDoProfessor'],
                         objeto_json['horarioDeAtendimento'],
                         objeto_json['periodo'])

    def verifica_professor_existe(self, id_num: int) -> bool:
        '''
        Verifica se determinado professor existe e retorna um booleano.
        '''
        return self.professor_service.professor_existe(id_num)
