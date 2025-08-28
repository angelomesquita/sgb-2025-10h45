from controller.base_controller import BaseController
from model.auth import Auth
from model.employee import Employee
from model.employee_dao import EmployeeDao
from model.logger import employee_logger


class EmployeeController(BaseController[Employee]):

    dao_class = EmployeeDao
    logger = employee_logger

    def register(self, name: str, cpf: str, role: str, login: str, password: str) -> None:
        super().register(cpf, name=name, role=role, login=login, password=password)

    def create_instance(self, name: str, cpf: str, contact: str, category: str, password_hash: str, deleted: bool = False) -> Employee:
        return Employee(name, cpf, contact, category, password_hash, deleted)

    def update(self, name: str, cpf: str, role: str, login: str, password: str) -> None:
        super().update(cpf, name=name, role=role, login=login, password=password)
