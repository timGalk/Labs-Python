class Polynomial:
    """Represents a polynomial with basic arithmetic operations.

    Attributes:
        coefficients (list): List of coefficients, where the i-th element represents the
            coefficient for the x^i term in the polynomial.

    Methods:
        degree(): Returns the degree of the polynomial.
        __str__(): Returns the string representation of the polynomial.
        __call__(x): Evaluates the polynomial at a given value of x.
        __add__(other): Adds another Polynomial to this one.
        __sub__(other): Subtracts another Polynomial from this one.
        __mul__(other): Multiplies this Polynomial by another Polynomial.
        __iadd__(other): Adds another Polynomial to this one using +=.
        __isub__(other): Subtracts another Polynomial from this one using -=.
        __imul__(other): Multiplies this Polynomial by another Polynomial using *=.

    Raises:
        ValueError: If coefficients is not a non-empty list of numbers or if an operation
            is attempted with a non-Polynomial object.
    """

    def __init__(self, coefficients: list):
        """Initializes a Polynomial instance with given coefficients.

        Args:
            coefficients (list): List of coefficients for each term, where the i-th element
                represents the coefficient for the x^i term.

        Raises:
            ValueError: If coefficients is not a non-empty list of numbers.
        """
        if not (isinstance(coefficients, list) and len(coefficients) > 0 and
                all(isinstance(c, (int, float)) for c in coefficients)):
            raise ValueError("Coefficients must be a non-empty list of numbers.")
        self.coefficients = coefficients

    def degree(self) -> int:
        """Returns the degree of the polynomial.

        Returns:
            int: The degree of the polynomial, calculated as the highest exponent with a
                non-zero coefficient.
        """
        return len(self.coefficients) - 1

    def __str__(self) -> str:
        """Generates a string representation of the polynomial.

        Returns:
            str: The polynomial in human-readable format, such as "3*x^2 + 2*x + 1".
        """
        terms = []
        for power, coef in enumerate(reversed(self.coefficients)):
            if coef != 0:
                term = f"{coef}" if power == 0 else (f"x^{power}" if power > 1 else "x")
                if coef != 1 or power == 0:
                    term = f"{coef}*{term}" if power > 0 else f"{coef}"
                terms.append(term)
        return " + ".join(reversed(terms)) if terms else "0"

    def __call__(self, x: float) -> float:
        """Evaluates the polynomial at a given value of x.

        Args:
            x (float): The value at which to evaluate the polynomial.

        Returns:
            float: The result of the polynomial evaluation.
        """
        return sum(coef * (x ** i) for i, coef in enumerate(self.coefficients))

    def __add__(self, other: "Polynomial") -> "Polynomial":
        """Adds another Polynomial to this Polynomial.

        Args:
            other (Polynomial): The Polynomial to add.

        Returns:
            Polynomial: A new Polynomial representing the sum.

        Raises:
            ValueError: If other is not an instance of Polynomial.
        """
        if not isinstance(other, Polynomial):
            raise ValueError("Can only add another Polynomial.")
        max_len = max(len(self.coefficients), len(other.coefficients))
        result_coeffs = [
            (self.coefficients[i] if i < len(self.coefficients) else 0) +
            (other.coefficients[i] if i < len(other.coefficients) else 0)
            for i in range(max_len)
        ]
        return Polynomial(result_coeffs)

    def __sub__(self, other: "Polynomial") -> "Polynomial":
        """Subtracts another Polynomial from this Polynomial.

        Args:
            other (Polynomial): The Polynomial to subtract.

        Returns:
            Polynomial: A new Polynomial representing the difference.

        Raises:
            ValueError: If other is not an instance of Polynomial.
        """
        if not isinstance(other, Polynomial):
            raise ValueError("Can only subtract another Polynomial.")
        max_len = max(len(self.coefficients), len(other.coefficients))
        result_coeffs = [
            (self.coefficients[i] if i < len(self.coefficients) else 0) -
            (other.coefficients[i] if i < len(other.coefficients) else 0)
            for i in range(max_len)
        ]
        return Polynomial(result_coeffs)

    def __mul__(self, other: "Polynomial") -> "Polynomial":
        """Multiplies this Polynomial by another Polynomial.

        Args:
            other (Polynomial): The Polynomial to multiply.

        Returns:
            Polynomial: A new Polynomial representing the product.

        Raises:
            ValueError: If other is not an instance of Polynomial.
        """
        if not isinstance(other, Polynomial):
            raise ValueError("Can only multiply by another Polynomial.")
        result_coeffs = [0] * (len(self.coefficients) + len(other.coefficients) - 1)
        for i, coef1 in enumerate(self.coefficients):
            for j, coef2 in enumerate(other.coefficients):
                result_coeffs[i + j] += coef1 * coef2
        return Polynomial(result_coeffs)

    def __iadd__(self, other: "Polynomial") -> "Polynomial":
        """Performs in-place addition of another Polynomial.

        Args:
            other (Polynomial): The Polynomial to add.

        Returns:
            Polynomial: The modified Polynomial after addition.
        """
        result = self + other
        self.coefficients = result.coefficients
        return self

    def __isub__(self, other: "Polynomial") -> "Polynomial":
        """Performs in-place subtraction of another Polynomial.

        Args:
            other (Polynomial): The Polynomial to subtract.

        Returns:
            Polynomial: The modified Polynomial after subtraction.
        """
        result = self - other
        self.coefficients = result.coefficients
        return self

    def __imul__(self, other: "Polynomial") -> "Polynomial":
        """Performs in-place multiplication with another Polynomial.

        Args:
            other (Polynomial): The Polynomial to multiply.

        Returns:
            Polynomial: The modified Polynomial after multiplication.
        """
        result = self * other
        self.coefficients = result.coefficients
        return self

def main():
    p1 = Polynomial([1, 0, 3, 4])
    print(str(p1))
    print(p1(2))

if __name__ == "__main__":
    main()
