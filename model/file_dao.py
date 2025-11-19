import os
from model.exceptions import EmployeeLoadError
from typing import Generic, List, TypeVar
from abc import ABC, abstractmethod

T = TypeVar("T")  # Generic Type (Customer, Employee, etc...)


class FileDao(ABC, Generic[T]):
    _FILE_PATH: str

    @classmethod
    def save_all(cls, items: List[T]):
        with open(cls._FILE_PATH, "w", encoding="utf-8") as file:
            for item in items:
                file.write(cls._serialize(item) + "\n")

    @classmethod
    def load_all(cls) -> List[T]:
        if not os.path.exists(cls._FILE_PATH):
            return []

        items: List[T] = []
        try:
            with open(cls._FILE_PATH, "r", encoding="utf-8") as file:
                for line in file:
                    item = cls._deserialize(line.strip())
                    items.append(item)
        except Exception as e:
            raise EmployeeLoadError(f"Failed to load employees: {e}") from e

        return items

    @staticmethod
    @abstractmethod
    def _serialize(item: T) -> str:
        """Converts the object into a string to save to the file"""
        pass

    @staticmethod
    @abstractmethod
    def _deserialize(data: str) -> T:
        """Converts the string read from the file an object"""
        pass
