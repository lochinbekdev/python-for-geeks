import unittest
from tests_calc.tests_mycalc_add import MyCalcAddTestSuite
from tests_calc.tests_mycalc_substract import MyCalcSubstractTestSuite
from tests_calc.test_myclac_multiply import MyCalcMultiplyTestSuite
from tests_calc.tests_mycalc_division import MyCalcDivisionTestSuite

def run_mytests():
    test_classes=[
        MyCalcAddTestSuite,MyCalcDivisionTestSuite,MyCalcSubstractTestSuite,MyCalcMultiplyTestSuite
    ]


    loader = unittest.TestLoader()

    test_suites = []
    for t_class in test_classes:
        suite = loader.loadTestsFromTestCase(t_class)
        test_suites.append(suite)

    final_suite = unittest.TestSuite(test_suites)

    runner = unittest.TextTestRunner()
    result = runner.run(final_suite)


if __name__ == "__main__":
    run_mytests()