from validators.validator import Validator


def test_not_empty_with_non_empty_string():
    """Should return True for a non-empty string."""
    assert Validator.not_empty("Hello") is True


def test_not_empty_with_whitespace_string():
    """Should return False when string contains only spaces."""
    assert Validator.not_empty("    ") is False


def test_not_empty_with_empty_string():
    """Should return False when string is empty."""
    assert Validator.not_empty("") is False
