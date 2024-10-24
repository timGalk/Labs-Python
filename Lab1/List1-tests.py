
import unittest
from List1 import weekday, segment_length, random_walk, dec2bin, dna_complement, find_genes


class TestTasks(unittest.TestCase):

    # Test Task 1: weekday
    def test_weekday(self):
        self.assertEqual(weekday(10, 10, 2024), "Thursday")
        self.assertEqual(weekday(1, 1, 2000), "Saturday")
        self.assertEqual(weekday(25, 12, 2023), "Monday")

    # Test Task 2: segment_length
    def test_segment_length(self):
        self.assertEqual(segment_length(1, 5, 3, 7), (3, 5))
        self.assertEqual(segment_length(2, 6, 8, 10), None)
        self.assertEqual(segment_length(-5, 0, -3, 2), (-3, 0))
        self.assertEqual(segment_length(5, 5, 5, 5), None)  # No intersection

    # Test Task 3: random_walk
    def test_random_walk(self):
        steps = 5
        walk = random_walk(steps)
        self.assertEqual(len(walk), steps + 1)
        self.assertEqual(walk[0], (0, 0))
        # Check if each step is adjacent (no more than 1 unit away)
        for i in range(1, len(walk)):
            self.assertTrue(abs(walk[i][0] - walk[i - 1][0]) <= 1)
            self.assertTrue(abs(walk[i][1] - walk[i - 1][1]) <= 1)

    # Test Task 4: dec2bin
    def test_dec2bin(self):
        self.assertEqual(dec2bin(42), "101010")
        self.assertEqual(dec2bin(0), "0")
        self.assertEqual(dec2bin(1), "1")
        self.assertEqual(dec2bin(255), "11111111")

    # Test Task 5: dna_complement
    def test_dna_complement(self):
        self.assertEqual(dna_complement("ATGC"), "TACG")
        self.assertEqual(dna_complement("GATTACA"), "CTAATGT")
        self.assertEqual(dna_complement(""), "")
        self.assertEqual(dna_complement("ATGCX"), "X is not a valid nucleotide. Please check your input.")

    # Test Task 6: find_genes
    def test_find_genes(self):
        self.assertTrue(find_genes("ATGAAATAG"))
        self.assertFalse(find_genes("ATGAAA"))
        self.assertFalse(find_genes("ATGAAATA"))
        self.assertFalse(find_genes("GTGAAATAG"))  # Missing start codon
        self.assertTrue(find_genes("ATGCCCCTAA"))


if __name__ == "__main__":
    unittest.main()
