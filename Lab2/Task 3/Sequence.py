from abc import ABC, abstractmethod

class Sequence(ABC):
    """Abstract base class representing a generic biological sequence.

    Attributes:
        identifier (str): A unique identifier for the sequence.
        _data (str): The sequence data containing nucleotide or amino acid codes.

    Methods:
        data (str): Gets or sets the sequence data with validation.
        __len__(): Returns the length of the sequence data.
        __str__(): Returns a FASTA-like string representation of the sequence.
        mutate(position, value): Mutates the sequence at a specified position.
        complement(): Returns the complementary sequence (abstract).
    """

    def __init__(self, identifier: str, data: str):
        """Initializes a Sequence with an identifier and data, ensuring data validity.

        Args:
            identifier (str): Unique identifier for the sequence.
            data (str): Sequence data containing characters defined in valid_chars.

        Raises:
            ValueError: If the data contains invalid characters.
        """
        self.identifier = identifier
        self._data = data
        if not all(char in self.valid_chars for char in data):
            raise ValueError("Invalid characters in sequence data.")

    @property
    def data(self):
        """str: The sequence data, ensuring valid characters upon setting."""
        return self._data

    @data.setter
    def data(self, new_data: str):
        """Sets the sequence data, validating characters against valid_chars.

        Args:
            new_data (str): The new sequence data to set.

        Raises:
            ValueError: If the new data contains invalid characters.
        """
        if all(char in self.valid_chars for char in new_data):
            self._data = new_data
        else:
            raise ValueError("Invalid characters in sequence data.")

    def __len__(self):
        """Calculates the length of the sequence data.

        Returns:
            int: Length of the sequence data.
        """
        return len(self._data)

    def __str__(self):
        """Provides a FASTA-like representation of the sequence.

        Returns:
            str: The sequence in FASTA format, with identifier and data.
        """
        return f">{self.identifier}\n{self._data}"

    def mutate(self, position: int, value: str):
        """Mutates the sequence data at a specified position with a new value.

        Args:
            position (int): The index in the sequence data to mutate.
            value (str): The new character to insert at the specified position.

        Raises:
            IndexError: If the position is out of bounds.
            ValueError: If the value is not in valid_chars.
        """
        if position < 0 or position >= len(self._data):
            raise IndexError("Position out of range.")
        if value not in self.valid_chars:
            raise ValueError("Invalid character for mutation.")
        self._data = self._data[:position] + value + self._data[position + 1:]

    @abstractmethod
    def complement(self):
        """Returns the complementary sequence.

        This is an abstract method to be implemented by subclasses, as the
        complement rules differ between DNA and RNA sequences.

        Returns:
            Sequence: The complementary sequence instance (DNA or RNA).
        """
        pass
