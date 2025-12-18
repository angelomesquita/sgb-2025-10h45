import pytest

from model.category import Category


@pytest.mark.parametrize("category, expected", [
    (Category.STUDENT, True),
    (Category.TEACHER, True),
    (Category.VISITOR, True),
    ("admin", False),
    ("", False),
    ("STUDENT", False)
])
def test_validate(category, expected):
    """Ensures validate() returns True only for the allowed categories."""
    assert Category.validate(category) is expected


@pytest.mark.parametrize("category, expected", [
    (Category.STUDENT, "estudante"),
    (Category.TEACHER, "professor"),
    (Category.VISITOR, "visitante"),
    ("STUDENT", "estudante"),
    ("Teacher", "professor"),
    ("visitor", "visitante"),
    ("unknown", "Unknown Category"),
    ("", "Unknown Category")
])
def test_translate(category, expected):
    """Ensures translate() returns the correct translation or 'Unknown Category'."""
    assert Category.translate(category) == expected


def test_options_return_all_items():
    """Ensures options() returns all translation pairs."""
    opts = Category.options()

    assert isinstance(opts, list)
    assert len(opts) == 3
    assert (Category.STUDENT, "estudante") in opts
    assert (Category.TEACHER, "professor") in opts
    assert (Category.VISITOR, "visitante") in opts
