from a import shingles
from shingle import counter_shingles
import pytest

# Part A tests

# Errors check
def test_shingles_with_invalid_input():
    """ Test shingles function with invalid input """
    with pytest.raises(TypeError):
        shingles([], 'null')


def test_with_invalid_k():
    """ Test shingles function with invalid k """
    with pytest.raises(ValueError):
        shingles('hello world', -1)
#
def test_with_zero_k ():
    """Test shingles function with zero k"""
    with pytest.raises(ValueError):
        shingles('hello world', 0)

def test_with_empty_string ():
    """Test shingles function with empty string"""
    with pytest.raises(TypeError):
        shingles('', 2)

#  def test_with_k_greater_than_string_length ():
#      """Test """
#      with pytest.raises(ValueError):
#          shingles('hello world', 5)
# Valid data
def test_shingles_with_valid_input():
    """ Test shingles function with valid input """
    assert shingles('hello world', 2) == ["hello world"]
    assert shingles("one two three four", 3) == ["one two three", "two three four"]
    assert shingles("This is a test. This is only a test", 2) == ['This is', 'is a', 'a test.',
                                                                  'test. This', 'This is', 'is only',
                                                                  'only a', 'a test']
# Part B tests  for counter_shingles function

def test_counter_shingles_with_valid_input():
    """ Test counter_shingles function with valid input """
    assert counter_shingles(shingles("one two three four", 3)) == {"one two three": 1, "two three four": 1}
    assert counter_shingles(shingles("This is a test. This is only a test", 2)) == {'This is': 2, 'is a': 1, 'a test.': 1,
                                                                                    'test. This': 1, 'is only': 1,
                                                                                    'only a': 1, 'a test': 1}
    assert counter_shingles(shingles("Hello world", 2)) == {"Hello world": 1}

def test_counter_shingles_with_invalid_input():
    """ Test counter_shingles function with invalid input """
    with pytest.raises(TypeError):
        counter_shingles(1)
    with pytest.raises(TypeError):
        counter_shingles("hello world")
    with pytest.raises(TypeError):
        counter_shingles([])
    with pytest.raises(TypeError):
        counter_shingles(["hello", 1, "world"])


# Part C tests
if __name__ == "__main__":
    # Task a tests
    test_shingles_with_invalid_input()
    test_with_invalid_k()
    test_with_zero_k()
    test_with_empty_string()
    # Task B tests
    test_counter_shingles_with_valid_input()
    test_counter_shingles_with_invalid_input()
    print("All tests passed")
