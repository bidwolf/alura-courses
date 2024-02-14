from src.challenges.module_challenge_8.book import Book


def main():
    beginners_book = Book(author="rik", publish_year=2024, title="python for beginners")
    advanced_book = Book(author="rik", publish_year=2024, title="advanced python")
    print(beginners_book)
    print(advanced_book)
    beginners_book.loan_book()
    print(beginners_book)
    for book in Book.verify_availability(year=2024):
        print(book)


if __name__ == "__main__":
    main()
