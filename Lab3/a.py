'''Lab 3 Task 1
Descriprions of the functions:

'''

def shingles(t:str, k:int ) -> list:
    """
    Generates k-shingles (k-grams) from a list of tokens.
    Args:
        t: string of tokens
        k: integer, number of shingles

    Returns:
        list of shingles
    Rises:
        TypeError: if t is not a string
        ValueError: if k is greater than the number of words in
    """
    if not isinstance(t, str) or t.isspace() or t == "":
        raise TypeError("t must be a non-empty string")
    if not isinstance(k, int):
        raise TypeError("k must be an integer")
    if k > len(t.split(' ')) or k <= 0:
        raise ValueError("k must be less than or equal to the number of words in t and greater than 0")

        # Shingles generation
    word_arr = t.split(' ')
    result = []
    for i in range(len(word_arr) - k + 1):
        result.append(" ".join(word_arr[i:i + k]))
    return result


def main ():
    print(shingles("one two three four five", 3))
    print(shingles("Hello world", 2))
    print(shingles("This is a test. This is only a test", 2))

if __name__ == "__main__": main()