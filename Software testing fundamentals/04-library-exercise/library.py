# title author copies available turetu buti privatus

import unittest

class Book:
    def __init__(self, title, author, copies=1, available=1):
        self.title = title
        self.author = author
        self.copies = copies
        self.available = available

    def is_available(self):
        return self.available > 0

    def borrow(self):
        if self.is_available():
            self.available -= 1
            return f"You have borrowed {self.pretty_name()}"
        else:
            return "You are unable to borrow this book, sorry!"

    def return_book(self):
        if self.available < self.copies:
            self.available += 1
            return "Thank you!"
        else:
            return "This is impossible! All the copies are already there."

    def pretty_name(self):
        return f'"{self.title}" by {self.author}'


class Library:
    def __init__(self):
        self.books_by_title = {}

    def add_book(self, book):
        if book.title not in self.books_by_title:
            self.books_by_title[book.title] = book

    def remove_book(self, book):
        if book.title not in self.books_by_title:
            return
        del self.books_by_title[book.title]

    def check_book_status(self, title):
        return (
            title in self.books_by_title and self.books_by_title[title].is_available()
        )

    def borrow(self, title):
        if title not in self.books_by_title:
            return f"We do not have {title}. Try something else."
        return self.books_by_title[title].borrow()

    def return_book(self, title):
        if title not in self.books_by_title:
            return f"We do not have {title}. Try something else."
        return self.books_by_title[title].return_book()

class BookInitTest(unittest.TestCase):
    def test_init(self):
        b = Book("Namai", "Aurelija")
        self.assertEqual(b.title, "Namai")
        self.assertEqual(b.author, "Aurelija")
        self.assertEqual(b.copies, 1)
        self.assertEqual(b.available, 1)

    def test_init_with_parameters(self):
        b = Book("Namai", "Aurelija", copies=6, available=2)
        self.assertEqual(b.title, "Namai")
        self.assertEqual(b.author, "Aurelija")
        self.assertEqual(b.copies, 6)
        self.assertEqual(b.available, 2)

    def test_is_available(self):
        b = Book("Namai", "Aurelija", available=0)
        self.assertFalse(b.is_available())
        b.available = 1
        self.assertTrue(b.is_available())

    def test_pretty_name(self):
        b = Book("Namai", "Aurelija")
        self.assertTrue(b.pretty_name())

class BookBorrowTest(unittest.TestCase):
    title = "Namai"
    author = "Aurelija"
    def test_book_borrowed(self):
        b = Book(self.title, self.author)
        expected = (f'You have borrowed "{self.title}" by {self.author}')
        self.assertEqual(b.borrow(),expected)
        self.assertEqual(b.available, 0)
        self.assertEqual(b.copies, 1)

    def test_borrow_multiple_copies_positive(self):
        b = Book(self.title, self.author, copies = 10, available = 6)
        expected = (f'You have borrowed "{self.title}" by {self.author}')
        self.assertEqual(b.borrow(), expected)
        self.assertEqual(b.available, 5)
        self.assertEqual(b.borrow(), expected)
        self.assertEqual(b.available, 4)
        self.assertEqual(b.copies, 10)


class BookReturnTest(unittest.TestCase):
    title = "Namai"
    author = "Aurelija"
    def test_return_book(self):
        b = Book(self.title, self.author, copies=4, available=2)
        expected = ("Thank you!")
        self.assertEqual(b.available, 2)
        self.assertEqual(b.copies, 4)
        self.assertEqual(b.return_book(), expected)


# class LibraryTest(unittest.TestCase):
#     pass
#
bookSuite = unittest.TestSuite()
bookSuite.addTests(
    [BookInitTest("test_init"),
    BookInitTest("test_init_with_parameters"),
    BookInitTest("test_is_available"),
    BookInitTest("test_pretty_name")]
)

bookborrowSuite = unittest.TestSuite()
bookborrowSuite.addTests(
    [BookBorrowTest("test_book_borrowed"),
     BookBorrowTest("test_borrow_multiple_copies_positive")]
)

bookreturnSuite = unittest.TestSuite()
bookreturnSuite.addTests(
    [BookReturnTest("test_return_book")]
)

# librarySuite = unittest.TestSuite()
# librarySuite.addTests(
#     []
