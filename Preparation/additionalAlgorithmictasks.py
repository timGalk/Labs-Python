def long_seq(arr: list[int]) -> int:
    if not arr:
        return 0

    arr.sort()
    longest_seq = []
    current_seq = [arr[0]]

    for i in range(1, len(arr)):
        if arr[i] == arr[i-1] + 1:  # Check for consecutive numbers
            current_seq.append(arr[i])
        else:
            if len(current_seq) > len(longest_seq):
                longest_seq = current_seq
            current_seq = [arr[i]]  # Start a new sequence

    if len(current_seq) > len(longest_seq):  # Check the last sequence
        longest_seq = current_seq

    return len(longest_seq)

def test_long_seq():
    assert long_seq([1, 2, 3, 6, 9]) == 3  # Should return the length of [1, 2, 3]

test_long_seq()
