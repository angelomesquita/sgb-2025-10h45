import os
import pytest

from typing import Iterable

from model.author import Author
from model.author_dao import AuthorDao
from model.book import Book
from model.book_dao import BookDao
from model.publisher import Publisher
from model.publisher_dao import PublisherDao


@pytest.fixture(autouse=True)
def use_temp_database(tmp_path, monkeypatch):
    """
    Use a temporary SQLite database for each test to avoid
    interfering with the real 'library.db' file.
    """
    db_file = tmp_path / "test_library.db"
    monkeypatch.setattr(BookDao, "_DB_NAME", str(db_file))

    BookDao.create_table()

    yield

    assert os.path.exists(db_file)


@pytest.fixture
def sample_data():
    author = Author(author_id="1", name="Author")
    AuthorDao.save(author=author)

    publisher = Publisher(publisher_id="1", legal_name="Publisher", city="City", state="ST")
    PublisherDao.save(publisher=publisher)

    return {
        "author": author,
        "publisher": publisher
    }


def test_create_table_is_idempotent():
    """
    Ensures create_table() can be called multiple times without errors.
    """
    BookDao.create_table()


def test_save_inserts_new_book_and_get_by_id_returns_it(sample_data):
    """
    Ensures save() inserts a new book and get_by_id() retrieves it.
    """
    author = sample_data.get("author")
    publisher = sample_data.get("publisher")

    book = Book(isbn="1", title="Book", author=author, publisher=publisher, year=2025, quantity=1)
    BookDao.save(book=book)

    loaded = BookDao.get_by_id(isbn="1")

    assert loaded is not None
    assert loaded.isbn == "1"
    assert loaded.title == "Book"
    assert loaded.author.name == "Author"
    assert loaded.publisher.legal_name == "Publisher"
    assert loaded.year == 2025
    assert loaded.quantity == "1"
    assert loaded.deleted is False


def test_get_all_returns_only_not_deleted_books(sample_data):
    """
    Ensures get_all() returns only books where deleted = 0.
    """
    author = sample_data.get("author")
    publisher = sample_data.get("publisher")

    b1 = Book(isbn="1", title="Book1", author=author, publisher=publisher, year=2025, quantity=1)
    b2 = Book(isbn="2", title="Book2", author=author, publisher=publisher, year=2025, quantity=1)
    b3 = Book(isbn="3", title="Book3", author=author, publisher=publisher, year=2025, quantity=1, deleted=True)

    BookDao.save(b1)
    BookDao.save(b2)
    BookDao.save(b3)

    books: Iterable[Book] = BookDao.get_all()
    books_list = list(books)

    assert len(books_list) == 2
    ids = {b.isbn for b in books_list}
    assert "1" in ids
    assert "2" in ids
    assert "3" not in ids


def test_get_all_returns_empty_list_when_no_books():
    """
    Ensures get_all() return an empty list when there are no books.
    """
    books = BookDao.get_all()
    assert list(books) == []


def test_get_by_id_returns_none_when_book_not_found():
    """
    Ensures get_by_id() returns None when isbn is not found.
    """
    result = BookDao.get_by_id(isbn="not_found")
    assert result is None


def test_save_updates_existing_book(sample_data):
    """
    Ensures save() updates an existing book when the same isbn is used.
    """
    author = sample_data.get("author")
    publisher = sample_data.get("publisher")

    book = Book(isbn="978", title="Original Title", author=author, publisher=publisher, year=2025, quantity=1)
    BookDao.save(book=book)

    updated_book = Book(isbn="978", title="Updated Title", author=author, publisher=publisher, year=2025, quantity=1, deleted=True)
    BookDao.save(book=updated_book)

    active = BookDao.get_by_id(isbn="978")
    assert active is None

    deleted_book = BookDao.get_by_id(isbn="978", deleted=1)
    assert deleted_book is not None
    assert deleted_book.isbn == "978"
    assert deleted_book.title == "Updated Title"
    assert deleted_book.deleted is True


def test_delete_sets_deleted_flag_to_true(sample_data):
    """
    Ensures delete() sets deleted = 1 for the given publisher_id
    """
    author = sample_data.get("author")
    publisher = sample_data.get("publisher")

    book = Book(isbn="978978", title="Original Title", author=author, publisher=publisher, year=2025, quantity=1)
    BookDao.save(book=book)

    BookDao.delete(isbn="978978")

    active = BookDao.get_by_id(isbn="978978")
    assert active is None

    deleted_book = BookDao.get_by_id(isbn="978978", deleted=1)
    assert deleted_book is not None
    assert deleted_book.deleted is True


def test_restore_sets_deleted_flag_to_false(sample_data):
    """
    Ensures restore() sets deleted = 0 for the given isbn.
    """
    author = sample_data.get("author")
    publisher = sample_data.get("publisher")

    book = Book(isbn="978978978", title="Original Title", author=author, publisher=publisher, year=2025, quantity=1)
    BookDao.save(book=book)

    BookDao.delete(isbn="978978978")
    assert BookDao.get_by_id(isbn="978978978") is None
    assert BookDao.get_by_id(isbn="978978978", deleted=1) is not None

    BookDao.restore(isbn="978978978")

    restored = BookDao.get_by_id(isbn="978978978")
    assert restored is not None
    assert restored.deleted is False

    deleted_again = BookDao.get_by_id(isbn="978978978", deleted=1)
    assert deleted_again is None
