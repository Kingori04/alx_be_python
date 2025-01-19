class Book:
    """Represents a book with a title, author, and availability status."""

    def __init__(self, title, author):
        """Initialize a book with a title, an author, and an availability status."""
        self.title = title
        self.author = author
        self._is_checked_out = False

    def check_out(self):
        """Mark the book as checked out if it's not already checked out."""
        if not self._is_checked_out:
            self._is_checked_out = True
            return True
        return False

    def return_book(self):
        """Mark the book as available if it's currently checked out."""
        if self._is_checked_out:
            self._is_checked_out = False
            return True
        return False

    def is_available(self):
        """Check if the book is available for checkout."""
        return not self._is_checked_out


class Library:
    """Manages a collection of books in a library."""

    def __init__(self):
        """Initialize the library with an empty collection of books."""
        self._books = []

    def add_book(self, book):
        """Add a book to the library's collection."""
        if isinstance(book, Book):
            self._books.append(book)

    def check_out_book(self, title):
        """Attempt to check out a book by title."""
        for book in self._books:
            if book.title == title and book.is_available():
                book.check_out()
                print(f"The book '{title}' has been checked out.")
                return
        print(f"The book '{title}' is not available or does not exist.")

    def return_book(self, title):
        """Attempt to return a book by title."""
        for book in self._books:
            if book.title == title and not book.is_available():
                book.return_book()
                print(f"The book '{title}' has been returned.")
                return
        print(f"The book '{title}' is not currently checked out or does not exist.")

    def list_available_books(self):
        """List all available books in the library."""
        available_books = [book for book in self._books if book.is_available()]
        if available_books:
            for book in available_books:
                print(f"{book.title} by {book.author}")
        else:
            print("No books are currently available.")


