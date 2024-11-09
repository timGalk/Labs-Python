import unittest
from Polynomial import Polynomial


class TestPolynomial(unittest.TestCase):
    def setUp(self):
        # Create test polynomials that will be used across multiple tests
        self.p1 = Polynomial([3, 2, 1])  # 3x² + 2x + 1
        self.p2 = Polynomial([1, 0, -1])  # x² - 1
        self.p3 = Polynomial([1, 1])  # x + 1
        self.p4 = Polynomial([2, 0, 0])  # 2x²
        self.p5 = Polynomial([1, -2, 3, 4])  # 1x³ + -2x² + 3x + 4
        self.zero = Polynomial([0])  # 0

    def test_initialization(self):
        # Test valid initialization
        p1 = Polynomial([3, 2, 1])  # Should work fine

        # Test invalid initialization
        with self.assertRaises(ValueError):
            Polynomial("invalid")  # Not a list
        with self.assertRaises(ValueError):
            Polynomial([])  # Empty list
        with self.assertRaises(ValueError):
            Polynomial([1, "two", 3])  # Non-numeric element

    def test_degree(self):
        # Test degree calculation
        self.assertEqual(self.p1.degree(), 2)
        self.assertEqual(self.p2.degree(), 2)
        self.assertEqual(self.p3.degree(), 1)
        self.assertEqual(self.p4.degree(), 2)
        self.assertEqual(self.p5.degree(), 3)
        self.assertEqual(self.zero.degree(), 0)

    def test_str(self):
        # Test string representation for a few cases
        self.assertEqual(str(self.p1), "3x² + 2x + 1")
        self.assertEqual(str(self.p2), "x² + -1")
        self.assertEqual(str(self.p3), "x + 1")
        self.assertEqual(str(self.p4), "2x²")
        self.assertEqual(str(self.p5), "x³ + -2x² + 3x + 4")

        p = Polynomial([0])
        self.assertEqual(str(p), "0")

    def test_call(self):
        # Test polynomial evaluation
        p = Polynomial([1, 2, 3])  # Represents 1*x^2 + 2*x + 3
        self.assertAlmostEqual(p(1), 6)  # 1*1^2 + 2*1 + 3 = 6
        self.assertAlmostEqual(p(0), 3)  # 1*0^2 + 2*0 + 3 = 3
        self.assertAlmostEqual(p(2), 11)  # 1*2^2 + 2*2 + 3 = 11

    def test_add(self):
        # Test basic addition
        result = self.p1 + self.p2  # (3x² + 2x + 1) + (x² - 1)
        self.assertEqual(result.coefficients, [4, 2, 0])  # 4x² + 2x

        # Test addition with different degrees
        result = self.p1 + self.p3  # (3x² + 2x + 1) + (x + 1)
        self.assertEqual(result.coefficients, [3, 3, 2])  # 3x² + 3x + 2

        # Test addition with zero
        result = self.p1 + self.zero
        self.assertEqual(result.coefficients, self.p1.coefficients)

        # Test adding polynomials of very different degrees
        result = self.p4 + self.p3  # (2x²) + (x + 1)
        self.assertEqual(result.coefficients, [2, 1, 1])  # 2x² + x + 1

        # Test type error
        with self.assertRaises(ValueError):
            result = self.p1 + "not a polynomial"

    def test_sub(self):
        # Test basic subtraction
        result = self.p1 - self.p2  # (3x² + 2x + 1) - (x² - 1)
        self.assertEqual(result.coefficients, [2, 2, 2])  # 2x² + 2x + 2

        # Test subtraction with different degrees
        result = self.p1 - self.p3  # (3x² + 2x + 1) - (x + 1)
        self.assertEqual(result.coefficients, [3, 1, 0])  # 3x² + x

        # Test subtraction with zero
        result = self.p1 - self.zero
        self.assertEqual(result.coefficients, self.p1.coefficients)

        # Test subtracting polynomials of very different degrees
        result = self.p4 - self.p3  # (2x²) - (x + 1)
        self.assertEqual(result.coefficients, [2, -1, -1])  # 2x² - x - 1

        # Test type error
        with self.assertRaises(ValueError):
            result = self.p1 - "not a polynomial"


if __name__ == "__main__":
    unittest.main()