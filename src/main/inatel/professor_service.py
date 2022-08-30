"""
Contains the ProfessorService interface.

...

Classes
-------
ProfessorService
    Contains methods to access the Inatel's database.
"""

from abc import abstractmethod


class ProfessorService():
    """
    Class that contains methods to access the Inatel's database.
    """

    @abstractmethod
    def busca(self, id_num: int) -> str:
        """
        Abstract method to access the Inatel's database and search for a professor, returning a
        string with the data of the professor.

        ...

        Raises
        ------
        NotImplementedError
            Abstract method.
        """
        raise NotImplementedError

    @abstractmethod
    def professor_existe(self, id_num: int) -> bool:
        """
        Abstract method to access the Inatel's database and check if a professor exists, returning
        a boolean.

        ...

        Raises
        ------
        NotImplementedError
            Abstract method.
        """
        raise NotImplementedError
