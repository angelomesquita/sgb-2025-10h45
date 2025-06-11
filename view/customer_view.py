from view.view import View
from controller.customer_controller import CustomerController
from typing import Tuple
from getpass import getpass


class CustomerView(View):

    def show_menu(self) -> None:
        self.clear_screen()
        print('\n=== Customer Module ===')  # Módulo de Usuário
        print('1. Register Customer ')  # Cadastrar Usuário (Estudante, Professor ou Visitante)
        #print('2. List Employees')  # Listar Funcionarios
        #print('3. Authenticate Employee')  # Autenticar Funcionario
        #print('4. Update Employee')  # Atualizar Funcionario
        #print('5. Delete Employee')  # Apagar Funcionario
        #print('0. Exit')  # Sair

    def register_employee(self, controller: CustomerController) -> None:
        print('\n=== Register Employee ===')
        data = self.get_customer_data()
        controller.register(*data)
        self.press_enter_to_continue()

    def get_customer_data(self) -> Tuple[str, str, str, str, str]:
        name = input('Name: ')
        cpf = self.get_cpf_customer()
        role = input('Role: ')
        login, password = self.get_auth_data()
        return name, cpf, role, login, password

    def get_auth_data(self) -> Tuple[str, str]:
        username = input('Username: ')
        password = getpass('Password: ')
        return username, password

    def get_cpf_customer(self) -> str:
        cpf = input('CPF: ')
        return cpf
