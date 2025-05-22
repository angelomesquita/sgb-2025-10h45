def show_menu():
    print('=== Sistema Gerenciador de Bibliotecas ===')
    print('1 - Cadastrar Funcionario')
    print('2 - Listar Funcionarios')
    print('3 - Sair')


def request_employee_data():
    name = input('Nome: ')
    cpf = input('CPF: ')
    job_position = input('Cargo: ')
    login = input('Login: ')
    password = input('Senha: ')
    return name, cpf, job_position, login, password


def show_employees(employees):
    if not employees:
        print('No employees registered.\n')
        return
    print('\n=== Lista de Funcionários ===')
    for employee in employees:
        print(employee)
    print()
