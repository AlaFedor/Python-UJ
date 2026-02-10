import unittest
from polynomial import Polynomial
from fractions import Fraction

class TestPolynomial(unittest.TestCase):

    def test_init(self):
        p = Polynomial([1, 2, 0, 0, 0]) # 2x+1
        self.assertEqual(p.coeffs, [1, 2])
        self.assertEqual(p.degree(), 1)
        
        p_zero = Polynomial([0, 0]) # 0
        self.assertEqual(p_zero.coeffs, [0])
        self.assertTrue(p_zero.is_zero())

        p_num = Polynomial(5)
        self.assertEqual(p_num.coeffs, [5])
        self.assertEqual(p_num.degree(), 0)

    def test_empty_init(self):
        p = Polynomial([])
        self.assertTrue(p.is_zero())

    def test_addition(self):
        p1 = Polynomial([1, 2, 3]) # 3x^2 + 2x + 1
        p2 = Polynomial([4, 5])    # 5x + 4
        res = p1 + p2
        self.assertEqual(res.coeffs, [5, 7, 3]) # 3x^2 + 7x + 5

        p1 = Polynomial([1, 2, 3]) # 3x^2 + 2x + 1
        p2 = Polynomial([-4, -5])    # -5x - 4
        res = p1 + p2
        self.assertEqual(res.coeffs, [-3, -3, 3]) # 3x^2 - 3x - 3

        res2 = p1 + 10
        self.assertEqual(res2.coeffs, [11, 2, 3]) # 3x^2 + 2x + 11

        res3 = 10 + p1
        self.assertEqual(res3.coeffs, [11, 2, 3])

    def test_subtraction(self):
        p1 = Polynomial([1, 2, 3]) # 3x^2 + 2x + 1
        p2 = Polynomial([0, 0, 3]) # 3x^2
        res = p1 - p2
        self.assertEqual(res.coeffs, [1, 2])  # 2x + 1

        p1 = Polynomial([1, 2, 3]) # 3x^2 + 2x + 1
        p2 = Polynomial([0, -1, 5, -2]) # -2x^3 + 5x^2 -x
        res = p1 - p2
        self.assertEqual(res.coeffs, [1, 3, -2, 2])  # 2x^3 - 2x^2 + 3x + 1
        
        res_zero = p1 - p1
        self.assertTrue(res_zero.is_zero())

        res2 = p1 - 1
        self.assertEqual(res2.coeffs, [0, 2, 3]) # 3x^2 + 2x

        # 5 - (3x^2 + 2x + 1) = -3x^2 - 2x + 4
        res3 = 5 - p1
        self.assertEqual(res3.coeffs, [4, -2, -3])

    def test_multiplication(self):
        p1 = Polynomial([2, 1])   # x + 2
        p2 = Polynomial([-3, 4])  # 4x - 3
        res = p1 * p2
        self.assertEqual(res.coeffs, [-6, 5, 4]) # 4x^2 + 5x - 6

        p1 = Polynomial([1, 2])   # 2x + 1
        p2 = Polynomial([0])  # 0
        res = p1 * p2
        self.assertTrue(res.is_zero())

        res2 = p1 * 10
        self.assertEqual(res2.coeffs, [10, 20]) # 20x + 10

        res3 = 10 * p1
        self.assertEqual(res3.coeffs, [10, 20])

    def test_value(self):
        p = Polynomial([1, 2, 1]) # x^2 + 2x + 1
        # Dla x = 2: 4 + 4 + 1 = 9
        self.assertEqual(p.value(2), 9)
        # Dla x = 0: 0 + 0 + 1 = 1
        self.assertEqual(p.value(0), 1)

    def test_getitem(self):
        p = Polynomial([3, 0, -1]) # -x^2 + 3
        self.assertEqual(p[0], 3)
        self.assertEqual(p[1], 0)
        self.assertEqual(p[2], -1)
        self.assertEqual(p[100], 0) # Wykraczanie poza 

    def test_equality(self):
        p1 = Polynomial([1, 2])
        p2 = Polynomial([1, 2, 0, 0])
        p3 = Polynomial([1, 3])
        
        self.assertTrue(p1 == p2)
        self.assertFalse(p1 == p3)
        self.assertTrue(p1 != p3)

        self.assertTrue(Polynomial([5]) == 5)
        self.assertTrue(5 == Polynomial([5]))
        self.assertFalse(p1 == 1)

        self.assertFalse(p1 == "abc")

    def test_string(self):
        p = Polynomial([1, -2, 3]) # 3x^2 - 2x + 1
        self.assertEqual(str(p), "3x^2 - 2x + 1")
        
        p0 = Polynomial([0])
        self.assertEqual(str(p0), "0")

    def test_float(self):
        p = Polynomial([1.5, 2.5]) # 2.5x + 1.5
        res = p * 2.0
        self.assertEqual(res.coeffs, [3.0, 5.0]) # 5.0x + 3.0

    def test_fractions(self):
            p = Polynomial([Fraction(1, 2), 1]) # x + 1/2
            
            res = p + Fraction(1, 2)
            self.assertEqual(res.coeffs, [1, 1]) # x + 1
            
            res2 = p * Fraction(1, 2) 
            self.assertEqual(res2.coeffs, [Fraction(1, 4), Fraction(1, 2)]) # 1/2x + 1/4

    def test_mixed_types(self):
        p = Polynomial([1,2]) # 2x + 1
        res = p + Fraction(1,2)
        self.assertEqual(res.coeffs, [Fraction(3,2), 2]) # 2x + 3/2


if __name__ == '__main__':
    unittest.main()