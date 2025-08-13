import os
from typing import List
from model.employee import Employee


class EmployeeDao:
    __FILE_PATH = 'employees.txt'

    @staticmethod
    def save_all(employees: List[Employee]) -> None:
        with open(EmployeeDao.__FILE_PATH, "w", encoding="utf-8") as file:
            for e in employees:
                line = f"{e.name}|{e.cpf}|{e.role}|{e.username}|{e.password_hash}|{e.deleted}\n"
                file.write(line)

    @staticmethod
    def load_all() -> List[Employee]:
        if not os.path.exists(EmployeeDao.__FILE_PATH):
            return []

        employees = []
        with open(EmployeeDao.__FILE_PATH, "r", encoding="utf-8") as file:
            for line in file:
                name, cpf, role, username, password_hash, deleted = line.strip().split("|")
                employee = Employee(name, cpf, role, username, password_hash, deleted)
                employee.deleted = deleted.lower() == "true"
                employees.append(employee)

        return employees
