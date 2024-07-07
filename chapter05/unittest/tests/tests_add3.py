from contextlib import AbstractContextManager
from typing import Any
import unittest
from unittest.src.add2 import MyAdd

class MyAddTestSuite(unittest.TestCase):
    def setUp(self):
        self.myadd = MyAdd

    def test_typeerror1(self):
        """This test case to check if we can handle nom number input"""
        self.assertRaises(TypeError,self.myadd.add,'a',-5)

    def test_typeerror2(self):
        """this test case to check i we can handle non number input"""
        self.assertRaises(TypeError ,self.myadd.add,'a','b')

    