
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 10 10:22:55 2024

@author: Tsimur Halkin
"""

import matplotlib.pyplot as plt
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

def random_walk(number_of_steps: int) -> list:
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
        codon = dna[i:i+3]
        if codon in stop_codons:
            return i + 3 == len(dna)  # True if the stop codon is at the end

    return False  # No valid stop codon found at the end

def main():
    print("Hello, this is the report for the lab I.")
    print("Which task would you like to check? Please provide your answer (1-6):")

    while True:
        try:
            task = int(input("Enter the task number (1-6) or 0 to exit: "))
            if task == 0:
                print("Exiting the report. Goodbye!")
                break
            elif task == 1:
                # Task 1: Get weekday
                day = int(input("Enter the day (1-31): "))
                month = int(input("Enter the month (1-12): "))
                year = int(input("Enter the year: "))
                result = weekday(day, month, year)
                print(f"The day of the week for {day}/{month}/{year} is {result}.")
            elif task == 2:
                # Task 2: Find segment intersection length
                Ap = float(input("Enter the start point of segment A: "))
                Ak = float(input("Enter the end point of segment A: "))
                Bp = float(input("Enter the start point of segment B: "))
                Bk = float(input("Enter the end point of segment B: "))
                result = segment_length(Ap, Ak, Bp, Bk)
                if result:
                    print(f"The intersection of the segments is from {result[0]} to {result[1]}.")
                else:
                    print("There is no intersection between the segments.")
            elif task == 3:
                # Task 3: Random walk visualization
                n = int(input("Enter the number of steps for the random walk: "))
                coordinates = random_walk(n)
                x, y = zip(*coordinates)
                plt.plot(x, y, marker='o', linestyle='-', markersize=2)
                plt.xlabel('X Coordinate')
                plt.ylabel('Y Coordinate')
                plt.title('Walker\'s Trajectory')
                plt.grid(True)
                plt.show()
            elif task == 4:
                # Task 4: Convert decimal to binary
                num = int(input("Enter a decimal number: "))
                result = dec2bin(num)
                print(f"The binary representation of {num} is {result}.")
            elif task == 5:
                # Task 5: Find DNA complement
                dna = input("Enter a DNA sequence: ")
                result = dna_complement(dna)
                print(f"The complementary DNA sequence is {result}.")
            elif task == 6:
                # Task 6: Check for valid gene in DNA sequence
                dna = input("Enter a DNA sequence: ")
                result = find_genes(dna)
                if result:
                    print("The DNA sequence contains a valid gene.")
                else:
                    print("The DNA sequence does not contain a valid gene.")
            else:
                print("Please enter a valid task number (1-6).")
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 6, or 0 to exit.")



if __name__ == "__main__":
    main()