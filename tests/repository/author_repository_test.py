import pytest

from unittest.mock import patch
from model.author import Author
from model.author_sqlite_dao import AuthorSqliteDao
from repository.author_repository import AuthorRepository
from model.exceptions import AuthorNotFoundError


@pytest.fixture
def sample_authors():
    """Fixture that provides a sample list of Author objects."""
    return [
        Author(author_id='A1', name='Alice', deleted=False),
        Author(author_id='A2', name='Bob', deleted=True),
        Author(author_id='A3', name='Carol', deleted=False),
    ]


def test_get_all_authors_return_authors(sample_authors):
    """Ensures get_all_authors() returns all author loaded from DAO."""
    with patch.object(AuthorSqliteDao, 'get_all', return_value=sample_authors) as mock_load_all:
        result = AuthorRepository.get_all_authors()
        assert result == sample_authors
        mock_load_all.assert_called_once()


@pytest.mark.parametrize('author_id, expected_name', [
    ('A1', 'Alice'),
    ('A2', 'Bob'),
    ('A3', 'Carol'),
])
def test_get_author_by_id_return_author(sample_authors, author_id, expected_name):
    """Ensures get_author_by_id() returns the correct Author when found."""
    with patch.object(AuthorSqliteDao, 'get_all', return_value=sample_authors) as mock_load_all:
        author = AuthorRepository.get_author_by_id(author_id)
        assert author.name == expected_name
        mock_load_all.assert_called_once()


def test_get_author_by_id_raises_error(sample_authors):
    """Ensures get_author_by_id() raises AuthorNotFoundError when ID is not found."""
    with patch.object(AuthorSqliteDao, 'get_all', return_value=sample_authors):
        with pytest.raises(AuthorNotFoundError, match="Author with ID X999 not found."):
            AuthorRepository.get_author_by_id('X999')


def test_options_returns_only_active_authors(sample_authors):
    """Ensure options() return tuples (id, name) only for non-deleted authors."""
    with patch.object(AuthorSqliteDao, 'get_all', return_value=sample_authors) as mock_load_all:
        result = AuthorRepository.options()
        expected = [('A1', 'Alice'), ('A3', 'Carol')]
        assert result == expected
        mock_load_all.assert_called_once()
