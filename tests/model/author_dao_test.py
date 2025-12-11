import os
import pytest

from typing import Iterable

from model.author import Author
from model.author_dao import AuthorDao


@pytest.fixture(autouse=True)
def use_temp_database(tmp_path, monkeypatch):
    """
    Use a temporary SQLite database for each test to avoid
    interfering with the real 'library.db' file.
    """
    db_file = tmp_path / "test_library.db"
    monkeypatch.setattr(AuthorDao, "_DB_NAME", str(db_file))

    AuthorDao.create_table()

    yield

    assert os.path.exists(db_file)


def test_create_table_is_idempotent():
    """
    Ensures create_table() can be called multiple times without errors.
    """
    AuthorDao.create_table()


def test_save_inserts_new_author_and_get_by_id_returns_it():
    """
    Ensures save() inserts a new author and get_by_id() retrieves it.
    """
    author = Author(author_id="1", name="George Orwell")
    AuthorDao.save(author=author)

    loaded = AuthorDao.get_by_id(author_id="1")

    assert loaded is not None
    assert loaded.author_id == "1"
    assert loaded.name == "George Orwell"
    assert loaded.deleted is False


def test_get_all_returns_only_not_deleted_authors():
    """
    Ensures get_all() returns only authors where deleted = 0.
    """
    a1 = Author(author_id="1", name="Author 1")
    a2 = Author(author_id="2", name="Author 2")
    a3 = Author(author_id="3", name="Author 3", deleted=True)

    AuthorDao.save(a1)
    AuthorDao.save(a2)
    AuthorDao.save(a3)

    authors: Iterable[Author] = AuthorDao.get_all()
    authors_list = list(authors)

    assert len(authors_list) == 2
    ids = {a.author_id for a in authors_list}
    assert "1" in ids
    assert "2" in ids
    assert "3" not in ids


def test_get_all_returns_empty_list_when_no_authors():
    """
    Ensures get_all() return an empty list when there are no authors.
    """
    authors = AuthorDao.get_all()
    assert list(authors) == []


def test_get_by_id_returns_none_when_author_not_found():
    """
    Ensures get_by_id() returns None when author_id is not found.
    """
    result = AuthorDao.get_by_id(author_id="not_found")
    assert result is None


def test_save_updates_existing_author():
    """
    Ensures save() updates an existing author when the same author_id is used.
    """
    author = Author(author_id="A001", name="Original Name")
    AuthorDao.save(author)

    updated_author = Author(author_id="A001", name="Updated Name", deleted=True)
    AuthorDao.save(updated_author)

    active = AuthorDao.get_by_id(author_id="A001")
    assert active is None

    deleted_author = AuthorDao.get_by_id(author_id="A001", deleted=1)
    assert deleted_author is not None
    assert deleted_author.author_id == "A001"
    assert deleted_author.name == "Updated Name"
    assert deleted_author.deleted is True


def test_delete_sets_deleted_flag_to_true():
    """
    Ensures delete() sets deleted = 1 for the given author_id
    """
    author = Author(author_id="A002", name="To Delete")
    AuthorDao.save(author)

    AuthorDao.delete(author_id="A002")

    active = AuthorDao.get_by_id(author_id="A002")
    assert active is None

    deleted_author = AuthorDao.get_by_id(author_id="A002", deleted=1)
    assert deleted_author is not None
    assert deleted_author.deleted is True


def test_restore_sets_deleted_flag_to_false():
    """
    Ensures restore() sets deleted = 0 for the given author_id.
    """
    author = Author(author_id="A003", name="To Restore")
    AuthorDao.save(author)

    AuthorDao.delete(author_id="A003")
    assert AuthorDao.get_by_id(author_id="A003") is None
    assert AuthorDao.get_by_id(author_id="A003", deleted=1) is not None

    AuthorDao.restore(author_id="A003")

    restored = AuthorDao.get_by_id(author_id="A003")
    assert restored is not None
    assert restored.deleted is False

    deleted_again = AuthorDao.get_by_id(author_id="A003", deleted=1)
    assert deleted_again is None
