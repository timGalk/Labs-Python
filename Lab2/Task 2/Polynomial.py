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
            str: The polynomial in human-readable format, such as "3x² + 2x + 1".
        """
        # Unicode superscript mapping for exponents up to 9
        # Warning the provided code was developed by ChatGPT for the prompt :{initial code} modify the code with
        # the
        # https://en.wikipedia.org/wiki/Superscript
        superscripts = "⁰¹²³⁴⁵⁶⁷⁸⁹"

        terms = []
        for power, coef in enumerate(reversed(self.coefficients)):
            if coef != 0:
                # Choose the term format based on power
                if power == 0:
                    term = f"{coef}"
                elif power == 1:
                    term = f"{coef}x" if coef != 1 else "x"
                elif power < 10:
                    term = f"{coef}x{''.join(superscripts[int(digit)] for digit in str(power))}" if coef != 1 \
                        else f"x{''.join(superscripts[int(digit)] for digit in str(power))}"
                else:
                    term = f"{coef}x^{power}" if coef != 1 else f"x^{power}"

                terms.append(term)

        return " + ".join(reversed(terms)) if terms else "0"

    def __call__(self, x: float) -> float:
        """Evaluates the polynomial at a given value of x.

        Args:
            x (float): The value at which to evaluate the polynomial.

        Returns:
            float: The result of the polynomial evaluation.
        """
        result = 0.0
        power = len(self.coefficients) - 1  # Start with highest power
        for coeff in self.coefficients:
            result += coeff * (x ** power)
            power -= 1
        return result

    def __add__(self, other: "Polynomial") -> "Polynomial":
        """Adds another Polynomial to this Polynomial.

        Args:
            other (Polynomial): The Polynomial to add.

        Returns:
            Polynomial: A new Polynomial representing the sum.

        Raises:
            ValueError: If other is not an instance of Polynomial.
        """
        if not isinstance(other, type(self)):
            raise ValueError("Can only add Polynomial to another Polynomial")

        # Get the degree of each polynomial
        len1 = len(self.coefficients)
        len2 = len(other.coefficients)

        # Initialize result with zeros for the maximum degree
        max_len = max(len1, len2)
        new_coeffs = [0] * max_len

        # Add coefficients from first polynomial
        offset = max_len - len1
        for i in range(len1):
            new_coeffs[i + offset] = self.coefficients[i]

        # Add coefficients from second polynomial
        offset = max_len - len2
        for i in range(len2):
            new_coeffs[i + offset] += other.coefficients[i]

        # Create a new polynomial with the summed coefficients
        return type(self)(new_coeffs)

    def __sub__(self, other: "Polynomial") -> "Polynomial":
        """Subtracts another Polynomial from this Polynomial.

        Args:
            other (Polynomial): The Polynomial to subtract.

        Returns:
            Polynomial: A new Polynomial representing the difference.

        Raises:
            ValueError: If other is not an instance of Polynomial.
        """
        if not isinstance(other, type(self)):
            raise ValueError("Can only subtract Polynomial from another Polynomial")

        # Get the degree of each polynomial
        len1 = len(self.coefficients)
        len2 = len(other.coefficients)

        # Initialize result with zeros for the maximum degree
        max_len = max(len1, len2)
        new_coeffs = [0] * max_len

        # Add coefficients from first polynomial
        offset = max_len - len1
        for i in range(len1):
            new_coeffs[i + offset] = self.coefficients[i]

        # Subtract coefficients from second polynomial
        offset = max_len - len2
        for i in range(len2):
            new_coeffs[i + offset] -= other.coefficients[i]

        # Create a new polynomial with the differenced coefficients
        return type(self)(new_coeffs)

    def __mul__(self, other: "Polynomial") -> "Polynomial":
        """Multiplies this Polynomial by another Polynomial.

        Args:
            other (Polynomial): The Polynomial to multiply.

        Returns:
            Polynomial: A new Polynomial representing the product.

        Raises:
            ValueError: If other is not an instance of Polynomial.
        """
        if not isinstance(other, type(self)):
            raise ValueError("Can only multiply Polynomial by another Polynomial")

        # Get the lengths of both polynomials
        len1 = len(self.coefficients)
        len2 = len(other.coefficients)

        # The degree of the product will be the sum of the degrees
        # Initialize result array with zeros
        result_length = len1 + len2 - 1
        new_coeffs = [0] * result_length

        # Multiply each term of self by each term of other
        # Remember coefficients are in descending order
        for i in range(len1):
            for j in range(len2):
                # When multiplying terms, add their powers
                # The power at position i is (len1 - 1 - i)
                # The power at position j is (len2 - 1 - j)
                power_sum = (len1 - 1 - i) + (len2 - 1 - j)
                # This sum corresponds to position (result_length - 1 - power_sum) in new_coeffs
                pos = result_length - 1 - power_sum
                new_coeffs[pos] += self.coefficients[i] * other.coefficients[j]

        return type(self)(new_coeffs)

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
    # p1 = Polynomial([1, 0, 3, 4])
    # print(str(p1))
    # print(p1(2))
    p1 = Polynomial([3, -2, 1])
    print(str(p1))
    p2 = Polynomial([0, 2, 4])
    p1 += p2
    print(str(p1))

if __name__ == "__main__":
    main()
