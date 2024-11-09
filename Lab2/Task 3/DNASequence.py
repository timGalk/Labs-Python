from Sequence import Sequence
from RNASequence import RNASequence
# Formatig to Google style was performed by AI
class DNASequence(Sequence):
    """Class representing a DNA sequence, derived from the abstract Sequence class.

    Attributes:
        identifier (str): Unique identifier for the DNA sequence.
        _data (str): Sequence data containing DNA nucleotides (A, T, C, G).
        valid_chars (set): Set of valid characters for DNA sequences.
    """

    valid_chars = {'A', 'T', 'C', 'G'}

    def complement(self):
        """Generates the complementary DNA sequence.

        The complement is calculated using standard DNA base-pairing rules:
        A ↔ T and C ↔ G.

        Returns:
            DNASequence: A new DNASequence instance representing the complementary sequence.

        Raises:
            ValueError: If the sequence data contains invalid characters.
        """
        complement_map = str.maketrans("ATCG", "TAGC")
        complement_data = self._data.translate(complement_map)
        return DNASequence(self.identifier, complement_data)

    def transcribe(self):
        """Transcribes the DNA sequence into an RNA sequence.

        In transcription, all occurrences of thymine (T) are replaced with uracil (U).

        Returns:
            RNASequence: A new RNASequence instance with the transcribed RNA data.
        """
        rna_data = self._data.replace("T", "U")
        return RNASequence(self.identifier, rna_data)

    def find_motif(self, motif: str):
        """Finds all starting positions of a motif within the DNA sequence.

        Args:
            motif (str): The nucleotide sequence motif to search for within the DNA sequence.

        Returns:
            list[int]: A list of starting positions where the motif is found within the DNA sequence.

        Raises:
            ValueError: If the motif contains invalid characters not defined in valid_chars.
        """
        # Validate that all characters in the motif are valid nucleotides
        if not all(char in self.valid_chars for char in motif):
            raise ValueError("Motif contains invalid characters for DNA sequence.")

        # Find all positions where the motif occurs in the sequence
        return [
            i for i in range(len(self._data) - len(motif) + 1)
            if self._data[i:i + len(motif)] == motif
        ]
