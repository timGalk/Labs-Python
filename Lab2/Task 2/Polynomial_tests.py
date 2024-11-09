import unittest
from Polynomial import Polynomial

class TestPolynomial(unittest.TestCase):
    def test_initialization(self):
        # Test valid initialization
        p = Polynomial([1, -2, 3, 4])
        self.assertEqual(p.coefficients, [1, -2, 3, 4])

        # Test invalid initialization
        with self.assertRaises(ValueError):
            Polynomial("invalid")  # Not a list
        with self.assertRaises(ValueError):
            Polynomial([])  # Empty list
        with self.assertRaises(ValueError):
            Polynomial([1, "two", 3])  # Non-numeric element

    def test_degree(self):
        # Degree of polynomial with coefficients [1, 2, 3] should be 2
        p = Polynomial([1, -2, 3, 4])
        self.assertEqual(p.degree(), 3)

        # Degree of constant polynomial [5] should be 0
        p = Polynomial([5])
        self.assertEqual(p.degree(), 0)

    def test_str(self):
        # Test string representation for a few cases
        p = Polynomial([1, 0, -3, 4])
        self.assertEqual(str(p), "*x^3 - 3*x^2 + 1")

        p = Polynomial([0, 2, 0, 4])
        self.assertEqual(str(p), "4*x^3 + 2*x")

    #     p = Polynomial([0])
    #     self.assertEqual(str(p), "0")
    #
    # def test_call(self):
    #     # Test polynomial evaluation
    #     p = Polynomial([1, 2, 3])  # Represents 1 + 2*x + 3*x^2
    #     self.assertAlmostEqual(p(1), 6)  # 1 + 2*1 + 3*1^2 = 6
    #     self.assertAlmostEqual(p(0), 1)  # 1 + 2*0 + 3*0^2 = 1
    #     self.assertAlmostEqual(p(2), 17) # 1 + 2*2 + 3*2^2 = 17
    #
    # def test_add(self):
    #     # Test addition of two polynomials
    #     p1 = Polynomial([1, 2, 3])  # 1 + 2*x + 3*x^2
    #     p2 = Polynomial([3, 4])     # 3 + 4*x
    #     result = p1 + p2            # Should be 4 + 6*x + 3*x^2
    #     self.assertEqual(result.coefficients, [4, 6, 3])
    #
    # def test_sub(self):
    #     # Test subtraction of two polynomials
    #     p1 = Polynomial([1, 2, 3])  # 1 + 2*x + 3*x^2
    #     p2 = Polynomial([3, 1])     # 3 + 1*x
    #     result = p1 - p2            # Should be -2 + 1*x + 3*x^2
    #     self.assertEqual(result.coefficients, [-2, 1, 3])
    #
    # def test_mul(self):
    #     # Test multiplication of two polynomials
    #     p1 = Polynomial([1, 2])  # 1 + 2*x
    #     p2 = Polynomial([3, 4])  # 3 + 4*x
    #     result = p1 * p2         # Should be 3 + 10*x + 8*x^2
    #     self.assertEqual(result.coefficients, [3, 10, 8])
    #
    # def test_inplace_add(self):
    #     # Test in-place addition
    #     p1 = Polynomial([1, 2, 3])  # 1 + 2*x + 3*x^2
    #     p2 = Polynomial([3, 4])     # 3 + 4*x
    #     p1 += p2                    # Should be 4 + 6*x + 3*x^2
    #     self.assertEqual(p1.coefficients, [4, 6, 3])
    #
    # def test_inplace_sub(self):
    #     # Test in-place subtraction
    #     p1 = Polynomial([1, 2, 3])  # 1 + 2*x + 3*x^2
    #     p2 = Polynomial([3, 1])     # 3 + 1*x
    #     p1 -= p2                    # Should be -2 + 1*x + 3*x^2
    #     self.assertEqual(p1.coefficients, [-2, 1, 3])
    #
    # def test_inplace_mul(self):
    #     # Test in-place multiplication
    #     p1 = Polynomial([1, 2])  # 1 + 2*x
    #     p2 = Polynomial([3, 4])  # 3 + 4*x
    #     p1 *= p2                 # Should be 3 + 10*x + 8*x^2
    #     self.assertEqual(p1.coefficients, [3, 10, 8])

if __name__ == "__main__":
    unittest.main()
