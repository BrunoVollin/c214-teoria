"""
Script to execute all tests in this module.
"""

import unittest
from src.tests.inatel.busca_professor import TesteBuscaProfessor


def create_suite():
    """
    Creates a test suite with all tests in this module.

    ...

    Returns
    -------
    unittest.TestSuite
        Test suite with all tests in this module.
    """
    test_suite = unittest.TestSuite()
    test_suite.addTest(unittest.makeSuite(TesteBuscaProfessor))
    return test_suite


if __name__ == '__main__':
    suite = create_suite()
    runner = unittest.TextTestRunner()
    runner.run(suite)
