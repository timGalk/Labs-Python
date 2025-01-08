class Book:
    """
    Represents a book with title, author and pub. year

    Attributes:
        title(str):represents a title of a book
        author(str): represents an author of a book
        year(int): represents a year of a book publication
    Raises
        ValueError: if parameters
    """
    def __init__(self, title,author, year):
        self.title = title
        self.author = author
        self.year = year
        if not isinstance(title,str) or title == "":
            raise ValueError("Title must be a string")
        if not isinstance(author,str):
            raise ValueError("Author must be a string")
        if not isinstance(year,int) or year <= 0 :
            raise ValueError("Year must be positive integer number")

class Library:
    """  """
    def __init__(self, books: list[Book]):
        self.books = books
        if not all(isinstance(book,Book) for book in self.books):
            TypeError("Books must implement a Book class ")

    def add_book (self, book:Book):
        self.books.append(book)
    def remove_book(self, book_name:str ):
        for book in self.books:
            if book.title ==book_name:
                self.books.remove(book)
    def find_book_by_author (self, author_name: str) -> list :
        result = []
        for book in self.books:
            if book.author == author_name:
                result.append(book)

        return result

    def get_all_books(self):
        return [book.title for book in self.books]