import unittest # Jupyter notebook
import User
class TestUser(unittest.TestCase): # test class

    def setUp(self):
        print('Set up')
    def tearDown(self):
        print('Tear Down')
    def test_genAccNum(self): # test case
        self.assertEqual(User.genAccNum(), 10000)
        self.assertEqual(User.genAccNum(), 33333)
        self.assertEqual(User.genAccNum(), 22)
        self.assertEqual(User.genAccNum(), 999999)

    def test_deposit(self):
        self.assertEqual(User.newUser.deposit(100), 100)
        self.assertEqual(User.newUser.deposit(200), 300)
        self.assertEqual(User.newUser.deposit(300), 600)
        self.assertEqual(User.newUser.deposit(400), 1000)

    def test_information(self):
        self.assertEqual(User.newUser.information(), 'Here is your account information')
        self.assertEqual(User.newUser.information(), 'Name: ')
        self.assertEqual(User.newUser.information(), 'Account Number: ')
        self.assertEqual(User.newUser.information(), 'Open Date: ')
        self.assertEqual(User.newUser.information(), 'Account Balance: ')

    def test_store(self):
        self.assertEqual(User.newUser.store(), 'addAccount')
        self.assertEqual(User.newUser.store(), 'addAccount')
        self.assertEqual(User.newUser.store(), 'addAccount')
        self.assertEqual(User.newUser.store(), 'addAccount')


unittest.main(argv=[''], verbosity=2, exit=False)



#%%

#%%
