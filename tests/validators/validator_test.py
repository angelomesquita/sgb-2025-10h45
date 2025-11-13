import pytest

from validators.validator import Validator


@pytest.mark.parametrize('value, expected', [
    ('Hello', True),
    ('    ', False),
    ('', False)
])
def test_not_empty(value, expected):
    """Checks that not_empty return True for non-empty strings and False otherwise."""
    assert Validator.not_empty(value) is expected


@pytest.mark.parametrize('value, min_length, expected', [
    ('Hello', 3, True),  # Longer that min_length
    ('Hi', 3, False),  # Shorter than min_length
    ('    ', 1, False),  # Whitespace only
    ('  Test  ', 4, True),  # Trimmed string valid
])
def test_min_length(value, min_length, expected):
    """Checks that min_length validates string length correctly, ignoring whitespaces."""
    assert Validator.min_length(value, min_length) is expected


@pytest.mark.parametrize('value, expected', [
    ('12345', True),
    ('12a45', False),
    ('', False),
    ('  ', False),
])
def test_is_numeric(value, expected):
    """Checks that is_numeric return True only when string contain digits only."""
    assert Validator.is_numeric(value) is expected
