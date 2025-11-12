import pytest

from model.author import Author


@pytest.fixture
def author_default():
    """
    Provides a default Author instance for testing.

    Returns:
        - Author: An Author object with ID 'JD01', name 'John Doe', and deleted=False.
    """
    return Author(author_id='JD01', name='John Doe')


@pytest.mark.parametrize('deleted, expected', [
    (False, False),
    (True, True),
])
def test_author_creation_deleted_flag(deleted, expected):
    """
    Checks that the Author instance is created with the correct deleted flag.

    Parameters (via parametrize):
        - deleted (bool): Value passed during Author creation.
        - expected (bool): Expected value for the deleted attribute.
    """
    author = Author(author_id="JD01", name="John Doe", deleted=deleted)
    assert author.deleted is expected


def test_author_setters_update_attributes(author_default):
    """
    Verifies that the Author's setters correctly update its attributes.

    Fixture:
        - author_default: Provides an Authr instance with default values.
    """
    expected_id = "JD02"
    expected_name = "John Doe UPDATED"
    expected_deleted = True

    author_default.author_id = expected_id
    author_default.name = expected_name
    author_default.deleted = expected_deleted

    assert author_default.author_id == expected_id
    assert author_default.name == expected_name
    assert author_default.deleted is expected_deleted


def test_author_str_returns_formatted_string(author_default):
    """
    Checks that the __str__ method returns the correctly formatted string representation.
    """
    expected = "ID: JD01 - Name: John Doe"
    assert str(author_default) == expected
