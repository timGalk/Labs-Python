from DNASequence import DNASequence

def main():
    # Create a DNA sequence instance
    dna_seq = DNASequence(identifier="DNA1", data="ATCGATCG")
    print("Original DNA Sequence:")
    print(dna_seq)

    # Display length of DNA sequence
    print("Length of DNA Sequence:", len(dna_seq))

    # Mutate a base in the DNA sequence
    dna_seq.mutate(2, "G")
    print("Mutated DNA Sequence:")
    print(dna_seq)

    # Find a motif in the DNA sequence
    motif_positions = dna_seq.find_motif("AT")
    print("Positions of motif 'AT' in DNA Sequence:", motif_positions)

    # Complement the DNA sequence
    dna_complement = dna_seq.complement()
    print("Complement DNA Sequence:")
    print(dna_complement)

    # Transcribe the DNA sequence to RNA
    rna_seq = dna_seq.transcribe()
    print("Transcribed RNA Sequence:")
    print(rna_seq)

    # RNA specific operations
    print("\nRNA Sequence Operations:")
    print("Original RNA Sequence:", rna_seq)

    # Mutate the RNA sequence
    rna_seq.mutate(1, "A")
    print("Mutated RNA Sequence:")
    print(rna_seq)

    # Complement the RNA sequence
    rna_complement = rna_seq.complement()
    print("Complement RNA Sequence:")
    print(rna_complement)

    # Translate RNA to Protein
    protein_seq = rna_seq.translate()
    print("Translated Protein Sequence:")
    print(protein_seq)

    # Protein specific operations
    print("\nProtein Sequence Operations:")
    print("Original Protein Sequence:", protein_seq)

    # Find motif in Protein sequence
    protein_motif_positions = protein_seq.find_motif("M")
    print("Positions of motif 'M' in Protein Sequence:", protein_motif_positions)


if __name__ == "__main__":
    main()
