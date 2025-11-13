from unittest.mock import Mock

import pytest

from validators.author_validator import AuthorValidator


@pytest.mark.parametrize('author_id, expected', [
    ('12345', True),
    ('123A', False),
    ('', False)
])
def test_validate_author_id(author_id, expected):
    """Checks that numeric author IDs are valid and non-numeric are invalid."""
    assert AuthorValidator.validate_author_id(author_id=author_id) is expected


@pytest.mark.parametrize('name, expected', [
    ('Ana', True),
    ('Jo', False),
    ('', False)
])
def test_validate_author_name(name, expected):
    """Checks that author names with at least 3 characters are valid."""
    assert AuthorValidator.validate_name(name=name) is expected


@pytest.mark.parametrize('new_name, existing_name, deleted, expected', [
    ('Maria', 'Ana', False, True),  # New name not in list -> valid
    ('Ana', 'Ana', False, False),  # Existing name -> invalid
    ('Ana', 'Ana', True, True),  # Existing name but deleted -> valid
    ('  ANA', ' Ana ', False, False)  # Ignore case and space -> invalid
])
def test_validate_unique_names(new_name, existing_name, deleted, expected):
    """Checks that unique name validation works correctly, ignoring case and whitespace."""
    author = Mock()
    author.name = existing_name
    author.deleted = deleted
    authors = [author]
    assert AuthorValidator.validate_unique_names(new_name, authors) is expected
