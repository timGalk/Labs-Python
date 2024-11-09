from Sequence import Sequence

class ProteinSequence(Sequence):
    """Class representing a protein sequence, derived from the abstract Sequence class.

    Attributes:
        identifier (str): Unique identifier for the protein sequence.
        _data (str): Sequence data containing protein amino acid codes.
        valid_chars (set): Set of valid characters for protein sequences, including standard
                           amino acids and stop codon '*'.
    """

    valid_chars = {'A', 'R', 'N', 'D', 'C', 'Q', 'E', 'G', 'H', 'I', 'L', 'K', 'M', 'F',
                   'P', 'S', 'T', 'W', 'Y', 'V', '*'}

    def complement(self):
        """Raises an error, as protein sequences do not have a complementary sequence.

        Raises:
            NotImplementedError: Always raised, as the complement operation is not applicable to proteins.
        """
        raise NotImplementedError("Complement not defined for protein sequences.")

    def find_motif(self, motif: str) -> list[int]:
        """Finds all starting positions of a motif within the protein sequence.

        Args:
            motif (str): The amino acid sequence motif to search for within the protein sequence.

        Returns:
            list[int]: A list of starting positions where the motif is found within the protein sequence.

        Raises:
            ValueError: If the motif contains invalid characters not defined in valid_chars.
        """
        # Validate that all characters in the motif are valid amino acids
        if not all(char in self.valid_chars for char in motif):
            raise ValueError("Motif contains invalid characters for protein sequence.")

        # Find all positions where the motif occurs in the sequence
        return [
            i for i in range(len(self._data) - len(motif) + 1)
            if self._data[i:i + len(motif)] == motif
        ]
