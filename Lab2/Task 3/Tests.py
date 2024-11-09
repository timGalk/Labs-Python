
import unittest
from DNASequence import DNASequence
from RNASequence import RNASequence
from ProteinSeq import ProteinSequence
# from Sequence import Sequence
# DNA Tests
class TestDNASequence(unittest.TestCase):
    def setUp(self):
        self.dna = DNASequence("test_dna", "ATCGATTG")

    def test_len(self):
        self.assertEqual(len(self.dna), 8)

    def test_str(self):
        expected_str = ">test_dna\nATCGATTG"
        self.assertEqual(str(self.dna), expected_str)

    def test_mutate(self):
        self.dna.mutate(0, 'G')
        self.assertEqual(self.dna.data, "GTCGATTG")

    def test_find_motif(self):
        positions = self.dna.find_motif("AT")
        self.assertEqual(positions, [0, 4])

    def test_complement(self):
        complement = self.dna.complement()
        self.assertEqual(complement.data, "TAGCTAAC")

    def test_transcribe(self):
        rna = self.dna.transcribe()
        self.assertTrue(isinstance(rna, RNASequence))
        self.assertEqual(rna.data, "AUCGAUUG")
class TestProteinSequence(unittest.TestCase):

    def test_protein_sequence_creation(self):
        # Create a ProteinSequence object
        seq = ProteinSequence("Protein_1", "MSTVGA")

        # Check the identifier
        self.assertEqual(seq.identifier, "Protein_1")

        # Check the sequence data
        self.assertEqual(seq._data, "MSTVGA")

    def test_find_motif_valid_motif(self):
        seq = ProteinSequence("Protein_2", "MSTVGA")

        # Test for valid motif
        motif = "TV"
        result = seq.find_motif(motif)

        # Should find the motif starting at position 2
        self.assertEqual(result, [2])

    def test_find_motif_multiple_occurrences(self):
        seq = ProteinSequence("Protein_3", "MSTVTVGTVA")

        # Test for motif that appears multiple times
        motif = "TV"
        result = seq.find_motif(motif)

        # Motif "TV" appears starting at positions 2, 4, and 7
        self.assertEqual(result, [2, 4, 7])

    def test_find_motif_no_occurrence(self):
        seq = ProteinSequence("Protein_4", "MSTVGA")

        # Test for motif that does not appear
        motif = "XYZ"


        # No occurrence of "XYZ" in the sequence
        with self.assertRaises(ValueError):
            result = seq.find_motif(motif)


    def test_find_motif_invalid_motif(self):
        seq = ProteinSequence("Protein_5", "MSTVGA")

        # Test for invalid motif with characters not in valid_chars
        motif = "MSTZG"

        # Should raise ValueError
        with self.assertRaises(ValueError):
            seq.find_motif(motif)

    def test_complement_not_implemented(self):
        seq = ProteinSequence("Protein_6", "MSTVGA")

        # Test if calling complement raises NotImplementedError
        with self.assertRaises(NotImplementedError):
            seq.complement()
class TestRNASequence(unittest.TestCase):

    def test_rna_sequence_creation(self):
        # Create an RNASequence object
        seq = RNASequence("RNA_1", "AUGCGAU")

        # Check the identifier
        self.assertEqual(seq.identifier, "RNA_1")

        # Check the sequence data
        self.assertEqual(seq._data, "AUGCGAU")

    def test_complement_valid_sequence(self):
        seq = RNASequence("RNA_2", "AUGCGAU")

        # The complement should return the corresponding RNA bases
        complement_seq = seq.complement()

        self.assertEqual(complement_seq._data, "UACGCUA")
        self.assertEqual(complement_seq.identifier, "RNA_2")

    def test_complement_invalid_characters(self):
        # Should raise ValueError if invalid characters are in the sequence
        with self.assertRaises(ValueError) as context:
            RNASequence("RNA_3", "AUGZGAU")  # Invalid character 'Z'
        self.assertTrue("Invalid characters in sequence" in str(context.exception))

    def test_translate_valid_sequence(self):
        seq = RNASequence("RNA_4", "AUGCUUAAG")

        # Translate the RNA sequence to a protein sequence
        protein_seq = seq.translate()

        # The translated protein sequence should match the expected amino acids
        self.assertEqual(protein_seq._data, "MLK")
        self.assertEqual(protein_seq.identifier, "RNA_4")

    def test_translate_invalid_sequence_length(self):
        seq = RNASequence("RNA_5", "AUGCU")

        # Should raise ValueError if the RNA sequence length is not a multiple of 3
        with self.assertRaises(ValueError) as context:
            seq.translate()
        self.assertTrue("Invalid codon found in RNA sequence during translation." in str(context.exception))

    def test_translate_invalid_codon(self):
        # Should raise ValueError if the RNA sequence contains an invalid codon
        with self.assertRaises(ValueError) as context:
            RNASequence("RNA_6", "AUGXGA")  # Invalid character 'X' in codon
        self.assertTrue("Invalid characters in sequence" in str(context.exception))

    def test_translate_stop_codon(self):
        seq = RNASequence("RNA_7", "AUGUAG")

        # Translate the RNA sequence with stop codon
        protein_seq = seq.translate()

        # Should terminate translation at stop codon and return the protein sequence with 'M'
        self.assertEqual(protein_seq._data, "M")

    def test_complement_not_implemented_for_protein_sequence(self):
        seq = RNASequence("RNA_8", "AUGGCAU")

        # Test complement on RNA sequence and check result is valid
        complement_seq = seq.complement()
        self.assertEqual(complement_seq._data, "UACCGUA")



if __name__ == '__main__':
    unittest.main()

