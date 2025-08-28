from typing import Generic, List, Optional, TypeVar
from abc import ABC, abstractmethod
from model.auth import Auth
from model.cpf import Cpf

T = TypeVar("T")  # Generic type (Employee, Customer, etc...)
D = TypeVar("D")  # Generic type (DAO)


class BaseController(ABC, Generic[T]):

    def __init__(self, dao_class: D):
        self.dao_class = dao_class
        self.items: List[T] = self.dao_class.load_all()

    @abstractmethod
    def create_instance(self, *args, **kwargs) -> T:
        """Creates a new instance of the object (Customer, Employee, etc...)"""
        pass

    def register(self, *args, **kwargs):
        cpf = kwargs.get("cpf") or (args[1] if len(args) > 1 else None)
        self._register_logic(cpf, **kwargs)

    def _register_logic(self, cpf: str, **kwargs) -> None:
        if self.find(cpf):
            print('An entry with this CPF is already registered!\n')
            return
        if self.find_deleted(cpf):
            print('An entry with this CPF was previously deleted.\n')
            return
        if not Cpf.validate(cpf):
            print('Invalid CPF. Try again.\n')
            return

        if "password" in kwargs:
            password = kwargs.pop("password")
            kwargs["password_hash"] = Auth.hash_password(password)

        item = self.create_instance(cpf=cpf, **kwargs)
        self.items.append(item)
        self.dao_class.save_all(self.items)
        print(f'✅ {item.__class__.__name__} successfully registered!\n')

    def list(self) -> None:
        if not self.items:
            print("No entries registered yet.")
            return
        active_items = [item for item in self.items if not getattr(item, 'deleted', False)]
        if not active_items:
            print("No active entries found.")
            return
        for item in active_items:
            print(item)

    def find(self, cpf: str) -> Optional[T]:
        for item in self.items:
            if item.cpf == cpf and item.deleted is not True:
                return item
        return None

    def find_deleted(self, cpf: str) -> Optional[T]:
        for item in self.items:
            if item.cpf == cpf and getattr(item, 'deleted', False) is True:
                return item
        return None

    def update(self, cpf: str, **kwargs) -> None:
        for item in self.items:
            if item.cpf == cpf and not item.deleted:
                for field, value in kwargs.items():
                    if value is not None:
                        if field == "password":
                            setattr(item, "password_hash", Auth.hash_password(value))
                        else:
                            setattr(item, field, value)
                self.dao_class.save_all(self.items)
                print(f'✅ {item.__class__.__name__} successfully updated!\n')
                return
        print(f'Entry not found!\n')

    def delete(self, cpf: str) -> None:
        for item in self.items:
            if item.cpf == cpf and item.deleted is not True:
                item.deleted = True
                print(f'{item.__class__.__name__} successfully deleted!\n')
                self.dao_class.save_all(self.items)
                return
        print(f'Entry not found!\n')
