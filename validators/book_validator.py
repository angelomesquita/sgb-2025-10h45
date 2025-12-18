from datetime import datetime
from validators.validator import Validator


class BookValidator:

    @staticmethod
    def validate_isbn(isbn: str) -> bool:
        return Validator.is_numeric(isbn)

    @staticmethod
    def validate_title(title: str) -> bool:
        return Validator.min_length(title, 5)

    @staticmethod
    def validate_year(year: str) -> bool:
        current_year = datetime.now().year
        return 0 < int(year) <= current_year

    @staticmethod
    def validate_quantity(quantity: str) -> bool:
        if not Validator.is_numeric(quantity):
            return False
        return int(quantity) > 0

    @staticmethod
    def validate_amount(amount: str) -> bool:
        try:
            int(amount)
            return True
        except ValueError:
            return False
