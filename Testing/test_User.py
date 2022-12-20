

import unittest # Jupyter notebook
import BankAccountSystem.Structure.User

class User():
    def __init__(self, name, acc_num):
        self.name = name
        self.acc_num = acc_num

class newUser(User):
    def __init__(self, name, acc_num, init_dps):
        super().__init__(name, acc_num)
        self.balance = init_dps
        self.init_dps = init_dps

    def information(self, date):
        print("Here is your account information")
        print(f'Name: {self.name}')
        print(f'Account Number: {self.acc_num}')
        print(f'Open Date: {date}')
        print(f'Account Balance: {self.balance}')

    def store(self):
        ds.addAccount(self.name, self.acc_num, self.init_dps, self.balance)



class TestUser(unittest.TestCase): # test class

    def setUp(self):
        self.user1 = User('John', 10001)
        self.user2 = User('Mary', 10002)
        self.user3 = User('Tom', 10003)
        self.user4 = User('Jack', 10004)
        self.user1 = newUser('John', 10001, 10)
        self.user2 = newUser('Mary', 10002, 20)
        self.user3 = newUser('Tom', 10003, 30)
        self.user4 = newUser('Jack', 10004, 50)


    def tearDown(self):
        print('Tear Down')

    @classmethod
    def setUpClass(User):
        print('SetupClass')

    @classmethod
    def tearDownClass(cls):
        print('TearDownClass')

    def test_user(self):
        self.assertEqual(self.user1.name, 'John')
        self.assertEqual(self.user2.name, 'Mary')
        self.assertEqual(self.user3.name, 'Tom')
        self.assertEqual(self.user4.name, 'Jacck')

    def test_newUser(self):
        self.assertEqual(self.user1.balance, 10)
        self.assertEqual(self.user2.balance, 20)
        self.assertEqual(self.user3.balance, 30)
        self.assertEqual(self.user4.balance, 980)

    if __name__ == '__main__':
        unittest.main(argv=[''], verbosity=2, exit=False)

#%%
