import pytest

from unittest.mock import patch
from model.publisher import Publisher
from model.publisher_dao import PublisherDao
from repository.publisher_repository import PublisherRepository
from model.exceptions import PublisherNotFoundError


@pytest.fixture
def sample_publishers():
    """Fixture that provides a sample list of Publisher objects."""
    return [
        Publisher(publisher_id='P1', legal_name='Publisher 1', city='New York', state='New York', deleted=False),
        Publisher(publisher_id='P2', legal_name='Publisher 2', city='New York', state='New York', deleted=True),
        Publisher(publisher_id='P3', legal_name='Publisher 3', city='New York', state='New York', deleted=False),
    ]


def test_get_all_publishers_return_publishers(sample_publishers):
    """Ensures get_all_publishers() returns all publisher loaded from DAO."""
    with patch.object(PublisherDao, 'get_all', return_value=sample_publishers) as mock_load_all:
        result = PublisherRepository._get_all_publishers()
        assert result == sample_publishers
        mock_load_all.assert_called_once()


@pytest.mark.parametrize('publisher_id, expected_legal_name', [
    ('P1', 'Publisher 1'),
    ('P2', 'Publisher 2'),
    ('P3', 'Publisher 3'),
])
def test_get_publisher_by_id_return_publisher(sample_publishers, publisher_id, expected_legal_name):
    """Ensures get_publisher_by_id() returns the correct Publisher when found."""
    with patch.object(PublisherDao, 'get_all', return_value=sample_publishers) as mock_load_all:
        publisher = PublisherRepository.get_publisher_by_id(publisher_id)
        assert publisher.legal_name == expected_legal_name
        mock_load_all.assert_called_once()


def test_get_publisher_by_id_raises_error(sample_publishers):
    """Ensures get_publisher_by_id() raises PublisherNotFoundError when ID is not found."""
    with patch.object(PublisherDao, 'get_all', return_value=sample_publishers):
        with pytest.raises(PublisherNotFoundError, match="Publisher with ID X999 not found."):
            PublisherRepository.get_publisher_by_id('X999')


def test_options_returns_only_active_publishers(sample_publishers):
    """Ensure options() return tuples (id, legal_name) only for non-deleted publishers."""
    with patch.object(PublisherDao, 'get_all', return_value=sample_publishers) as mock_load_all:
        result = PublisherRepository.options()
        expected = [('P1', 'Publisher 1'), ('P3', 'Publisher 3')]
        assert result == expected
        mock_load_all.assert_called_once()
