from getpass import getpass
from typing import Tuple

from controller.auth_controller import AuthController
from controller.employee_controller import EmployeeController
from view.view import View


class EmployeeView(View):
    __EMPLOYEE_NOT_FOUND = 'Employee not found!\n'

    def __init__(self):
        self.controller = EmployeeController()

    def show_menu(self) -> None:
        while True:
            self.clear_screen()
            print('\n=== Employee Module ===')  # Módulo de Funcionario
            print('1. Register Employee ')  # Cadastrar Funcionario
            print('2. List Employees')  # Listar Funcionarios
            print('3. Authenticate Employee')  # Autenticar Funcionario
            print('4. Update Employee')  # Atualizar Funcionario
            print('5. Delete Employee')  # Apagar Funcionario
            print('0. Back to main menu')  # Voltar para o Menu Principal

            option = input('Select an option: ')  # Escolha uma opção

            if option == '1':
                self.register()
            elif option == '2':
                self.list()
            elif option == '3':
                self.authenticate()
            elif option == '4':
                self.update()
            elif option == '5':
                self.delete()
            elif option == '0':
                break
            else:
                print(View._MENU_INVALID_OPTION)  # Opção inválida
                self.press_enter_to_continue()

    def register(self) -> None:
        print('\n=== Register Employee ===')
        data = self.get_employee_data()
        self.controller.register(*data)
        self.press_enter_to_continue()
        self.clear_screen()

    def list(self) -> None:
        print('\n=== List Employees ===')
        self.controller.list()
        self.press_enter_to_continue()
        self.clear_screen()

    def update(self) -> None:
        print('\n=== Update Employee ===')
        cpf = self.get_cpf()
        employee = self.controller.find(cpf)
        if employee:
            data = self.get_employee_data()
            self.controller.update(*data)
        else:
            print(self.__EMPLOYEE_NOT_FOUND)
        self.press_enter_to_continue()
        self.clear_screen()

    def delete(self) -> None:
        print('\n=== Delete Employee ===')
        cpf = self.get_cpf()
        employee = self.controller.find(cpf)
        if employee:
            self.controller.delete(cpf)
        else:
            print(self.__EMPLOYEE_NOT_FOUND)
        self.press_enter_to_continue()
        self.clear_screen()

    def authenticate(self) -> None:
        print('\n=== Authenticate Employee ===')
        username, password = self.get_auth_data()
        AuthController.auth(self.controller.employees, username, password)
        self.press_enter_to_continue()
        self.clear_screen()

    def get_employee_data(self) -> Tuple[str, str, str, str, str]:
        name = input('Name: ')
        cpf = self.get_cpf()
        role = input('Role: ')
        login, password = self.get_auth_data()
        return name, cpf, role, login, password

    def get_auth_data(self) -> Tuple[str, str]:
        username = input('Username: ')
        password = getpass('Password: ')
        return username, password
