import pytest
from task1 import task1
from task2 import Book
from task2 import Library

def test_task1 ():
    valid_input = [1,0,2,0,3]
    invalid_dt = "[1,0,2,0,3]"
    invalid_dt_in_arr = [1,"2",0,0,(3)]
    assert (task1(valid_input) == [1,2,3,0,0])
    with pytest.raises(TypeError):
        task1(invalid_dt)
    with pytest.raises(TypeError):
        task1(invalid_dt_in_arr)

def test_task2 ():
    book_with_valid_details = Book("Hobbit","Tolkien", 1924)
    assert (book_with_valid_details.__class__ == Book)
    with pytest.raises(ValueError):
        book2 = Book("LOTR", 1924, 1924)
    with pytest.raises(ValueError):
        book3 = Book("LOTR", "Tolkien", "1924")



if __name__ == "__main__":
    test_task1()
    print("Tests for task 1 passed successfully")
    test_task2()
    print("Tests for task 2 passed successfully")