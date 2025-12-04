import pytest

from model.publisher import Publisher


@pytest.fixture
def publisher_default():
    """
    Provides a default Publisher instance for testing.

    Returns:
        - Publisher: A Publisher object with:
            - ID: 1
            - Legal_name: Publisher
            - City: New York
            - State: NY
    """
    return Publisher(publisher_id="1", legal_name="Publisher", city="New York", state="NY")


@pytest.mark.parametrize('deleted, expected', [
    (False, False),
    (True, True),
])
def test_publisher_creation_deleted_flag(deleted, expected):
    """
    Checks that the Publisher instance is created with the correct deleted flag.

    Parameters (via parametrize):
        - deleted (bool): Value passed during Publisher creation.
        - expected (bool): Expected value for the deleted attribute.
    """
    publisher = Publisher(publisher_id="1", legal_name="Publisher", city="New York", state="NY", deleted=deleted)
    assert publisher.deleted is expected


def test_publisher_setters_update_attributes(publisher_default):
    """
    Verifies that the Publisher's setters correctly update its attributes.

    Fixture:
        - publisher_default: Provides a Publisher instance with default values.
    """
    expected_id = "1"
    expected_legal_name = "Publisher UP"
    expected_city = "New York UP"
    expected_state = "NY"
    expected_deleted = True

    publisher_default.publisher_id = expected_id
    publisher_default.legal_name = expected_legal_name
    publisher_default.city = expected_city
    publisher_default.state = expected_state
    publisher_default.deleted = expected_deleted

    assert publisher_default.publisher_id == expected_id
    assert publisher_default.legal_name == expected_legal_name
    assert publisher_default.city == expected_city
    assert publisher_default.state == expected_state
    assert publisher_default.deleted is expected_deleted


def test_publisher_str_returns_formatted_string(publisher_default):
    """
    Checks that the __str__ method returns the correctly formatted string representation.
    """
    expected = "ID: 1, Legal Name: Publisher, City: New York, State: NY"
    assert str(publisher_default) == expected
