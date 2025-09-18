from validators.validator import Validator


class AuthorValidator:

    @staticmethod
    def validate_author_id(author_id: str) -> bool:
        return author_id.isdigit()

    @staticmethod
    def validate_name(name: str) -> bool:
        return Validator.min_length(name, 3)
