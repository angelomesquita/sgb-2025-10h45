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
            print(employee)

    def auth(self, username, password):
        for employee in self.employees:
            if Auth.auth(employee, username, password):
                print(f'Welcome, {employee.name}')
                return True
        print('Authentication failed.')
        return False
