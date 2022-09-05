"""
Script to execute all tests in this module.
"""

import unittest
from tests.test_calculator import TestCalculator


def create_test_suite() -> unittest.TestSuite:
    """
    Creates a test suite with all tests in this module.

    ...

    Returns
    -------
    unittest.TestSuite
        Test suite with all tests in this module.
    """
    test_suite = unittest.TestSuite()
    test_suite.addTest(unittest.makeSuite(TestCalculator))
    return test_suite


if __name__ == '__main__':
    suite = create_test_suite()
    runner = unittest.TextTestRunner()
    runner.run(suite)
