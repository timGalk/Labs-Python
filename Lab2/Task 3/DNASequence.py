from Sequence import Sequence
from RNAsequence import RNASequence


class DNASequence(Sequence):
    valid_chars = {'A', 'T', 'C', 'G'}

    def complement(self):
        complement_map = str.maketrans("ATCG", "TAGC")
        return DNASequence(self.identifier, self._data.translate(complement_map))

    def transcribe(self):
        return RNASequence(self.identifier, self._data.replace("T", "U"))

    def find_motif(self, motif: str):
        return [i for i in range(len(self._data) - len(motif) + 1) if self._data[i:i + len(motif)] == motif]