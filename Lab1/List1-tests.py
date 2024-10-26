import unittest
from datetime import datetime
from List1 import weekday, segment_length, random_walk, dec2bin, dna_complement, find_genes

# The test
class TestWeekday(unittest.TestCase):
    def test_valid_dates(self):
        self.assertEqual(weekday(1, 1, 2024), "Monday")
        self.assertEqual(weekday(4, 7, 1776), "Thursday")
        self.assertEqual(weekday(25, 12, 2023), "Monday")

    def test_leap_year(self):
        self.assertEqual(weekday(29, 2, 2024), "Thursday")  # 2024 is a leap year
        with self.assertRaises(ValueError):
            weekday(29, 2, 2023)  # 2023 is not a leap year

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            weekday("1", 1, 2024)
        with self.assertRaises(ValueError):
            weekday(1, 13, 2024)  # Invalid month
        with self.assertRaises(ValueError):
            weekday(32, 1, 2024)  # Invalid day
        with self.assertRaises(ValueError):
            weekday(1, 1, -1)  # Invalid year
        with self.assertRaises(ValueError):
            weekday(1, 1, datetime.now().year + 101)  # Too far in future


class TestSegmentLength(unittest.TestCase):
    def test_overlapping_segments(self):
        self.assertEqual(segment_length(1, 5, 3, 7), (3, 5))
        self.assertEqual(segment_length(0, 10, 5, 15), (5, 10))

    def test_non_overlapping_segments(self):
        self.assertIsNone(segment_length(1, 3, 4, 6))
        self.assertIsNone(segment_length(10, 20, 0, 5))

    def test_invalid_inputs(self):
        with self.assertRaises(ValueError):
            segment_length("1", 5, 3, 7)
        with self.assertRaises(ValueError):
            segment_length(None, 5, 3, 7)


class TestRandomWalk(unittest.TestCase):
    def test_valid_steps(self):
        result = random_walk(5)
        self.assertEqual(len(result), 6)  # 5 steps plus starting point
        self.assertEqual(result[0], (0, 0))  # Should start at origin

        # Test each step is valid (differs by at most 1 in each direction)
        for i in range(1, len(result)):
            dx = abs(result[i][0] - result[i - 1][0])
            dy = abs(result[i][1] - result[i - 1][1])
            self.assertLessEqual(dx, 1)
            self.assertLessEqual(dy, 1)

    def test_invalid_inputs(self):
        with self.assertRaises(ValueError):
            random_walk(0)
        with self.assertRaises(ValueError):
            random_walk(-1)
        with self.assertRaises(ValueError):
            random_walk(1.5)


class TestDec2Bin(unittest.TestCase):
    def test_valid_numbers(self):
        self.assertEqual(dec2bin(0), "0")
        self.assertEqual(dec2bin(1), "1")
        self.assertEqual(dec2bin(2), "10")
        self.assertEqual(dec2bin(8), "1000")
        self.assertEqual(dec2bin(15), "1111")

    def test_invalid_inputs(self):
        with self.assertRaises(ValueError):
            dec2bin(-1)
        with self.assertRaises(ValueError):
            dec2bin(1.5)
        with self.assertRaises(ValueError):
            dec2bin("123")


class TestDNAComplement(unittest.TestCase):
    def test_valid_sequences(self):
        self.assertEqual(dna_complement("ATCG"), "TAGC")
        self.assertEqual(dna_complement("AAAA"), "TTTT")
        self.assertEqual(dna_complement("GCTA"), "CGAT")
        self.assertEqual(dna_complement("atcg"), "TAGC")

    def test_invalid_inputs(self):
        with self.assertRaises(ValueError):
            dna_complement("ATCX")  # Invalid character
        with self.assertRaises(ValueError):
            dna_complement("AT CG")  # Space not allowed
        with self.assertRaises(ValueError):
            dna_complement(123)  # Non-string input
        with self.assertRaises(ValueError):
            dna_complement("")


class TestFindGenes(unittest.TestCase):
    def test_valid_genes(self):
        self.assertTrue(find_genes("ATGTAG"))  # Simplest valid gene
        self.assertTrue(find_genes("ATGAAATAG"))  # Valid gene with content
        self.assertTrue(find_genes("ATGAAATGA"))  # Valid gene with TGA stop codon

    def test_invalid_genes(self):
        self.assertFalse(find_genes("ATGAAA"))  # No stop codon
        self.assertFalse(find_genes("TAAATGTAG"))  # Starts with stop codon
        self.assertFalse(find_genes("ATGTAGTAG"))  # Multiple stop codons
        self.assertFalse(find_genes("ATGTAGA"))  # Length not multiple of 3
        self.assertFalse(find_genes("AAATAG"))  # No start codon

    def test_invalid_inputs(self):
        with self.assertRaises(ValueError):
            find_genes("ATGX")  # Invalid character
        with self.assertRaises(ValueError):
            find_genes("ATG TAG")  # Space not allowed
        with self.assertRaises(ValueError):
            find_genes(123)  # Non-string input


if __name__ == '__main__':
    unittest.main()