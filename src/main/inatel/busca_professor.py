"""
Contains the BuscaProfessor class.

...

Classes
-------
BuscaProfessor
    Contains methods to search for a professor in Inatel's database.
"""

import json
from src.main.inatel.professor_service import ProfessorService
from src.main.inatel.professor import Professor


class BuscaProfessor():
    """
    Class to search for a professor in Inatel's database.

    ...

    Initialization
    --------------
    professor_service : ProfessorService
        ProfessorService object to access the Inatel's database.

    Attributes
    ----------
    __professor_service : ProfessorService
        Private ProfessorService object to access the Inatel's database.
    """

    def __init__(self, professor_service: ProfessorService):
        self.__professor_service = professor_service

    def busca_professor(self, id_num: int) -> Professor:
        """
        Searches for a professor by id.

        ...

        Parameters
        ----------
        id_num : int
            Id of the professor.

        Returns
        -------
        Professor
            Data of the professor.
        """
        professor_json = self.__professor_service.busca(id_num)
        objeto_json = json.loads(professor_json)

        return Professor(objeto_json['nomeDoProfessor'],
                         objeto_json['horarioDeAtendimento'],
                         objeto_json['periodo'])

    def verifica_professor_existe(self, id_num: int) -> bool:
        """
        Verifies if a professor exists.

        ...

        Parameters
        ----------
        id_num : int
            Id of the professor.

        Returns
        -------
        bool
            True if the professor exists, False otherwise.
        """
        return self.__professor_service.professor_existe(id_num)
