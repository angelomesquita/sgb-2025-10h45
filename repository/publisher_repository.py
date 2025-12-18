from typing import Iterable, Tuple
from model.publisher import Publisher
from model.publisher_dao import PublisherDao
from model.exceptions import PublisherNotFoundError


class PublisherRepository:

    @staticmethod
    def get_all_publishers() -> Iterable[Publisher]:
        """Load all publishers from DAO (active and deleted)"""
        return PublisherDao.get_all()

    @staticmethod
    def get_publisher_by_id(publisher_id: str) -> Publisher:
        publishers = PublisherRepository.get_all_publishers()
        publisher = next((p for p in publishers if str(p.publisher_id) == publisher_id), None)
        if publisher is None:
            raise PublisherNotFoundError(f"Publisher with ID {publisher_id} not found.")
        return publisher

    @staticmethod
    def options() -> Iterable[Tuple[str, str]]:
        publishers = PublisherRepository.get_all_publishers()
        return [(str(p.publisher_id), p.legal_name) for p in publishers if not p.deleted]
