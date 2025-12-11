import os
import pytest

from typing import Iterable

from model.publisher import Publisher
from model.publisher_dao import PublisherDao


@pytest.fixture(autouse=True)
def use_temp_database(tmp_path, monkeypatch):
    """
    Use a temporary SQLite database for each test to avoid
    interfering with the real 'library.db' file.
    """
    db_file = tmp_path / "test_library.db"
    monkeypatch.setattr(PublisherDao, "_DB_NAME", str(db_file))

    PublisherDao.create_table()

    yield

    assert os.path.exists(db_file)


def test_create_table_is_idempotent():
    """
    Ensures create_table() can be called multiple times without errors.
    """
    PublisherDao.create_table()


def test_save_inserts_new_publisher_and_get_by_id_returns_it():
    """
    Ensures save() inserts a new publisher and get_by_id() retrieves it.
    """
    publisher = Publisher(publisher_id="1", legal_name="Publisher", city="City", state="ST")
    PublisherDao.save(publisher=publisher)

    loaded = PublisherDao.get_by_id(publisher_id="1")

    assert loaded is not None
    assert loaded.publisher_id == "1"
    assert loaded.legal_name == "Publisher"
    assert loaded.city == "City"
    assert loaded.state == "ST"
    assert loaded.deleted is False


def test_get_all_returns_only_not_deleted_publishers():
    """
    Ensures get_all() returns only publishers where deleted = 0.
    """
    p1 = Publisher(publisher_id="1", legal_name="Publisher 1", city="City", state="ST")
    p2 = Publisher(publisher_id="2", legal_name="Publisher 2", city="City", state="ST")
    p3 = Publisher(publisher_id="3", legal_name="Publisher 3", city="City", state="ST", deleted=True)

    PublisherDao.save(p1)
    PublisherDao.save(p2)
    PublisherDao.save(p3)

    publishers: Iterable[Publisher] = PublisherDao.get_all()
    publishers_list = list(publishers)

    assert len(publishers_list) == 2
    ids = {p.publisher_id for p in publishers_list}
    assert "1" in ids
    assert "2" in ids
    assert "3" not in ids


def test_get_all_returns_empty_list_when_no_publishers():
    """
    Ensures get_all() return an empty list when there are no publishers.
    """
    publishers = PublisherDao.get_all()
    assert list(publishers) == []


def test_get_by_id_returns_none_when_publisher_not_found():
    """
    Ensures get_by_id() returns None when publisher_id is not found.
    """
    result = PublisherDao.get_by_id(publisher_id="not_found")
    assert result is None


def test_save_updates_existing_publisher():
    """
    Ensures save() updates an existing publisher when the same publisher_id is used.
    """
    publisher = Publisher(publisher_id="A001", legal_name="Original Name", city="City", state="ST")
    PublisherDao.save(publisher)

    updated_publisher = Publisher(publisher_id="A001", legal_name="Updated Name", city="City", state="ST", deleted=True)
    PublisherDao.save(updated_publisher)

    active = PublisherDao.get_by_id(publisher_id="A001")
    assert active is None

    deleted_publisher = PublisherDao.get_by_id(publisher_id="A001", deleted=1)
    assert deleted_publisher is not None
    assert deleted_publisher.publisher_id == "A001"
    assert deleted_publisher.legal_name == "Updated Name"
    assert deleted_publisher.deleted is True


def test_delete_sets_deleted_flag_to_true():
    """
    Ensures delete() sets deleted = 1 for the given publisher_id
    """
    publisher = Publisher(publisher_id="A002", legal_name="To Delete", city="City", state="ST")
    PublisherDao.save(publisher)

    PublisherDao.delete(publisher_id="A002")

    active = PublisherDao.get_by_id(publisher_id="A002")
    assert active is None

    deleted_publisher = PublisherDao.get_by_id(publisher_id="A002", deleted=1)
    assert deleted_publisher is not None
    assert deleted_publisher.deleted is True


def test_restore_sets_deleted_flag_to_false():
    """
    Ensures restore() sets deleted = 0 for the given publisher_id.
    """
    publisher = Publisher(publisher_id="A003", legal_name="To Restore", city="City", state="ST")
    PublisherDao.save(publisher)

    PublisherDao.delete(publisher_id="A003")
    assert PublisherDao.get_by_id(publisher_id="A003") is None
    assert PublisherDao.get_by_id(publisher_id="A003", deleted=1) is not None

    PublisherDao.restore(publisher_id="A003")

    restored = PublisherDao.get_by_id(publisher_id="A003")
    assert restored is not None
    assert restored.deleted is False

    deleted_again = PublisherDao.get_by_id(publisher_id="A003", deleted=1)
    assert deleted_again is None
