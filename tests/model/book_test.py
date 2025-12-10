import pytest

from model.author import Author
from model.book import Book
from model.publisher import Publisher


@pytest.fixture
def book_default():
    """
    Provides a default Book instance for testing.

    Returns:
        - Book: A Book object with:
            - isbn: "9789789789789"
            - title: "Book"
            - author_id: "1"
            - publisher_id: "1"
            - year: 2025
            - quantity: 1
            - deleted: 0
    """
    author = Author(author_id="1", name="Author")
    publisher = Publisher(publisher_id="1", legal_name="Publisher", city="City", state="ST")
    return Book(isbn="9789789789789", title="Book", author=author, publisher=publisher, year=2025, quantity=1)


@pytest.mark.parametrize('deleted, expected', [
    (False, False),
    (True, True),
])
def test_book_creation_deleted_flag(deleted, expected):
    """
    Checks that the Book instance is created with the correct deleted flag.

    Parameters (via parametrize):
        - deleted (bool): Value passed during Book creation.
        - expected (bool): Expected value for the deleted attribute.
    """
    author = Author(author_id="1", name="Author")
    publisher = Publisher(publisher_id="1", legal_name="Publisher", city="City", state="ST")
    book = Book(isbn="9789789789789", title="Book", author=author, publisher=publisher, year=2025, quantity=1, deleted=deleted)

    assert book.deleted is expected


def test_book_setters_update_attributes(book_default):
    """
    Verifies that the Book's setters correctly update its attributes.

    Fixture:
        - book_default: Provides a Book instance with default values.
    """
    expected_isbn = "9789789789781"
    expected_title = "Book UP"
    expected_author = book_default.author
    expected_publisher = book_default.publisher
    expected_year = 2024
    expected_quantity = 2
    expected_deleted = True

    book_default.isbn = expected_isbn
    book_default.title = expected_title
    book_default.author = expected_author
    book_default.publisher = expected_publisher
    book_default.year = expected_year
    book_default.quantity = expected_quantity
    book_default.deleted = expected_deleted

    assert book_default.isbn == expected_isbn
    assert book_default.title == expected_title
    assert book_default.author == expected_author
    assert book_default.publisher == expected_publisher
    assert book_default.year == expected_year
    assert book_default.quantity == expected_quantity
    assert book_default.deleted is expected_deleted


def test_book_str_returns_formatted_string(book_default):
    """
    Checks that the __str__ method returns the correctly formatted string representation.
    """
    expected = f'ISBN: {book_default.isbn}, Title: {book_default.title}, Author: {book_default.author.name}, Publisher: {book_default.publisher.legal_name}, Year: {book_default.year}, Quantity: {book_default.quantity}'
    assert str(book_default) == expected
