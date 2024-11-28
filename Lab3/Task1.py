'''Lab 3 Task 1
Descriprions of the functions:

'''

def shingles(t:str, k:int ) -> list:
    """
    Args:
        t: string of tokens
        k: integer, number of shingles

    Returns:
        list of shingles
    Rises:
        TypeError: if t is not a string
        ValueError: if k is greater than the number of words in t


    """
    # errors check
    if (not isinstance(t, str)) or (t.isspace()) or (t == ""):
        raise TypeError("t must be a non-empty string")
    if (not isinstance(k, int)):
        raise TypeError("k must be an integer")
    if (k > len(t.split(' '))) or (k <=  0):
        raise ValueError("k must be less than the number of words in t") \
     # shingles
    word_arr = t.split(' ')
    result = []
    for i in range(len(word_arr)):
        if i + k >= len(word_arr):
            break
        result.append(" ".join(word_arr[i:i + k]))
    return result


def main ():
    print(shingles("one two three four five ", 3))

if __name__ == "__main__": main()