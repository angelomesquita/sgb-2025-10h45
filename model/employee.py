class Employee:
    def __init__(self, name, cpf, job_position, login, password):
        self.name = name
        self.cpf = cpf
        self.job_position = job_position
        self.login = login
        self.password = password

    def __str__(self):
        return f'Name: {self.name}, CPF: {self.cpf}, Job Position: {self.job_position}, Login: {self.login}'
