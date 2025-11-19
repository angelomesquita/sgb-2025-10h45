from controller.base_controller import BaseController
from model.author import Author
from model.author_file_dao import AuthorFileDao
from model.logger import author_logger
from model.exceptions import (
    AuthorAlreadyExistsError,
    AuthorDeletedError,
    AuthorNotFoundError,
    AuthorLoadError
)


class AuthorController(BaseController[Author]):

    dao_class = AuthorFileDao
    logger = author_logger

    AlreadyExistsError = AuthorAlreadyExistsError
    DeleteExistsError = AuthorDeletedError
    NotFoundError = AuthorNotFoundError
    LoadError = AuthorLoadError

    def __init__(self):
        super().__init__(model_class=Author, key_field="author_id")

    def register(self, author_id: str, name: str) -> None:
        super().register(author_id, name=name)

    def create_instance(self, author_id: str, name: str, deleted: bool = False) -> Author:
        return Author(author_id, name, deleted)

    def update(self, author_id: str, name: str) -> None:
        super().update(author_id, name=name)

    # TODO: def delete(self, author_id: str) -> None
    # TODO: search book_repository if exists book with this author
