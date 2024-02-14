"""
This module defines the Book class.
"""


class Book:
    """
    Represents a book.
    """

    _books_available = []

    def __init__(self, title: str, author: str, publish_year: int):
        self._title = title
        self._author = author
        self._publish_year = publish_year
        self._available = True
        Book._books_available.append(self)

    def __str__(self):
        return (
            f"The book {self._title} wrote by {self._author} in {self._publish_year} is "
            + ("available" if self._available is True else "not available")
        )

    def loan_book(self):
        """
        Marks the book as loaned by setting the availability status to False.
        Removes the book from the list of available books.
        """
        self._available = False
        Book._books_available.remove(self)

    @property
    def publish_year(self):
        """
        Returns the publication year of the book.

        Returns:
            int: The publication year of the book.
        """
        return self._publish_year

    @staticmethod
    def verify_availability(year: int):
        """
        Verifies the availability of books published in a specific year.

        Parameters:
        year (int): The year of publication to search for.

        Returns:
        list: A list of books published in the specified year.
        """
        return [book for book in Book._books_available if book.publish_year == year]
