class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self._is_checked_out = False

    def __str__(self):
        return f"{self.title} by {self.author}"

class Library:
    def __init__(self):
        self._books = []

    def add_book(self, book):
        self._books.append(book)

    def check_out_book(self, title):
        for book in self._books:
            if book.title == title:
                book._is_checked_out = True

        return f"No book with title {title} was found"

    def return_book(self, title):
        for book in self._books:
            if book.title == title:
                book._is_checked_out = False
                return book
        return f"Book not found"

    def list_available_books(self):
        for book in self._books:
            if book._is_checked_out == False:
                print(f"{book.title} by {book.author}")

