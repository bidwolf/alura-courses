"""
This module contains the 8th challenge.
"""

from src.challenges.module_challenge_8.book import Book


def challenge_8():
    """
    This function represents the solution to challenge 8.
    """
    book = Book(author="zdas", publish_year=2000, title="ssdasd")
    print(book)
    available_books_in_2000 = Book.verify_availability(year=2000)
    print("-----------------available books in 2000--------------------")
    for book in available_books_in_2000:
        print(book)
    book.loan_book()
    print(book)
    Book.verify_availability(year=2000)
