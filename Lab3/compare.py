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
    Calculate the Jaccard similarity between two sets.

    Args:
        set1 (set): First set.
        set2 (set): Second set.

    Returns:
        float: Jaccard similarity (intersection / union).
    """
    intersection = set1 & set2
    union = set1 | set2
    return len(intersection) / len(union)


def compare_files(file1: str, file2: str, k: int, remove_punctuation: bool) -> float:
    """
    Compare two files by calculating the Jaccard similarity of their k-shingles.
    """
    with open(file1, 'r') as f1, open(file2, 'r') as f2:
        text1 = preprocess_text(f1.read(), remove_punctuation)
        text2 = preprocess_text(f2.read(), remove_punctuation)

    tokens1 = text1.split()
    tokens2 = text2.split()

    if not tokens1 or not tokens2:
        raise ValueError("One or both files have no valid tokens for comparison.")

    shingles1 = set(shingles(tokens1, k))
    shingles2 = set(shingles(tokens2, k))
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