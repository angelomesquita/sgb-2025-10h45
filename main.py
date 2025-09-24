from view.author_view import AuthorView
from view.book_view import BookView
from view.customer_view import CustomerView
from view.employee_view import EmployeeView
from view.publisher_view import PublisherView
from view.view import View


def main():
    while True:
        show_app_menu()

        option = input('Select an option: ')

        if option == '1':
            author_view = AuthorView()
            author_view.show_menu()
            View.clear_screen()
        elif option == '2':
            book_view = BookView()
            book_view.show_menu()
            View.clear_screen()
        elif option == '3':
            employee_view = EmployeeView()
            employee_view.show_menu()
            View.clear_screen()
        elif option == '4':
            customer_view = CustomerView()
            customer_view.show_menu()
            View.clear_screen()
        elif option == '5':
            publisher_view = PublisherView()
            publisher_view.show_menu()
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
    print('1. Author Module')
    print('2. Book Module')
    print('3. Employee Module')
    print('4. Customer Module')
    print('5. Publisher Module')
    print('0. Exit')


if __name__ == '__main__':
    main()
