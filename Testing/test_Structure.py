import unittest 
import sys
sys.path.append('C:\\Users\\sophiechen\\2022MDS\\Block 3\\Data-533\\project\\step2\\DATA533-testing\\')
from BankAccountSystem.Structure import *

class test_User(unittest.TestCase): # test class 

    def setUp(self):
        self.user1 = User('Sherry', 10000)
        self.user2 = User('Yuki', 11111)
        self.user3 = User('Nyx', 22222)
        self.user4 = User('Shveta', 33333)
        self.user1 = newUser('Sherry', 10000, 10)
        self.user2 = newUser('Yuki', 11111, 20)
        self.user3 = newUser('Nyx', 22222, 30)
        self.user4 = newUser('Shveta', 33333, 40)


    def test_user(self):
        self.assertEqual(self.user1.name, 'Sherry')
        self.assertEqual(self.user2.name, 'Yuki')
        self.assertEqual(self.user3.name, 'Nyx')
        self.assertEqual(self.user4.name, 'Shveta')

    def test_newUser(self):
        self.assertEqual(self.user1.balance, 10)
        self.assertEqual(self.user2.balance, 20)
        self.assertEqual(self.user3.balance, 30)
        self.assertEqual(self.user4.balance, 40)

unittest.main(argv=[''], verbosity=2, exit=False)


class test_calculation(unittest.TestCase): # test class
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

    def test_getIntRates(): 
        self.assertEqual(getIntRates, 0.0001)

    def test_service(self):
        self.assertEqual(calculation.service(100), 103)
        self.assertEqual(calculation.service(200), 203)
        self.assertEqual(calculation.service(300), 303)
        self.assertEqual(calculation.service(400), 403)

unittest.main(argv=[''], verbosity=2, exit=False)
