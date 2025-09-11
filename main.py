from view.customer_view import CustomerView
from view.employee_view import EmployeeView
from view.view import View


def main():
    while True:
        show_app_menu()

        option = input('Select an option: ')

        if option == '1':
            employee_view = EmployeeView()
            employee_view.show_menu()
            View.clear_screen()
        elif option == '2':
            customer_view = CustomerView()
            customer_view.show_menu()
            View.clear_screen()
        elif option == '0':
            print('Exiting the system...')
            break
        else:
            print('Invalid option.')
            View.press_enter_to_continue()
            View.clear_screen()


def show_app_menu():
    print('\n=== Library Management System ===')
    print('1. Employee Module')
    print('2. Customer Module')
    print('0. Exit')


if __name__ == '__main__':
    main()
