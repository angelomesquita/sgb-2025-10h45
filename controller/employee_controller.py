from model.employee import Employee


class EmployeeController:
    def __init__(self):
        self.employees = []

    def save(self, name, cpf, job_position, login, password):
        employee = Employee(name, cpf, job_position, login, password)
        self.employees.append(employee)
        print('✅ Employee successfully registered!\n')

    def all(self):
        return self.employees
