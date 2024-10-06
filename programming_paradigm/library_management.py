class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self._is_checked_out = False

    def check_out_book(self):
        if not self._is_checked_out:
            self._is_checked_out = True
            return True
        else:
            return False

    def return_book(self):
        if self._is_checked_out:
            self._is_checked_out = False
            return True
        else:
            return False

    def is_available(self):
        return not self._is_checked_out

class Library:

    def __init__(self):
        self._books = []

    def add_book(self, book):
        self._books.append(book)

    def checkout_out_book(self, title):
        for book in self._books:
            if book.title == title:
                if book.check_out():
                    print("Book '{title}' checked out successfully")
                    return True
                else:
                    print("Book '{title}' is already checked out")
                    return False
            print(f"Book '{title}' is not in the library.")
            return False

    def return_book(self, title):
        for book in self._books:
            if book.title == title:
                if book.return_book():
                    print("Book '{title}' returned successfully")
                    return True
                else:
                    print("Book '{title}' was not checked out.")
                    return False
            print(f"Book '{title}' not found in the library.")
            return False

    def list_available_books(self):
        """List all availablee books"""
        available_books = [book for bookin self._books if book.is_available()]
        if available_books:
            print("Available books.")
            for book in available_books:
                print(f"- {book.title} by {book.author}")
            else:
                print("No books are currently available")

