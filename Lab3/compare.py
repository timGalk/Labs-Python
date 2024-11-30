import argparse
import re
from  a import shingles



def preprocess_text(text: str, remove_punctuation: bool) -> str:
    """
    Preprocess the text by optionally removing punctuation.

    Args:
        text (str): Input text.
        remove_punctuation (bool): Whether to remove punctuation.

    Returns:
        str: Processed text.
    """
    if remove_punctuation:
        text = re.sub(r'[^\w\s]', '', text)
    return text


def jaccard_similarity(set1: set, set2: set) -> float:
    """
    Calculates the Jaccard similarity between two sets.

    Args:
        set1 (set): First set.
        set2 (set): Second set.

    Returns:
        float: Jaccard similarity (intersection / union).
    """
    if  not  isinstance(set1, set) or not isinstance(set2, set):
        raise TypeError("Both inputs must be sets.")
    intersection = set1 & set2
    union = set1.union(set2)
    return len(intersection) / len(union)


def compare_files(file1: str, file2: str, k: int, remove_punctuation: bool) -> float:
    """
    Compare two files by calculating the Jaccard similarity of their k-shingles.
    Args :
        file1 (str): Path to the first file.
        file2 (str): Path to the second file.
        k (int): Size of the shingles (k-grams).
        remove_punctuation (bool): Whether to remove punctuation from text.
    Returns :
        float: Jaccard similarity of the two files.
    Raises :
        ValueError: If one or both files are empty.
    """
    with open(file1, 'r') as f1, open(file2, 'r') as f2:
        text1 = preprocess_text(f1.read(), remove_punctuation)
        text2 = preprocess_text(f2.read(), remove_punctuation)

    # empty files check
    if not text1 or not text2:
        raise ValueError("One or both files are empty.")

    shingles1 = set(shingles(text1, k))
    shingles2 = set(shingles(text2, k))
    return jaccard_similarity(shingles1, shingles2)



def main():
    parser = argparse.ArgumentParser(description="Compare two text files using Jaccard similarity.")
    parser.add_argument("--query", type=str, required=True, help="Path to the query text file.")
    parser.add_argument("--target", type=str, required=True, help="Path to the target text file.")
    parser.add_argument("-k", type=int, required=True, help="Size of the shingles (k-grams).")
    parser.add_argument("--remove_punctuation", action="store_true", help="Remove punctuation from text.")
    args = parser.parse_args()

    similarity = compare_files(args.query, args.target, args.k, args.remove_punctuation)
    print(f"Jaccard similarity: {similarity:.4f}")


if __name__ == "__main__":
    main()