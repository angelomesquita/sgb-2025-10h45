from unittest.mock import Mock
from validators.author_validator import AuthorValidator


def test_validate_author_id_numeric():
    """Ensure numeric IDs are validated as True."""
    assert AuthorValidator.validate_author_id(author_id="12345") is True


def test_validate_author_id_non_numeric():
    """Ensure non-numeric IDs return False."""
    assert AuthorValidator.validate_author_id(author_id="123A") is False


def test_validate_author_name_valid():
    """Ensure valid author names (>= 3 chars) return True."""
    assert AuthorValidator.validate_name(name="Ana") is True


def test_validate_author_name_invalid():
    """Ensure author names shorter than 3 chars return False."""
    assert AuthorValidator.validate_name(name="Jo") is False


def test_validate_unique_names_returns_true_for_new_name():
    """Ensure unique new names return True."""
    author = Mock()
    author.name = "Ana"
    author.deleted = False
    authors = [author]
    assert AuthorValidator.validate_unique_names("Maria", authors) is True


def test_validate_unique_names_returns_false_for_existing_name():
    """Ensure name already in the list return False."""
    author = Mock()
    author.name = "Ana"
    author.deleted = False
    authors = [author]
    assert AuthorValidator.validate_unique_names("Ana", authors) is False


def test_validate_unique_names_ignores_deleted_authors():
    """Ensure deleted authors are ignored in uniqueness check."""
    author = Mock()
    author.name = "Ana"
    author.deleted = True
    authors = [author]
    assert AuthorValidator.validate_unique_names("Ana", authors) is True


def test_validate_unique_names_strip_and_ignore_case():
    """Ensure name comparison ignores spaces and letter case."""
    author = Mock()
    author.name = " Ana "
    author.deleted = False
    authors = [author]
    assert AuthorValidator.validate_unique_names(" ANA", authors) is False
