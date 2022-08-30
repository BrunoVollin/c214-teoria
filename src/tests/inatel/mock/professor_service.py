"""
Contains the mock class for the inatel.professor_service module.

Classes
-------
MockProfessorService
    Mock class for the inatel.professor_service module.
"""

from src.main.inatel.professor_service import ProfessorService
from src.tests.inatel.constants.professor import *


class MockProfessorService(ProfessorService):
    """
    Mock class for ProfessorService.
    """

    def busca(self, id_num: int) -> str:
        """
        Searches for a professor by id.

        Parameters
        ----------
        id_num : int
            Id of the professor.

        Returns
        -------
        str
            Data of the professor.

        Raises
        ------
        ValueError
            If the professor was not found.
        """
        if id_num == 0:
            return CHRIS
        if id_num == 1:
            return MARCELO
        if id_num == 2:
            return RENZO
        raise ValueError("Professor não encontrado.")

    def professor_existe(self, id_num: int) -> bool:
        """
        Verifies if a professor exists.

        Parameters
        ----------
        id_num : int
            Id of the professor.

        Returns
        -------
        bool
            True if the professor exists, False otherwise.
        """
        lista_professores = [0, 1, 2]
        for professor in lista_professores:
            if professor == id_num:
                return True
        return False
