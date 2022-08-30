'''
Executa os testes do projeto Inatel.
'''

import unittest
from src.tests.inatel.busca_professor import TesteBuscaProfessor


def suite():
    '''
    Unifica todos os testes deste módulo em uma suite de testes.
    '''
    new_suite = unittest.TestSuite()
    new_suite.addTest(unittest.makeSuite(TesteBuscaProfessor))
    return new_suite


if __name__ == '__main__':
    test_suite = suite()
    runner = unittest.TextTestRunner()
    runner.run(test_suite)
