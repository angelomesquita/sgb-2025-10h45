class Employee:

    # TODO: apply encapsulation by converting attributes to private or protected instead of public

    def __init__(self, name, cpf, role, login, password_hash):
        self.name = name
        self.cpf = cpf
        self.role = role
        self.login = login
        self.password_hash = password_hash

    def __str__(self):
        return f'Name: {self.name}, CPF: {self.cpf}, Role: {self.role}, Login: {self.login}'
