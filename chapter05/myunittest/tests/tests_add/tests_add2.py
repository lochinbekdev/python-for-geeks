import unittest
from unittest.src.add2 import MyAdd

class MyAddTestSuite(unittest.TestCase):
    def setUp(self):
        self.myadd = MyAdd()

    def tearDown(self):
        del (self.myadd)

    def test_add1(self):
        """this test case validate two positive numbers"""
        self.assertEqual(15,self.myadd.add(10,5),"should be 15")

    def test_add2(self):
        """test case to validate positive and negative numbers"""
        self.assertEqual(5,self.myadd.add(10,-5),"Should be 5")
