import unittest
from proba.circle import circle_area
from math import pi

class TestCircleArea(unittest.TestCase):
    def test_area(self):
        self.assertEqual(circle_area(5),pi*5**2)
        self.assertEqual(circle_area(1),pi*1**2)
        self.assertEqual(circle_area(9.999),pi*9.999**2)
        self.assertEqual(circle_area(1.7), pi*1.7**2)

    print("Выбрасываются ли исключения для отрицательных радиусов?")
    def test_values(self):
        self.assertRaises(ValueError, circle_area, -5)
        self.assertRaises(ValueError, circle_area, -33)
        self.assertRaises(ValueError, circle_area, 0)

    print("Выбрасываются ли исключения о несовместимости типов?")
    def test_types(self):
        self.assertRaises(TypeError, circle_area, 5+5j)
        self.assertRaises(TypeError, circle_area, 'stroka')
        self.assertRaises(TypeError, circle_area, ['cikl',55])
        self.assertRaises(TypeError, circle_area, True)
