from parso.python.tree import Class


class Book:
    """ """
    def __init__(self, title,author, year):
        self.title = title
        self.author = author
        self.year = year
        if not isinstance(title,str):
            raise ValueError("Title must be a string")
        if not isinstance(author,str):
            raise ValueError("Author must be a string")
        if not isinstance(year,int):
            raise ValueError("Year must be a integer number")

class Library:
    """ """
    def __init__(self, books: list[Book]):
        self.books = books

    def add_book (self, book:Book):
        self.books.append(Book)
    def remove_book(self, book_name:str ):
        for book in self.books:
            if book.title ==book_name:
                self.books.remove(book)



