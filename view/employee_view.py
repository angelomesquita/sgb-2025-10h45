import os
from controller.employee_controller import EmployeeController
from controller.auth_controller import AuthController
from typing import Tuple


def show_menu():
    clear_screen()
    print('\n=== Library Management System ===')  # Sistema Gerenciador de Bibliotecas
    print('1. Register Employee ')  # Cadastrar Funcionario
    print('2. List Employees')  # Listar Funcionarios
    print('3. Authenticate Employee')  # Autenticar Funcionario
    print('4. Update Employee')  # Atualizar Funcionario
    print('5. Delete Employee')  # Apagar Funcionario
    print('0. Exit')  # Sair


def register_employee(controller: EmployeeController) -> None:
    print('\n=== Register Employee ===')
    data = get_employee_data()
    controller.register(*data)
    press_enter_to_continue()


def list_employees(controller: EmployeeController) -> None:
    print('\n=== List Employees ===')
    controller.list()
    press_enter_to_continue()


def update_employee(controller: EmployeeController) -> None:
    print('\n=== Update Employee ===')
    cpf = get_cpf_employee()
    employee = controller.find(cpf)
    if employee:
        data = get_employee_data()
        controller.update(*data)
    else:
        print(employee_not_found())
    press_enter_to_continue()


def delete_employee(controller: EmployeeController) -> None:
    print('\n=== Delete Employee ===')
    cpf = get_cpf_employee()
    employee = controller.find(cpf)
    if employee:
        controller.delete(cpf)
    else:
        print(employee_not_found())
    press_enter_to_continue()


def authenticate_employee(controller: EmployeeController) -> None:
    print('\n=== Authenticate Employee ===')
    username, password = get_auth_data()
    AuthController.auth(controller.employees, username, password)
    press_enter_to_continue()


def get_employee_data() -> Tuple[str, str, str, str, str]:
    name = input('Name: ')
    cpf = get_cpf_employee()
    role = input('Role: ')
    login, password = get_auth_data()
    return name, cpf, role, login, password


def get_auth_data() -> Tuple[str, str]:
    username = input('Username: ')
    password = input('Password: ')
    return username, password


def get_cpf_employee() -> str:
    cpf = input('CPF: ')
    return cpf


def clear_screen() -> None:
    os.system('cls' if os.name == 'nt' else 'clear')


def press_enter_to_continue() -> None:
    input('Press Enter to continue...')


def employee_not_found() -> str:
    return 'Employee not found!\n'
