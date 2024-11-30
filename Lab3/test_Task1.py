from a import shingles
from shingle import counter_shingles
from compare import preprocess_text, jaccard_similarity, compare_files
import pytest

# Part A tests

# Errors check
def test_shingles_with_invalid_input():
    """ Test shingles function with invalid input """
    with pytest.raises(TypeError):
        shingles([], 'null')


def test_shingles_invalid_k ():
    """ Test shingles function with invalid k """
    with pytest.raises(ValueError):
        shingles('hello world', -1)
#
def test_shingles_with_zero_k ():
    """Test shingles function with zero k"""
    with pytest.raises(ValueError):
        shingles('hello world', 0)

def test_empty_string_shingles ():
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
    with pytest.raises(TypeError):
        counter_shingles(["hello", "world", 1])




# Part C tests
# Test preprocess_text function
def test_preprocess_text_no_punctuation():
    text = "Hello, world! How are you?"
    assert preprocess_text(text, remove_punctuation=True) == "Hello world How are you"
def test_preprocess_text_with_punctuation():
    text = "Hello, world! How are you?"
    assert preprocess_text(text, remove_punctuation=False) == text

# Test jaccard_similarity function
def test_jaccard_similarity():
    set1 = {"a", "b", "c"}
    set2 = {"a", "b", "d"}
    assert jaccard_similarity(set1, set2) == 2 / 4
    set3 = {"a", "b", "c", "e"}
    set4 = {"a", "b", "d"}
    assert jaccard_similarity(set3, set4) == pytest.approx(2 / 5, 0.001)

def test_jaccard_similarity_invalid_input():
    with pytest.raises(TypeError):
        jaccard_similarity("hello", "world")
    with pytest.raises(TypeError):
        jaccard_similarity({"hello"}, "world")
    with pytest.raises(TypeError):
        jaccard_similarity("hello", {"world"})

# Test compare_files function
def test_compare_files():
    # The part of the code that was gerenated by Github Copilot for the prompt : write a tests for the function
    with open("file1.txt", "w") as f1, open("file2.txt", "w") as f2:
        f1.write("Hello, world! How are you?")
        f2.write("Hello, world! How are you?")
    assert compare_files("file1.txt", "file2.txt", 2, True) == 1.0
    with open("file1.txt", "w") as f1, open("file2.txt", "w") as f2:
        f1.write("Hello, world! How are you?")
        f2.write("Hello, world! How are you?")
    assert compare_files("file1.txt", "file2.txt", 2, False) == 1.0
    with open("file1.txt", "w") as f1, open("file2.txt", "w") as f2:
        f1.write("Hello, world! How are you?")
        f2.write("Hello, world! How are you?")
    assert compare_files("file1.txt", "file2.txt", 3, True) == 1.0
    with open("file1.txt", "w") as f1, open("file2.txt", "w") as f2:
        f1.write("Hello, world! How are you?")
        f2.write("Hello, world! How are you?")
    assert compare_files("file1.txt", "file2.txt", 3, False) == 1.0
    with open("file1.txt", "w") as f1, open("file2.txt", "w") as f2:
        f1.write("")
        f2.write("")
    with pytest.raises(ValueError):
        compare_files("file1.txt", "file2.txt", 2, True)
    with pytest.raises(ValueError):
        compare_files("file1.txt", "file2.txt", 2, False)
    with pytest.raises(ValueError):
        compare_files("file1.txt", "file2.txt", 3, True)
    with pytest.raises(ValueError):
        compare_files("file1.txt", "file2.txt", 3, False)


if __name__ == "__main__":
    # Task a tests
    test_shingles_with_invalid_input()
    test_shingles_invalid_k()
    test_shingles_with_zero_k()
    test_empty_string_shingles()
    test_shingles_with_valid_input()
    # Task B tests
    test_counter_shingles_with_valid_input()
    test_counter_shingles_with_invalid_input()

    # Task C tests
    test_preprocess_text_no_punctuation()
    test_preprocess_text_with_punctuation()
    test_jaccard_similarity()
    test_jaccard_similarity_invalid_input()
    test_compare_files()
    print("All tests passed")
