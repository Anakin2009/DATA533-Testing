

import unittest # Jupyter notebook
from User import *
from Calculation import *
class TestUser(unittest.TestCase): # test class
    def __int__(self):
        return super().__int__()

    def setUp(self):
        self.newuser1 = newUser('John', 10001, 10)
        self.newuser2 = newUser('Mary', 10002, 20)
        self.newuser3 = newUser('Tom', 10003, 30)
        self.newuser4 = newUser('Jack', 10004, 40)

    def tearDown(self):
        print('Tear Down')

    def setUpClass(newUser):
        print('SetupClass')

    def tearDownClass(newUser):
        print('TearDownClass')

    def test_deposit(self):
        self.newuser1.deposit('2020-01-01')
        self.assertEqual(self.newuser1.balance, 10)
        self.newuser2.deposit('2020-01-02')
        self.assertEqual(self.newuser2.balance, 20)
        self.newuser3.deposit('2020-01-03')
        self.assertEqual(self.newuser3.balance, 30)
        self.newuser4.deposit('2020-01-04')
        self.assertEqual(self.newuser4.balance, 50)

    def test_information(self):
        self.newuser1.information('2020-01-01')
        self.newuser2.information('2020-01-02')
        self.newuser3.information('2020-01-03')
        self.newuser4.information('2020-01-04')
        self.assertEqual(self.newuser1.acc_num, 10001)
        self.assertEqual(self.newuser2.acc_num, 10002)
        self.assertEqual(self.newuser3.acc_num, 10003)
        self.assertEqual(self.newuser4.acc_num, 10005)


unittest.main(argv=[''], verbosity=2, exit=False)





