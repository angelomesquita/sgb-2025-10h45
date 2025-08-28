from controller.base_controller import BaseController
from model.category import Category
from model.customer import Customer
from model.customer_dao import CustomerDao


class CustomerController(BaseController[Customer]):

    def __init__(self):
        super().__init__(CustomerDao)

    def register(self, name: str, cpf: str, contact: str, category: str, password: str) -> None:
        if not Category.validate(category):
            print('Invalid category. Try again.\n')
            return
        super().register(cpf, name=name, contact=contact, category=category, password=password)

    def create_instance(self, name: str, cpf: str, contact: str, category: str, password_hash: str, deleted: bool = False) -> Customer:
        return Customer(name, cpf, contact, category, password_hash, deleted)

    def update(self, name: str, cpf: str, contact: str, category: str, password: str) -> None:
        super().update(cpf, name=name, contact=contact, category=category, password=password)

