import argparse
import sys
from collections import Counter
from a import shingles

# The advice of the use of the Counter class was taken from ChatGPT for the prompt "Find the most common k-shingles
# in the input text."

def counter_shingles(arr: list) -> dict:
    """
    Counts the frequencies of elements in `arr`.

    Args:
        arr (list): A list of strings.

    Returns:
        dict: A dictionary where keys are strings, and values are their frequencies.
    """
    return Counter(arr)

def main():
    parser = argparse.ArgumentParser(description="Find the most common k-shingles in the input text.")
    parser.add_argument('-n', type=int, required=True, help="Number of most common shingles to display.")
    parser.add_argument('-k', type=int, required=True, help="Length of each shingle.")
    args = parser.parse_args()

    # Input validation
    if args.n <= 0:
        raise ValueError("Number of most common shingles (-n) must be positive.")
    if args.k <= 0:
        raise ValueError("Length of shingles (-k) must be positive.")

    # Read multiline input until EOF
    input_text = sys.stdin.read().strip()
    if not input_text:
        raise ValueError("Input text cannot be empty.")

        # Generate shingles and count frequencies
    k_shingles = shingles(input_text, args.k)
    shingles_count = counter_shingles(k_shingles)

    most_common = shingles_count.most_common(args.n)

    print()
     # Print results
    for phrase, frequency in most_common:
        print(f"{phrase}: {frequency}")

if __name__ == "__main__":
    main()
