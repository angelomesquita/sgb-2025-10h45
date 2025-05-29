from model.employee import Employee
from model.auth import Auth


class EmployeeController:
    def __init__(self):
        self.employees = []

    def register(self, name, cpf, role, login, password):
        password_hash = Auth.hash_password(password)
        employee = Employee(name, cpf, role, login, password_hash)
        self.employees.append(employee)
        print('✅ Employee successfully registered!\n')

    def list(self):
        if not self.employees:
            print("No employees registered yet.")
            return
        for employee in self.employees:
            if not employee.deleted:
                print(employee)

    def find(self, cpf):
        for employee in self.employees:
            if employee.cpf == cpf and employee.deleted is not True:
                return employee
        print('Employee not found!\n')
        return None

    def update(self, name, cpf, role, login, password):
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

    def delete(self, cpf):
        for employee in self.employees:
            if employee.cpf == cpf and employee.deleted is not True:
                employee.deleted = True
                print('Employee successfully deleted!\n')
                return
        print('Employee not found!\n')

    def auth(self, username, password):
        for employee in self.employees:
            if Auth.auth(employee, username, password) and employee.deleted is not True:
                print(f'Welcome, {employee.name}')
                return True
        print('Authentication failed.')
        return False
