from math import gcd   # Py3

def skroc_ulamek(u):
    licznik, mianownik = u
    if mianownik == 0:
        raise ValueError("mianownik nie moze byc zerem")
    nwd = gcd(licznik, mianownik)
    licznik //= nwd
    mianownik //= nwd
    if mianownik < 0:
        licznik *= -1
        mianownik *= -1
    return [licznik, mianownik]

def add_frac(frac1, frac2):
    licznik1, mianownik1 = frac1
    licznik2, mianownik2 = frac2
    licznik_wynik = licznik1 * mianownik2 + licznik2 * mianownik1
    mianownik_wynik = mianownik1 * mianownik2
    return skroc_ulamek([licznik_wynik, mianownik_wynik])      # frac1 + frac2

def sub_frac(frac1, frac2):
    licznik1, mianownik1 = frac1
    licznik2, mianownik2 = frac2
    licznik_wynik = licznik1 * mianownik2 - licznik2 * mianownik1
    mianownik_wynik = mianownik1 * mianownik2
    return skroc_ulamek([licznik_wynik, mianownik_wynik])      # frac1 - frac2

def mul_frac(frac1, frac2):
    licznik1, mianownik1 = frac1
    licznik2, mianownik2 = frac2
    licznik_wynik = licznik1 * licznik2
    mianownik_wynik = mianownik1 * mianownik2
    return skroc_ulamek([licznik_wynik, mianownik_wynik])       # frac1 * frac2

def div_frac(frac1, frac2):
    licznik1, mianownik1 = frac1
    licznik2, mianownik2 = frac2
    licznik_wynik = licznik1 * mianownik2
    mianownik_wynik = mianownik1 * licznik2
    return skroc_ulamek([licznik_wynik, mianownik_wynik])       # frac1 / frac2

def is_positive(frac):
    licznik, mianownik = skroc_ulamek(frac)
    return licznik > 0            # bool, czy dodatni

def is_zero(frac):
    licznik, mianownik = skroc_ulamek(frac)
    return licznik == 0             # bool, typu [0, x]

def cmp_frac(frac1, frac2):
    licznik1, mianownik1 = skroc_ulamek(frac1)
    licznik2, mianownik2 = skroc_ulamek(frac2)
    licznik3 = licznik1 * mianownik2
    licznik4= licznik2 * mianownik1
    if licznik3 < licznik4: 
        return -1
    elif licznik3 > licznik4:
        return 1
    else:
        return 0
       # -1 | 0 | +1

def frac2float(frac):
    licznik, mianownik = frac
    if mianownik == 0:
        raise ZeroDivisionError("nie mozna dzielic przez zero")
    return licznik/mianownik          # konwersja do float

import unittest

class TestFractions(unittest.TestCase):

    def setUp(self):
        self.zero = [0, 1]

    def test_add_frac(self):
        self.assertEqual(add_frac([1, 2], [1, 3]), [5, 6])
        self.assertEqual(add_frac([1, 13], [5, 15]), [16, 39])

    def test_sub_frac(self):
        self.assertEqual(sub_frac([1, 2], [1, 4]), [1, 4])
        self.assertEqual(sub_frac([1, 13], [5, 15]), [-10, 39])

    def test_mul_frac(self):
        self.assertEqual(mul_frac([1, 2], [1, 4]), [1, 8])
        self.assertEqual(mul_frac([1, 13], [5, 15]), [1, 39])

    def test_div_frac(self):
        self.assertEqual(div_frac([1, 2], [1, 4]), [2, 1])
        self.assertEqual(div_frac([1, 13], [5, 15]), [3, 13])

    def test_is_positive(self):
        self.assertEqual(is_positive([1, 2]), True)
        self.assertEqual(is_positive([-1, 2]), False)

    def test_is_zero(self): 
        self.assertEqual(is_zero([0, 1]), True)
        self.assertEqual(is_zero([-1, 2]), False)

    def test_cmp_frac(self):
        self.assertEqual(cmp_frac([1, 2], [1, 4]), 1)
        self.assertEqual(cmp_frac([1, 13], [5, 15]), -1)

    def test_frac2float(self):
        self.assertEqual(frac2float([1, 2]), 0.5)
        self.assertEqual(frac2float([10, 2]), 5.0)

    def tearDown(self):
        self.zero = [0, 1]

if __name__ == '__main__':
    unittest.main()     # uruchamia wszystkie testy