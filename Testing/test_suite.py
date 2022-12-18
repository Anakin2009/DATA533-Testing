import unittest
from Testing.test_User import TestUser
from Testing.test_calculation import Testcalculation
from Testing.test_bankingUI import TestbankingUI
from Testing.test_bankingDS import TestbankingDS


def my_suite():
    suite = unittest.TestSuite()
    result = unittest.TestResult()
    suite.addTest(unittest.makeSuite(TestUser))
    suite.addTest(unittest.makeSuite(Testcalculation))
    suite.addTest(unittest.makeSuite(TestbankingUI))
    suite.addTest(unittest.makeSuite(TestbankingDS))
    runner = unittest.TextTestRunner()
    print(runner.run(suite))

my_suite()

