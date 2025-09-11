import re
from validators.validator import Validator


class CustomerValidator:

    @staticmethod
    def validate_name(name: str) -> bool:
        return Validator.min_length(name, 3)

    @staticmethod
    def validate_contact(contact: str) -> bool:
        """
        Validates email in simple format:
        - Must have at least one character before the first dot
        - Must contain a '.' before the '@'
        - Must contain a '.' after the '@'
        """
        pattern = r"^[^@]+?\.[^@]+?@[^@]+\.[^@]+$"
        return re.match(pattern, contact) is not None

    @staticmethod
    def validate_username(username: str) -> bool:
        return Validator.min_length(username, 4)

    @staticmethod
    def validate_password(password: str) -> bool:
        return Validator.min_length(password, 6)
