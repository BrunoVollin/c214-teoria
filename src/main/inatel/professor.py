"""
Contains the Professor class.

...

Classes
-------
Professor
    Contains data of a professor.
"""


class Professor():
    """
    Class used to represent a professor from Inatel.

    ...

    Initialization
    --------------
    nome : str
        Name of the professor.
    horario_atendimento : str
        Professor's hours of attendance in the format "hh:mm"".
    periodo : str
        Professor's period, "integral" or "noturno".

    Attributes
    ----------
    __nome : str
        Private name of the professor.
    __horario_atendimento : str
        Private professor's hours of attendance in the format "hh:mm"".
    __periodo : str
        Private professor's period, "integral" or "noturno".
    """

    def __init__(self, nome: str, horario_atendimento: str, periodo: str):
        self.__nome = nome
        self.__horario_atendimento = horario_atendimento
        self.__periodo = periodo

    def get_nome(self) -> str:
        """
        Returns the name of the professor.

        ...

        Returns
        -------
        str
            Name of the professor.
        """
        return self.__nome

    def set_nome(self, nome: str) -> None:
        """
        Sets the name of the professor.

        ...

        Parameters
        ----------
        nome : str
            Name of the professor.
        """
        self.__nome = nome

    def get_horario_atendimento(self) -> str:
        """
        Returns the professor's hours of attendance.

        ...

        Returns
        -------
        str
            Professor's hours of attendance in the format "hh:mm"".
        """
        return self.__horario_atendimento

    def set_horario_atendimento(self, horario_atendimento: str) -> None:
        """
        Sets the professor's hours of attendance.

        ...

        Parameters
        ----------
        horario_atendimento : str
            Professor's hours of attendance in the format "hh:mm"".
        """
        self.__horario_atendimento = horario_atendimento

    def get_periodo(self) -> str:
        """
        Returns the professor's period.

        ...

        Returns
        -------
        str
            Professor's period, "integral" or "noturno".
        """
        return self.__periodo

    def set_periodo(self, periodo: str) -> None:
        """
        Sets the professor's period.

        ...

        Parameters
        ----------
        periodo : str
            Professor's period, "integral" or "noturno".
        """
        self.__periodo = periodo
