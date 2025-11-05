import bcrypt
from model.auth import Auth
from unittest.mock import Mock


def test_hash_password_creates_valid_hash():
    """Ensure hash_password method returns a valid bcrypt hash and is not equal to the original password."""
    password = "123"
    hashed = Auth.hash_password(password=password)

    assert isinstance(hashed, str)
    assert hashed != password
    assert bcrypt.checkpw(password.encode('utf-8'), hashed.encode('utf-8'))


def test_verify_password_returns_true_for_correct_password():
    """Ensure verify_password returns True for a matching password."""
    password = "123"
    hashed = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')

    assert Auth.verify_password(password, hashed) is True


def test_verify_password_returns_false_for_incorrect_password():
    """Ensure verify_password returns False for a wrong password."""
    password = "123"
    hashed = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')

    assert Auth.verify_password("WrongPassword", hashed) is False


def test_auth_returns_true_when_username_and_password_match():
    """Ensure auth() return True when username and password are correct."""
    expected_username = "admin"
    password = "123"
    hashed = Auth.hash_password(password=password)

    employee = Mock()
    employee.username = expected_username
    employee.password_hash = hashed

    assert Auth.auth(employee, expected_username, password) is True


def test_auth_returns_false_when_username_is_wrong():
    """Ensure auth() return False when username does not match."""
    expected_username = "admin"
    password = "123"
    hashed = Auth.hash_password(password=password)

    employee = Mock()
    employee.username = expected_username
    employee.password_hash = hashed

    assert Auth.auth(employee, "wrong_username", password) is False


def test_auth_returns_false_when_password_is_wrong():
    """Ensure auth() return False when password does not match."""
    expected_username = "admin"
    password = "123"
    hashed = Auth.hash_password(password=password)

    employee = Mock()
    employee.username = expected_username
    employee.password_hash = hashed

    assert Auth.auth(employee, expected_username, "wrong_password") is False
