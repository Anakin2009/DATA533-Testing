import unittest # Jupyter notebook
import calculation
class Testcalculation(unittest.TestCase): # test class
    def setUp(self):
        print('Set up')

    def tearDown(self):
        print('Tear Down')

    def test_interest(self):
        self.assertEqual(calculation.interest(100), 1)
        self.assertEqual(calculation.interest(200), 2)
        self.assertEqual(calculation.interest(300), 3)
        self.assertEqual(calculation.interest(400), 4)

    def test_service(self):
        self.assertEqual(calculation.service(100), 103)
        self.assertEqual(calculation.service(2), 5)
        self.assertEqual(calculation.service(11), 14)
        self.assertEqual(calculation.service(400), 403)

unittest.main(argv=[''], verbosity=2, exit=False)


#%%
