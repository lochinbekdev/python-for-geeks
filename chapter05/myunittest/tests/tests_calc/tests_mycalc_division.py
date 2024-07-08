import unittest
from myunittest.src.calc.mycalc import MyCalc

class MyCalcDivisionTestSuite(unittest.TestCase):
    def setUp(self):
        self.mycalc = MyCalc()

    def test_division(self):
        """Test case to validate two positive numbers """
        self.assertEqual(2,self.mycalc.divide(10,5),"should be 2")
