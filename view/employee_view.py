import os


def show_menu():
    clear_screen()
    print('\n=== Library Management System ===')  # Sistema Gerenciador de Bibliotecas
    print('1. Register Employee ')  # Cadastrar Funcionario
    print('2. List Employees')  # Listar Funcionarios
    print('3. Authenticate Employee')  # Autenticar Funcionario
    print('4. Update Employee') # Atualizar Funcionario
    print('0. Exit')  # Sair


def register_employee(controller):
    print('\n=== Register Employee ===')
    data = get_employee_data()
    controller.register(*data)
    press_enter_to_continue()


def list_employees(controller):
    print('\n=== List Employees ===')
    controller.list()
    press_enter_to_continue()


def update_employee(controller):
    print('\n=== Update Employee ===')
    cpf = input('CPF: ')
    employee = controller.find(cpf)
    if employee:
        data = get_employee_data()
        controller.update(*data)
    press_enter_to_continue()


def authenticate_employee(controller):
    print('\n=== Authenticate Employee ===')
    auth_data = get_auth_data()
    controller.auth(*auth_data)
    press_enter_to_continue()


def get_employee_data():
    name = input('Name: ')
    cpf = input('CPF: ')
    role = input('Role: ')
    login = input('Username: ')
    password = input('Password: ')
    return name, cpf, role, login, password


def get_auth_data():
    username = input('Username: ')
    password = input('Password: ')
    return username, password


def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


def press_enter_to_continue():
    input('Press Enter to continue...')
