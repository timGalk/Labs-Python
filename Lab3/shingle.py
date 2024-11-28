import argparse as ap

from sortedcontainers import SortedSet

from shingles import shingles

def counter (arr: list) -> dict:

    # counter has a struclure {key: value - list[str]}
    #very specific thing : if two keys has the same value

    unique_phrases_set = set(arr)
    counter = {}

    for combination in unique_phrases_set:
        if combination not in counter.keys():
            counter[combination] = 1
        else:
            counter[combination] += 1

     # the counter of the most popular phrase
    the_most_popular_phrase = max(counter.values())
    result = set()
    for key in counter.keys():
        if counter[key] == the_most_popular_phrase:
            result.add(key)

    return result


def main():
    lst = shingles("one two three four five ", 3)
    print(', ')

if __name__ == "__main__": main()