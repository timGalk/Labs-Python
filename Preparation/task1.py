def task1(array: list[int]) -> list[int]:
    """Moves all zeroes in the array to the end while preserving the order of other elements.

    Args:
        array (list[int]): List of integers.

    Returns:
        list[int]: A new list with zeroes moved to the end.

    Raises:
        TypeError: If the input is not a list or if elements are not integers.
    """
    # Validate input type
    if not isinstance(array, list):
        raise TypeError("Input must be a list")

    # Validate element types
    if not all(isinstance(i, int) for i in array):
        raise TypeError("All elements in the list must be integers")

    result = []
    zeroes_counter = 0

    for i in array:
        if i == 0:
            zeroes_counter += 1
            continue
        result.append(i)

    return result + [0] * zeroes_counter
