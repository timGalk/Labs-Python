from task2 import Book
from task2 import Library

from  additional_OOP_tasks import Main, Hatchback
if __name__ == "__main__":
    book1 = Book("Hoobit","Tolkien", 1924)
    book2 = Book("Python", "Mark Lutz", 2020 )
    book3 = Book("LOTR", "Tolkien", 1924)

    library = Library([book1])
    library.add_book(book2)
    library.add_book(book3)

    print(*library.get_all_books())

    library.remove_book("LOTR")

    print(*library.get_all_books())

    car1 = Hatchback("Maruti", "Alto", "2022")

    # Call methods
    car1.printDetails()
    car1.accelerate()
    car1.sunroof()


