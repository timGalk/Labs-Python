from shingles import shingles
import pytest


def test_shingles_with_invalid_input():
    """ Test shingles function with invalid input """
    with pytest.raises(TypeError):
        shingles([], 'null')


def test_with_invalid_k():
    """ Test shingles function with invalid k """
    with pytest.raises(ValueError):
        shingles('hello world', -1)


def test_shingles_with_valid_input():
    """ Test shingles function with valid input """
    assert shingles('hello world', 2) == ["hello world"]
    assert shingles("one two three four", 3) == ["one two three", "two three four"]
    assert shingles("This is a test. This is only a test", 2) == ['This is', 'is a', 'a test.', 'test. This', 'This is', 'is only',
                                                 'only a']

def test_counter_shingles_with_valid_input():
    """ Test shingles function with valid input """
if __name__ == "__main__":
    test_shingles_with_invalid_input()
    test_with_invalid_k()
    print("All tests passed")
