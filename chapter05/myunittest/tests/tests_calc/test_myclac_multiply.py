import unittest
from myunittest.src.calc.mycalc import MyCalc

class MyCalcMultiplyTestSuite(unittest.TestCase):
    def setUp(self):
        self.mycalc = MyCalc()

    def test_multiply(self):
        """Test case to validate two positive numbers """
        self.assertEqual(50,self.mycalc.multiply(10,5),"should be 50")
