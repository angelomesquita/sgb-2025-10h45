from model.employee import Employee
from model.auth import Auth
from model.cpf import Cpf
from typing import Optional


class EmployeeController:
    def __init__(self):
        self.employees = []

    def register(self, name: str, cpf: str, role: str, login: str, password: str) -> None:
        if self.find(cpf):
            print('An Employee with this CPF is already registered!\n')
            return
        if self.find_deleted(cpf):
            print('An Employee with this CPF was previously deleted.\n')
            return
        if not Cpf.validate(cpf):
            print('Invalid CPF. Try again.\n')
            return
        password_hash = Auth.hash_password(password)
        employee = Employee(name, cpf, role, login, password_hash)
        self.employees.append(employee)
        print('✅ Employee successfully registered!\n')

    def list(self) -> None:
        if not self.employees:
            print("No employees registered yet.")
            return
        active_employees = [emp for emp in self.employees if not getattr(emp, 'deleted', False)]
        if not active_employees:
            print("No active employees found.")
            return
        for employee in active_employees:
            print(employee)

    def find(self, cpf: str) -> Optional[Employee]:
        for employee in self.employees:
            if employee.cpf == cpf and employee.deleted is not True:
                return employee
        return None

    def find_deleted(self, cpf: str) -> Optional[Employee]:
        for employee in self.employees:
            if employee.cpf == cpf and getattr(employee, 'deleted', False) is True:
                return employee
        return None

    def update(self, name: str, cpf: str, role: str, login: str, password: str) -> None:
        for employee in self.employees:
            if employee.cpf == cpf and employee.deleted is not True:
                if name is not None:
                    employee.name = name
                if role is not None:
                    employee.role = role
                if login is not None:
                    employee.username = login
                if password is not None:
                    employee.password_hash = Auth.hash_password(password)
                print('Employee successfully updated!\n')
                return
        print('Employee not found!\n')

    def delete(self, cpf: str) -> None:
        for employee in self.employees:
            if employee.cpf == cpf and employee.deleted is not True:
                employee.deleted = True
                print('Employee successfully deleted!\n')
                return
        print('Employee not found!\n')
