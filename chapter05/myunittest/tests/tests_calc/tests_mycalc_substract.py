import unittest
from myunittest.src.calc.mycalc import MyCalc

class MyCalcSubstractTestSuite(unittest.TestCase):
    def setUp(self):
        self.mycalc = MyCalc()

    def test_substract(self):
        """Test case to validate two positive numbers """
        self.assertEqual(5,self.mycalc.substract(10,5),"should be 5")
