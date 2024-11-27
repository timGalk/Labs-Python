from Task1 import shingles
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

if __name__ == "__main__":
    test_shingles_with_invalid_input()
    test_with_invalid_k()
    print("All tests passed")
