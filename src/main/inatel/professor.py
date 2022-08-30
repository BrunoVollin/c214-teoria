'''
Contém uma classe Professor, representando um professor.
'''


class Professor():
    '''
    Classe representando um professor, com nome, horário de atendimento e período.
    '''

    def __init__(self, nome: str, horario_atendimento: str, periodo: str):
        self.__nome = nome
        self.__horario_atendimento = horario_atendimento
        self.__periodo = periodo

    def get_nome(self) -> str:
        '''
        Retorna o nome do professor.
        '''
        return self.__nome

    def set_nome(self, nome: str) -> None:
        '''
        Define o nome do professor.
        '''
        self.__nome = nome

    def get_horario_atendimento(self) -> str:
        '''
        Retorna o horário de atendimento do professor, das "08:00" às "23:10".
        '''
        return self.__horario_atendimento

    def set_horario_atendimento(self, horario_atendimento: str) -> None:
        '''
        Define o horário de atendimento do professor, das "08:00" às "23:10".
        '''
        self.__horario_atendimento = horario_atendimento

    def get_periodo(self) -> str:
        '''
        Retorna o periodo do professor, "Integral" ou "Noturno".
        '''
        return self.__periodo

    def set_periodo(self, periodo: str) -> None:
        '''
        Define o periodo do professor, "Integral" ou "Noturno".
        '''
        self.__periodo = periodo
