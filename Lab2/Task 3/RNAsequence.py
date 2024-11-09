from Sequence import Sequence
from ProteinSeq import ProteinSequence


class RNASequence(Sequence):
    """Class representing an RNA sequence, derived from the abstract Sequence class.

    Attributes:
        identifier (str): Unique identifier for the RNA sequence.
        _data (str): Sequence data containing RNA nucleotides (A, U, C, G).
        valid_chars (set): Set of valid characters for RNA sequences.
    """

    valid_chars = {'A', 'U', 'C', 'G'}

    def complement(self) -> 'RNASequence':
        """Generates the complementary RNA sequence.

        The complement is calculated using standard RNA base-pairing rules:
        A ↔ U and C ↔ G.

        Returns:
            RNASequence: A new RNASequence instance representing the complementary sequence.

        Raises:
            ValueError: If the sequence data contains invalid characters.
        """
        complement_map = str.maketrans("AUCG", "UAGC")
        complement_data = self._data.translate(complement_map)
        return RNASequence(self.identifier, complement_data)

    def translate(self) -> 'ProteinSequence':
        """Translates the RNA sequence into a protein sequence.

        Translation uses a simplified codon table to convert each triplet (codon) in the
        RNA sequence to an amino acid in the resulting protein sequence. Translation
        terminates when a stop codon (* symbol) is encountered.

        Returns:
            ProteinSequence: A new ProteinSequence instance with the translated amino acid sequence.

        Raises:
            ValueError: If the sequence length is not a multiple of 3 or if there is an invalid codon.
        """
        # Codon table for translation from RNA to protein was taken from
        # https://github.com/AndrewZoldy/lecture6/blob/e42eb996336b0faafe4f5d3c3f5400b4801a6f60/sequence_worker.py
        codon_table = {
            'GCU': 'A', 'GCC': 'A', 'GCA': 'A', 'GCG': 'A', 'UUA': 'L', 'UUG': 'L',
            'CUU': 'L', 'CUC': 'L', 'CUA': 'L', 'CUG': 'L', 'CGU': 'R', 'CGC': 'R',
            'CGA': 'R', 'CGG': 'R', 'AGA': 'R', 'AGG': 'R', 'AAA': 'K', 'AAG': 'K',
            'AAU': 'N', 'AAC': 'N', 'AUG': 'M', 'GAU': 'D', 'GAC': 'D', 'UUU': 'F',
            'UUC': 'F', 'UGU': 'C', 'UGC': 'C', 'CCU': 'P', 'CCC': 'P', 'CCA': 'P',
            'CCG': 'P', 'CAA': 'Q', 'CAG': 'Q', 'UCU': 'S', 'UCC': 'S', 'UCA': 'S',
            'UCG': 'S', 'AGU': 'S', 'AGC': 'S', 'GAA': 'E', 'GAG': 'E', 'ACU': 'T',
            'ACC': 'T', 'ACA': 'T', 'ACG': 'T', 'GGU': 'G', 'GGC': 'G', 'GGA': 'G',
            'GGG': 'G', 'UGG': 'W', 'CAU': 'H', 'CAC': 'H', 'UAU': 'Y', 'UAC': 'Y',
            'AUU': 'I', 'AUC': 'I', 'AUA': 'I', 'GUU': 'V', 'GUC': 'V', 'GUA': 'V',
            'GUG': 'V', 'UAG': '*', 'UGA': '*', 'UAA': '*'
        }

        # Check that the RNA sequence length is a multiple of 3
        if len(self._data) % 3 != 0:
            raise ValueError("RNA sequence length must be a multiple of 3 for translation.")

        # Translate the RNA sequence to a protein sequence
        protein_sequence = ''.join(
            codon_table.get(self._data[i:i + 3], '') for i in range(0, len(self._data), 3)
        )

        # Handle case where codon is not found in the codon table
        if '' in protein_sequence:
            raise ValueError("Invalid codon found in RNA sequence during translation.")

        return ProteinSequence(self.identifier, protein_sequence)
