# -*- coding: utf-8 -*-
"""
Created on Thu Oct 10 10:22:55 2024

@author: Tsimur Halkin
"""

import random


# Task 1

def weekday(day: int, month: int, year: int) -> str:
    """Return the day of the week for a given date.

    Args:
        day (int): The day of the month.
        month (int): The month (1-12).
        year (int): The year.

    Returns:
        str: The name of the day of the week (e.g., "Monday").
    """
    week_days = {0: "Sunday", 1: "Monday", 2: "Tuesday",
                 3: "Wednesday", 4: "Thursday", 5: "Friday", 6: "Saturday"}

    y0 = year - (14 - month) // 12
    x = y0 + (y0 // 4) - (y0 // 100) + (y0 // 400)
    m0 = month + 12 * ((14 - month) // 12) - 2
    d0 = (day + x + (31 * m0) // 12) % 7

    return week_days[d0]


# Task 2

def segment_length(Ap: float, Ak: float, Bp: float, Bk: float) -> tuple or None:
    """Calculate the length of the intersection of two segments.

    Args:
        Ap (float): The start point of segment A.
        Ak (float): The end point of segment A.
        Bp (float): The start point of segment B.
        Bk (float): The end point of segment B.

    Returns:
        tuple: A tuple containing the start and end of the intersection,
               or None if there is no intersection.
    """
    start_A = min(Ap, Ak)
    end_A = max(Ap, Ak)
    start_B = min(Bp, Bk)
    end_B = max(Bp, Bk)
    start_intersection = max(start_A, start_B)
    end_intersection = min(end_A, end_B)

    if end_intersection <= start_intersection:
        return None
    else:
        return (start_intersection, end_intersection)


# Task 3

def random_walk(number_of_steps: int) -> tuple:
    """Generate a random walk starting from the origin.

    Args:
        number_of_steps (int): The number of steps in the walk.

    Returns:
        list: A list of tuples representing the coordinates visited during the walk.
    """
    start_point = (0, 0)
    movement = [start_point]

    for _ in range(number_of_steps):
        last_x, last_y = movement[-1]
        x_coordinate = random.randint(last_x - 1, last_x + 1)
        y_coordinate = random.randint(last_y - 1, last_y + 1)
        movement.append((x_coordinate, y_coordinate))

    return movement


def dec2bin(num: int) -> str:
    """Convert a decimal number to its binary representation.

    Args:
        num (int): The decimal number to convert.

    Returns:
        str: The binary representation of the number as a string.
    """
    if num == 0:
        return "0"

    result = ""
    while num > 0:
        result += str(num % 2)
        num //= 2

    return result[::-1]


# Task 5

def dna_complement(dna: str) -> str:
    """Find the complementary DNA strand for a given DNA sequence.

    Args:
        dna (str): A string representing the DNA sequence.

    Returns:
        str: The complementary DNA sequence or an error message if the input is invalid.
    """
    dna = dna.upper()
    pairs = {"A": "T", "C": "G", "T": "A", "G": "C"}
    output = ""

    for acid in dna:
        if acid not in pairs:
            return f"{acid} is not a valid nucleotide. Please check your input."

        output += pairs[acid]

    return output


# Task 6
def find_genes(dna: str) -> bool:
    """Determine if a DNA sequence contains a valid gene.

    Args:
        dna (str): A string representing the DNA sequence.

    Returns:
        bool: True if the sequence is a valid gene, False otherwise.
    """
    stop_codons = {"TAG", "TAA", "TGA"}
    start_codon = "ATG"

    if not dna.startswith(start_codon):
        return False

    if len(dna) % 3 != 0:
        return False

    for i in range(3, len(dna), 3):
        codon = dna[i:i + 3]
        if codon in stop_codons:
            return i + 3 == len(dna)  # True if the stop codon is at the end

    return False  # No valid stop codon found at the end


def main():
    # Input condition  for task 6
    print(find_genes(input("Enter DNA sequence: ")))


if __name__ == "__main__":
    main()
