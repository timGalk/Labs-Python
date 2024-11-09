from Sequence import Sequence

class ProteinSequence(Sequence):
    valid_chars = {'A', 'R', 'N', 'D', 'C', 'Q', 'E', 'G', 'H', 'I', 'L', 'K', 'M', 'F', 'P', 'S', 'T', 'W', 'Y', 'V', '*'}

    def complement(self):
        raise NotImplementedError("Complement not defined for protein sequences.")

    def find_motif(self, motif: str):
        return [i for i in range(len(self._data) - len(motif) + 1) if self._data[i:i + len(motif)] == motif]