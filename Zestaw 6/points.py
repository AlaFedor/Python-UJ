import math

class Point:
    """Klasa reprezentująca punkty na płaszczyźnie."""

    def __init__(self, x, y):  # konstuktor
        self.x = x
        self.y = y

    def __str__(self):
        return f"({self.x}, {self.y})"        # zwraca string "(x, y)"

    def __repr__(self):
        return f"Point({self.x}, {self.y})"        # zwraca string "Point(x, y)"

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y   # obsługa point1 == point2

    def __ne__(self, other):        # obsługa point1 != point2
        return not self == other

    # Punkty jako wektory 2D.
    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y) # v1 + v2

    def __sub__(self, other):
        return Point(self.x - other.x, self.y - other.y)  # v1 - v2

    def __mul__(self, other):
        return self.x * other.x + self.y * other.y  # v1 * v2, iloczyn skalarny, zwraca liczbę

    def cross(self, other):         # v1 x v2, iloczyn wektorowy 2D, zwraca liczbę
        return self.x * other.y - self.y * other.x

    def length(self):
        return math.sqrt(self.x ** 2 + self.y ** 2)          # długość wektora

    def __hash__(self):
        return hash((self.x, self.y))   # bazujemy na tuple, immutable points

# Kod testujący moduł.

import unittest

class TestPoint(unittest.TestCase):
    def test_init_and_repr(self):
        p1 = Point(1, 2)
        p2 = Point(-3, 4)
        self.assertEqual(p1.x, 1)
        self.assertEqual(p1.y, 2)
        self.assertEqual(p2.x, -3)
        self.assertEqual(p2.y, 4)
        self.assertEqual(str(p1), "(1, 2)")
        self.assertEqual(str(p2), "(-3, 4)")
        self.assertEqual(repr(p1), "Point(1, 2)")
        self.assertEqual(repr(p2), "Point(-3, 4)")

    def test_equality(self):
        self.assertTrue(Point(1, 2) == Point(1, 2))
        self.assertFalse(Point(1, 2) == Point(2, 1))
        self.assertTrue(Point(0, 0) != Point(1, 0))
        self.assertFalse(Point(5, 5) != Point(5, 5))

    def test_addition(self):
        self.assertEqual(Point(1, 2) + Point(3, 4), Point(4, 6))
        self.assertEqual(Point(-1, 5) + Point(2, -3), Point(1, 2))

    def test_subtraction(self):
        self.assertEqual(Point(1, 2) - Point(3, 4), Point(-2, -2))
        self.assertEqual(Point(-1, 0) - Point(2, -3), Point(-3, 3))

    def test_scalar_product(self):
        self.assertEqual(Point(1, 2) * Point(3, 4), 11)
        self.assertEqual(Point(-1, 2) * Point(2, -3), -8)

    def test_cross_product(self):
        self.assertEqual(Point(1, 2).cross(Point(3, 4)), -2)
        self.assertEqual(Point(-1, 5).cross(Point(2, -3)), -7)

    def test_length(self):
        self.assertAlmostEqual(Point(3, 4).length(), 5.0)
        self.assertAlmostEqual(Point(-3, -4).length(), 5.0)

    def test_hash(self):
        s = {Point(1, 2), Point(1, 2), Point(2, 1)}
        self.assertEqual(len(s), 2)

if __name__ == '__main__':
    unittest.main()
    