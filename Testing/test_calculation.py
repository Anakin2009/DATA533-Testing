import unittest # Jupyter notebook
from BankAccountSystem.Structure import calculation




class Testcalculation(unittest.TestCase): # test class
    def setUp(self):
        print('Set up')

    def tearDown(self):
        print('Tear Down')

    @classmethod
    def setUpClass(cls):
        print('SetupClass')

    @classmethod
    def tearDownClass(cls):
        print('TearDownClass')

    def test_interest(self):
        self.assertEqual(calculation.interest(1), 0.0001)
        self.assertEqual(calculation.interest(2), 0.0002)
        self.assertEqual(calculation.interest(3), 0.0003)
        self.assertEqual(calculation.interest(4), 0.0004)

    def test_service(self):
        self.assertEqual(calculation.service(100), 103)
        self.assertEqual(calculation.service(2), 5)
        self.assertEqual(calculation.service(11), 14)
        self.assertEqual(calculation.service(400), 403)

unittest.main(argv=[''], verbosity=2, exit=False)


#%%
