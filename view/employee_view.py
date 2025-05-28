import os


def show_menu():
    clear_screen()
    print('\n=== Library Management System ===') # Sistema Gerenciador de Bibliotecas
    print('1. Register Employee ') # Cadastrar Funcionario
    print('2. List Employees') # Listar Funcionarios
    print('3. Authenticate Employee') # Autenticar Funcionario
    print('0. Exit') # Sair


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
