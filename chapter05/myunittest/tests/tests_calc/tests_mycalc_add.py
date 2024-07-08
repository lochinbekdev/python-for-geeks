import unittest
from myunittest.src.calc.mycalc import MyCalc

class MyCalcAddTestSuite(unittest.TestCase):
    def setUp(self):
        self.mycalc = MyCalc()

    def test_add(self):
        """Test case to validate two positive numbers """
        self.assertEqual(15,self.mycalc.add(10,5),"should be 15")
