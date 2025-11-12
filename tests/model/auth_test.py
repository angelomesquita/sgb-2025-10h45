import bcrypt
import pytest

from model.auth import Auth
from unittest.mock import Mock


@pytest.fixture
def credentials():
    """
    Fixture that provides basic authentication credentials for the tests.

    Returns:
        dict: A dictionary containing:
            - 'username' (str): valid username
            - 'password' (str): plain text password
            - 'hashed' (str): bcrypt hash generated from the password
    """
    username = 'admin'
    password = '123'
    hashed = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')
    return {'username': username, 'password': password, 'hashed': hashed}


def test_hash_password_creates_valid_hash(credentials):
    """
    Ensure that the hash_password() method creates a valid bcrypt hash
    that is not equal to the original password.

    Scenario:
        - Uses the password provided by the `credentials` fixture.
        - Verifies that the generated hash is a string, different from
          the plain password, and matches the original when validated
          using bcrypt.
    """
    hashed = Auth.hash_password(password=credentials['password'])

    assert isinstance(hashed, str)
    assert hashed != credentials['password']
    assert bcrypt.checkpw(credentials['password'].encode('utf-8'), hashed.encode('utf-8'))


@pytest.mark.parametrize("password, expected", [
    ('123', True),
    ('WrongPassword', False)
])
def test_verify_password(credentials, password, expected):
    """
    Verify that the verify_password() method behaves correctly for both
    matching and non-matching passwords.

    Parameters (via parametrize):
        - password (str): Input password to be checked.
        - expected (bool): Expected result (True if match, False otherwise).

    Fixtures:
        - credentials: Provides the valid hashed password.

    The test ensures that Auth.verify_password() returns the correct boolean
    value depending on whether the given password matches the stored hash.
    """
    assert Auth.verify_password(password, credentials['hashed']) is expected


@pytest.mark.parametrize("username, password, expected", [
    ('admin', '123', True),
    ('user', '123', False),
    ('admin', '1234', False),
])
def test_auth(credentials, username, password, expected):
    """
    Test the auth() method for different combinations of username and password.

    Parameters (via parametrize):
        - username (str): Username provided for authentication.
        - password (str): Password provided for authentication.
        - expected (bool): Expected result (True for success, False for failure).

    Fixtures:
        - credentials: Provides valid user credentials (username and hash).

    The test mocks an employee object and checks whether Auth.auth() returns
    the expected authentication result for each scenario.
    """
    employee = Mock()
    employee.username = credentials['username']
    employee.password_hash = credentials['hashed']

    assert Auth.auth(employee, username, password) is expected
