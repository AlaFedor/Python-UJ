#from fractions import gcd   # Py2
from math import gcd   # Py3

class Frac:
    """Klasa reprezentująca ułamek."""

    def __init__(self, x=0, y=1):
        if y == 0:
            raise ZeroDivisionError("mianownik nie moze byc zerem")
        self.x = x
        self.y = y
        self.skroc_ulamek()

    def skroc_ulamek(self):
        if self.y == 0:
            raise ZeroDivisionError("mianownik nie moze byc zerem")
        nwd = gcd(self.x, self.y)
        self.x //= nwd
        self.y //= nwd
        if self.y < 0:
            self.x *= -1
            self.y *= -1

    def __str__(self):
        if self.y == 1: 
            return str(self.x)
        return str(self.x) + '/' + str(self.y)         # zwraca "x/y" lub "x" dla y=1

    def __repr__(self):
        return f"Frac({self.x},{self.y})"       # zwraca "Frac(x, y)"

    #def __cmp__(self, other): pass  # cmp(frac1, frac2)    # Py2

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y    # Py2.7 i Py3

    def __ne__(self, other):
        return not self.__eq__(other)

    def __lt__(self, other):
        return self.x * other.y < self.y * other.x

    def __le__(self, other):
        return self.x * other.y <= self.y * other.x

    #def __gt__(self, other): pass

    #def __ge__(self, other): pass

    def __add__(self, other):
        licznik_wynik = self.x * other.y + other.x * self.y
        mianownik_wynik = self.y * other.y
        return Frac(licznik_wynik, mianownik_wynik)  # frac1 + frac2

    def __sub__(self, other):
        licznik_wynik = self.x * other.y - other.x * self.y
        mianownik_wynik = self.y * other.y
        return Frac(licznik_wynik, mianownik_wynik)  
          # frac1 - frac2

    def __mul__(self, other):
        licznik_wynik = self.x * other.x
        mianownik_wynik = self.y * other.y
        return Frac(licznik_wynik, mianownik_wynik)
      # frac1 * frac2

    def __div__(self, other):
        if other.x == 0:
            raise ZeroDivisionError("dzielenie przez zero")
        licznik_wynik = self.x * other.y
        mianownik_wynik = self.y * other.x
        return Frac(licznik_wynik, mianownik_wynik) 
          # frac1 / frac2, Py2

    def __truediv__(self, other):
        if other.x == 0:
            raise ZeroDivisionError("dzielenie przez zero")
        licznik_wynik = self.x * other.y
        mianownik_wynik = self.y * other.x
        return Frac(licznik_wynik, mianownik_wynik)   # frac1 / frac2, Py3

    def __floordiv__(self, other):
        if other.x == 0:
            raise ZeroDivisionError("dzielenie przez zero")
        return (self.x * other.y) // (self.y * other.x)  # frac1 // frac2, opcjonalnie

    def __mod__(self, other):
        if other.x == 0:
            raise ZeroDivisionError("dzielenie przez zero")
        q = self.__floordiv__(other)
        return self - Frac(q, 1) * other
         # frac1 % frac2, opcjonalnie

    # operatory jednoargumentowe
    def __pos__(self):  # +frac = (+1)*frac
        return self

    def __neg__(self):  # -frac = (-1)*frac
        return Frac(-self.x, self.y)

    def __invert__(self):  # odwrotnosc: ~frac
        return Frac(self.y, self.x)

    def __float__(self):
        return self.x / self.y       # float(frac)

    def __hash__(self):
        return hash(float(self))   # immutable fracs
        # w Pythonie set([2]) == set([2.0])
        # chcemy set([2]) == set([Frac(2)])

# Kod testujący moduł.

import unittest

class TestFrac(unittest.TestCase):

    def setUp(self):
        self.zero = [0, 1]
    
    def test_init_and_simplify(self):
        self.assertEqual(Frac(-3, -9), Frac(1, 3))
        self.assertEqual(Frac(2, -4), Frac(-1, 2))
        with self.assertRaises(ZeroDivisionError):
            Frac(1, 0)

    def test_str_repr(self):
        self.assertEqual(str(Frac(-3, 1)), "-3")
        self.assertEqual(str(Frac(3, 2)), "3/2")
        self.assertEqual(repr(Frac(5, 2)), "Frac(5,2)")
        self.assertEqual(repr(Frac(-5, 3)), "Frac(-5,3)")

    def test_equality(self):
        self.assertTrue(Frac(-3, -9) == Frac(1, 3))
        self.assertFalse(Frac(2, -4) == Frac(3, 4))
        self.assertTrue(Frac(-2, 4) == Frac(-1, 2))
        self.assertFalse(Frac(0, 1) == Frac(1, 1))

    def test_comparisons(self):
        self.assertTrue(Frac(1, 4) < Frac(1, 2))
        self.assertTrue(Frac(1, 2) <= Frac(2, 4))
        self.assertFalse(Frac(3, 1) < Frac(1, 2))
        self.assertFalse(Frac(10, 2) <= Frac(2, 3))

    def test_add(self):
        self.assertEqual(Frac(1, 2) + Frac(1, 3), Frac(5, 6))
        self.assertEqual(Frac(-1, 2) + Frac(2, 3), Frac(1, 6))

    def test_sub(self):
        self.assertEqual(Frac(1, 2) - Frac(1, 3), Frac(1, 6))
        self.assertEqual(Frac(2, 3) - Frac(1, 2), Frac(1, 6))

    def test_mul(self):
        self.assertEqual(Frac(2, 3) * Frac(3, 4), Frac(1, 2))
        self.assertEqual(Frac(-2, 3) * Frac(3, 4), Frac(-1, 2))

    def test_truediv(self):
        self.assertEqual(Frac(1, 2) / Frac(3, 4), Frac(2, 3))
        self.assertEqual(Frac(-2, 3) / Frac(1, 6), Frac(-4, 1))
        with self.assertRaises(ZeroDivisionError):
            Frac(1, 2) / Frac(0, 1)

    def test_floordiv(self):
        self.assertEqual(Frac(7, 3) // Frac(2, 5), 5)
        self.assertEqual(Frac(-7, 3) // Frac(2, 5), -6)
        with self.assertRaises(ZeroDivisionError):
            Frac(1, 2) // Frac(0, 1)

    def test_mod(self):
        self.assertEqual(Frac(7, 3) % Frac(2, 5), Frac(1, 3))
        self.assertEqual(Frac(17, 4) % Frac(5, 6), Frac(1, 12))

    def test_unary(self):
        self.assertEqual(+Frac(3, 4), Frac(3, 4))
        self.assertEqual(+Frac(-5, 6), Frac(-5, 6))
        self.assertEqual(-Frac(3, 4), Frac(-3, 4))
        self.assertEqual(-Frac(-2, 3), Frac(2, 3))
        self.assertEqual(~Frac(3, 4), Frac(4, 3))
        self.assertEqual(~Frac(-2, 5), Frac(5, -2))
        with self.assertRaises(ZeroDivisionError):
            ~Frac(0, 1)

    def test_float(self):
        self.assertAlmostEqual(float(Frac(1, 4)), 0.25)
        self.assertAlmostEqual(float(Frac(-3, 2)), -1.5)

    def test_hash(self):
        s = {Frac(1, 2), Frac(2, 4), Frac(3, 6)}
        self.assertEqual(len(s), 1) 
        s2 = {Frac(1, 2), Frac(1, 3)}
        self.assertEqual(len(s2), 2)

    def tearDown(self): pass

if __name__ == '__main__':
    unittest.main()