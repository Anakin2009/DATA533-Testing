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

unittest.main(argv=[''], verbosity=2, exit=False)



#%%
