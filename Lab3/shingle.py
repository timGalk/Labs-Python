import argparse
import sys

from a import shingles

def counter_shingels(arr: list) -> dict:
    """
    Counts the frequencies of elements in `arr` and groups them by frequency.

    Args:
        arr (list): A list of strings.

    Returns:
        dict: A dictionary where keys are frequencies, and values are lists of strings with that frequency.
    """
    # Count frequencies of each unique element in `arr`
    counter = {}
    for element in arr:
        counter[element] = counter.get(element, 0) + 1

    # Group elements by their frequencies
    result = {}
    for key, frequency in counter.items():
        if frequency not in result:
            result[frequency] = []
        result[frequency].append(key)

    return result



def main():

    parser = argparse.ArgumentParser(description="Find the most common k-shingles in the input text.")
    parser.add_argument('-n', type=int, required=True, help="Number of most common shingles to display.")
    parser.add_argument('-k', type=int, required=True, help="Length of each shingle.")
    args = parser.parse_args()
    # n - number of most common shingles to display
    if args.n <= 0:
        raise ValueError("Number of most common shingles must be positive.")
    if args.k <= 0:
        raise ValueError("Impossible to have k greater than number of words ")
    # Read multiline input until EOF
    input_text = sys.stdin.read()
    k_shingles = shingles(input_text, args.k)
    most_common = counter_shingels(k_shingles)
    loop_counter = 0
    for frequency in sorted(most_common.keys(), reverse=True):
        for phrase in most_common[frequency]:
            print(f"{phrase}: {frequency}")
        loop_counter += 1
        if loop_counter == args.n:
            break

if __name__ == "__main__": main()