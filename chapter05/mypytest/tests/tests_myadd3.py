import pytest
from mypytest.src.myadd3 import add

def test_add1():
    """test validate two positive numbers"""
    assert add(10,-5) == 5, "should be 5"

def testadd_2():
    """test case to validate two positive numbers"""
    assert add(10,-5) == 5, "should be 5"

