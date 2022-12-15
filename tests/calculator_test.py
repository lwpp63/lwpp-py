import sys
from pprint import pprint
from unittest import TestCase, main
from proba.calculator import calculator
#pprint(sys.path)

class CalculatorTest(TestCase):
    def test_plus(self):
        self.assertEqual(calculator('5+5'), 10)

    def test_minus(self):
        self.assertEqual(calculator('15-25'), -10)

    def test_multi(self):
        self.assertEqual(calculator('7*7'), 49)

    def test_divide(self):
        self.assertEqual(calculator('55/11'), 5.0)

    def test_no_sing(self):
        with self.assertRaises(ValueError) as e:
            calculator('abracadabra')
        self.assertEqual('Выражение должно содержать хотя-бы один знак +-/* действия',e.exception.args[0])

    def test_two_sing(self):
        with self.assertRaises(ValueError) as e:
            calculator('3+9-5')
        self.assertEqual('Выражение должно содержать два целых и один знак!',e.exception.args[0])

if __name__ == "__main__":
    main()
