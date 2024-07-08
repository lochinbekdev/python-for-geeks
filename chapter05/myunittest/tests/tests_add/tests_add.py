import unittest

from myunittest.src.myadd.add import add

class MyAddTestSuite(unittest.TestCase):


    def test_add1(self):
        self.assertEqual(15,add(10,5),"should bi 15")

    def test_add2(self):
        self.assertEqual(5,add(10,-5),"should be 5")

    def test_add3(self):
        self.assertEqual(-15,add(-10,-5),"should be -15")

    def test_add4(self):
        self.assertEqual(-5,add(-10,5),"should bbe -5")




if __name__ == "__main__":
    unittest.main()
