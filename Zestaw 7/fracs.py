
from math import gcd

class Frac:
    """Klasa reprezentująca ułamek."""

    def __init__(self, x=0, y=1):
        # Sprawdzamy, czy y=0.
        if y == 0:
            raise ZeroDivisionError("mianownik nie moze byc zerem")
        self.x = x
        self.y = y
        self._simplify()

    def _simplify(self):
        nwd = gcd(self.x, self.y)
        self.x //= nwd
        self.y //= nwd

        if self.y < 0:
            self.x *= -1
            self.y *= -1

    def _to_frac(self, other):
        if isinstance(other, Frac):
            return other
        if isinstance(other, int):
            return Frac(other, 1)
        if isinstance(other, float):
            num, den = other.as_integer_ratio()
            return Frac(num, den)
        raise ValueError("Niepoprawny typ do operacji z Frac")

    def __str__(self):
        if self.y == 1: 
            return str(self.x)
        return str(self.x) + '/' + str(self.y) # zwraca "x/y" lub "x" dla y=1

    def __repr__(self):
        return f"Frac({self.x},{self.y})" # zwraca "x/y" lub "x" dla y=1

    def __eq__(self, other):
        other = self._to_frac(other)
        return self.x == other.x and self.y == other.y

    def __ne__(self, other):
        other = self._to_frac(other)
        return not self.__eq__(other)

    def __lt__(self, other):
        other = self._to_frac(other)
        return self.x * other.y < self.y * other.x

    def __le__(self, other):
        other = self._to_frac(other)
        return self.x * other.y <= self.y * other.x

    def __gt__(self, other):
        other = self._to_frac(other)
        return self.x * other.y > self.y * other.x

    def __ge__(self, other):
        other = self._to_frac(other)
        return self.x * other.y >= self.y * other.x

    def __add__(self, other):
        other = self._to_frac(other)
        return Frac(self.x * other.y + other.x * self.y, self.y * other.y) # frac1+frac2, frac+int

    __radd__ = __add__ # int+frac

    def __sub__(self, other):
        other = self._to_frac(other)
        return Frac(self.x * other.y - other.x * self.y, self.y * other.y) # frac1-frac2, frac-int

    def __rsub__(self, other):
        other = self._to_frac(other)
        return other.__sub__(self)

    def __mul__(self, other): # frac1*frac2, frac*int
        other = self._to_frac(other)
        return Frac(self.x * other.x, self.y * other.y)

    __rmul__ = __mul__ # int*frac

    def __truediv__(self, other): # frac1/frac2, frac/int, Py3
        other = self._to_frac(other)
        if other.x == 0:
            raise ZeroDivisionError("dzielenie przez zero")
        return Frac(self.x * other.y, self.y * other.x)

    def __rtruediv__(self, other): # int/frac, Py3
        other = self._to_frac(other)
        return other.__truediv__(self)

 # operatory jednoargumentowe

    def __pos__(self):
        return self # +frac = (+1)*frac

    def __neg__(self):
        return Frac(-self.x, self.y) # -frac = (-1)*frac

    def __invert__(self):
        if self.x == 0:
            raise ZeroDivisionError("odwrotność z 0 nie istnieje")
        return Frac(self.y, self.x)
         # odwrotnosc: ~frac

    def __float__(self):
        return self.x / self.y  # float(frac)

    def __hash__(self):
        return hash(float(self))

import unittest 

class TestFrac(unittest.TestCase):

    def test_init_and_simplify(self):
        self.assertEqual(Frac(-3, -9), Frac(1, 3))
        self.assertEqual(Frac(2, -4), Frac(-1, 2))
        with self.assertRaises(ZeroDivisionError):
            Frac(1, 0)

    def test_to_frac(self):
        f = Frac(1, 2)
        self.assertEqual(f._to_frac(3), Frac(3, 1))
        self.assertEqual(f._to_frac(0.5), Frac(1, 2))
        g = Frac(7, 9)
        self.assertIs(f._to_frac(g), g)
        with self.assertRaises(ValueError):
            f._to_frac("abc")

    def test_str_repr(self):
        self.assertEqual(str(Frac(-3, 1)), "-3")
        self.assertEqual(str(Frac(3, 2)), "3/2")
        self.assertEqual(repr(Frac(5, 2)), "Frac(5,2)")
        self.assertEqual(repr(Frac(-5, 3)), "Frac(-5,3)")

    def test_equality(self):
        self.assertTrue(Frac(-3, -9) == Frac(1, 3))
        self.assertTrue(Frac(2, 1) == 2)
        self.assertTrue(Frac(-2, 4) == -0.5)
        self.assertFalse(Frac(0, 1) == Frac(1, 1))

    def test_comparisons(self):
        self.assertTrue(Frac(1, 4) < 2)
        self.assertTrue(Frac(1, 2) <= 0.5)
        self.assertFalse(3 < Frac(1, 2))
        self.assertFalse(Frac(10, 2) <= Frac(2, 3))

    def test_add(self):
        self.assertEqual(Frac(1, 2) + 0.5, Frac(1, 1))
        self.assertEqual(1 + Frac(1, 2), Frac(3, 2))

    def test_sub(self):
        self.assertEqual(Frac(1, 2) - 1, Frac(-1, 2))
        self.assertAlmostEqual(float(Frac(2, 5) - 0.2), 0.2)

    def test_rsub(self):
        self.assertAlmostEqual(float(1 - Frac(1, 2)), 0.5)
        self.assertAlmostEqual(float(0.4 - Frac(1, 5)), 0.2)

    def test_mul(self):
        self.assertEqual(Frac(2, 3) * 3, Frac(2, 1))
        self.assertEqual(2 * Frac(3, 2), Frac(3, 1))
        self.assertEqual(Frac(3, 2) * 0.5, Frac(3, 4))

    def test_truediv(self):
        self.assertEqual(Frac(1, 2) / Frac(3, 4), Frac(2, 3))
        self.assertEqual(Frac(3, 2) / 0.5, Frac(3, 1))
        self.assertEqual(2 / Frac(3, 2), Frac(4, 3))
        with self.assertRaises(ZeroDivisionError):
            Frac(1, 2) / Frac(0, 1)

    def test_rtruediv(self):
        self.assertEqual(1 / Frac(1, 2), Frac(2, 1))
        self.assertEqual(1.5 / Frac(3, 2), Frac(1, 1))
        self.assertEqual(2 / Frac(-3, 4), Frac(-8, 3))
        with self.assertRaises(ZeroDivisionError):
            1 / Frac(0, 1)

    def test_unary(self):
        self.assertEqual(+Frac(3, 4), Frac(3, 4))
        self.assertEqual(-Frac(3, 4), Frac(-3, 4))
        self.assertEqual(~Frac(3, 4), Frac(4, 3))
        with self.assertRaises(ZeroDivisionError):
            ~Frac(0, 1)

    def test_float(self):
        self.assertAlmostEqual(float(Frac(1, 4)), 0.25)

    def test_hash(self):
        s = {Frac(1, 2), Frac(2, 4), Frac(3, 6)}
        self.assertEqual(len(s), 1)


if __name__ == '__main__':
    unittest.main()
