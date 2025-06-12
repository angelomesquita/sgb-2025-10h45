import os
from view.employee_view import EmployeeView
from view.customer_view import CustomerView


def main():

    while True:
        show_app_menu()

        option = input('Select an option: ') # Escolha uma opção

        if option == '1':
            employee_view = EmployeeView()
            employee_view.show_menu()
            clear_screen()
        elif option == '2':
            customer_view = CustomerView()
            customer_view.show_menu()
            clear_screen()
        elif option == '0':
            print('Exiting the system...') # Saindo do sistema
            break
        else:
            print('Invalid option.') # Opção inválida
            press_enter_to_continue()


def clear_screen() -> None:
    os.system('cls' if os.name == 'nt' else 'clear')


def press_enter_to_continue() -> None:
    input('Press Enter to continue...')


def show_app_menu():
    print('\n=== Library Management System ===')  # Sistema Gerenciador de Bibliotecas
    print('1. Employee Module')  # Módulo Funcionário
    print('2. Customer Module')  # Módulo Usuário (Estudante, Professor ou Visitante)
    print('0. Exit') # Sair do Sistema


if __name__ == '__main__':
    main()
