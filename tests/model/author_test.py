from model.author import Author


def test_it_should_create_author_default_deleted_false():
    """Checks if the author is created correctly with deleted=False by default."""
    author = Author(author_id="JD01", name="John Doe")
    assert author.author_id == "JD01"
    assert author.name == "John Doe"
    assert author.deleted is False


def test_it_should_create_author_with_deleted_true():
    """Checks if the author can be created with deleted=True"""
    author = Author(author_id="JD01", name="John Doe", deleted=True)
    assert author.deleted is True


def test_it_should_check_setters_update_values_correctly():
    """Checks if the setters correctly update the attribute values."""
    author = Author(author_id="JD01", name="John Doe")

    expected_id = "JD02"
    expected_name = "John Doe UPDATED"
    expected_deleted = True

    author.author_id = expected_id
    author.name = expected_name
    author.deleted = expected_deleted
    assert author.author_id == expected_id
    assert author.name == expected_name
    assert author.deleted is expected_deleted


def test_it_should_check_str_representation():
    """Checks if the __str__ method returns the correctly formatted string"""
    author = Author(author_id="JD01", name="John Doe")
    expected = "ID: JD01 - Name: John Doe"
    assert str(author) == expected
