from view.view import View
from controller.customer_controller import CustomerController
from typing import Tuple
from getpass import getpass


class CustomerView(View):

    def __init__(self):
        self.controller = CustomerController()

    def show_menu(self) -> None:
        while True:
            self.clear_screen()
            print('\n=== Customer Module ===')  # Módulo de Usuário
            print('1. Register Customer ')
            print('2. List Customers ')
            print('0. Back to main menu')  # Voltar para o Menu Principal

            option = input('Select an option: ')  # Escolha uma opção

            if option == '1':
                self.register()
            elif option == '2':
                self.list()
            elif option == '0':
                break
            else:
                print(self.__MENU_INVALID_OPTION)  # Opção inválida
                self.press_enter_to_continue()

    def register(self) -> None:
        print('\n=== Register Customer ===')
        data = self.get_customer_data()
        self.controller.register(*data)
        self.press_enter_to_continue()
        self.clear_screen()

    def list(self) -> None:
        print('\n=== List Customers ===')
        self.controller.list()
        self.press_enter_to_continue()
        self.clear_screen()

    def get_customer_data(self) -> Tuple[str, str, str, str, str]:
        name = input('Name: ')
        cpf = self.get_cpf_customer()
        contact = input('Contact: ')
        category = input('Category: ')
        password = self.get_auth_data()
        return name, cpf, contact, category, password

    def get_auth_data(self) -> Tuple[str, str]:
        password = getpass('Password: ')
        return password

    def get_cpf_customer(self) -> str:
        cpf = input('CPF: ')
        return cpf
