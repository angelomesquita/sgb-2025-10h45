from getpass import getpass
from typing import Tuple

from controller.customer_controller import CustomerController
from model.category import Category
from view.view import View


class CustomerView(View):

    __CUSTOMER_NOT_FOUND = 'Customer not found!\n'

    def __init__(self):
        self.controller = CustomerController()

    def show_menu(self) -> None:
        while True:
            self.clear_screen()
            print('\n=== Customer Module ===')  # Módulo de Usuário
            print('1. Register Customer ')
            print('2. List Customers ')
            print('3. Update Customer')  # Atualizar Usuário
            print('4. Delete Customer')  # Apagar Usuário
            print('0. Back to main menu')  # Voltar para o Menu Principal

            option = input('Select an option: ')  # Escolha uma opção

            if option == '1':
                self.register()
            elif option == '2':
                self.list()
            elif option == '3':
                self.update()
            elif option == '4':
                self.delete()
            elif option == '0':
                break
            else:
                print(View._MENU_INVALID_OPTION)  # Opção inválida
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

    def update(self) -> None:
        print('\n=== Update Customer ===')
        cpf = self.get_cpf()
        customer = self.controller.find(cpf)
        if customer:
            data = self.get_customer_data()
            self.controller.update(*data)
        else:
            print(self.__CUSTOMER_NOT_FOUND)
        self.press_enter_to_continue()
        self.clear_screen()

    def delete(self) -> None:
        print('\n=== Delete Customer ===')
        cpf = self.get_cpf()
        customer = self.controller.find(cpf)
        if customer:
            self.controller.delete(cpf)
        else:
            print(self.__CUSTOMER_NOT_FOUND)
        self.press_enter_to_continue()
        self.clear_screen()

    def get_customer_data(self) -> Tuple[str, str, str, str, str]:
        name = input('Name: ')
        cpf = self.get_cpf()
        contact = input('Contact: ')
        category = self.get_category_customer()
        password = getpass('Password: ')
        return name, cpf, contact, category, password

    @staticmethod
    def get_category_customer() -> str:
        print('Choose category: ')
        options = Category.options()
        for i, (value, label) in enumerate(options, start=1):
            print(f"{i}. {label}")
        while True:
            choice = input('Enter the category number: ')
            if choice.isdigit() and 1 <= int(choice) <= len(options):
                return options[int(choice)-1][0]
