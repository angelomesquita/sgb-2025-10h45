from model.file_dao import FileDao
from model.author import Author


class AuthorFileDao(FileDao[Author]):
    _FILE_PATH = 'authors.txt'

    @staticmethod
    def _serialize(a: Author) -> str:
        return f"{a.author_id}|{a.name}|{a.deleted}"

    @staticmethod
    def _deserialize(data: str) -> Author:
        author_id, name, deleted = data.split("|")
        author = Author(author_id, name, deleted)
        author.deleted = deleted.lower() == "true"

        return author
