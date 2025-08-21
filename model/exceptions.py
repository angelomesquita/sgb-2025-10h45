"""
exceptions.py

This module defines custom exception classes related to Employee management.
These exceptions are intended to provide meaningful error handling and improve
readability throughout the application, following the principle of explicitness.

Hierarchy:
    - EmployeeError (base class for all Employee-related exceptions)
        - EmployeeAlreadyExistsError
        - EmployeeDeletedError
        - EmployeeNotFoundError
        - InvalidCpfError
"""


class EmployeeError(Exception):
    """Base class for Employee-related errors."""
    pass


class EmployeeAlreadyExistsError(EmployeeError):
    """Raised when trying to register an employee with an existing CPF."""
    pass


class EmployeeDeletedError(EmployeeError):
    """Raised when trying to register/update a deleted employee."""
    pass


class EmployeeNotFoundError(EmployeeError):
    """Raised when employee cannot be found."""
    pass


class InvalidCpfError(EmployeeError):
    """Raised when CPF validation fails."""
    pass
