import os
from model.cpf import Cpf


class View:

    _MENU_INVALID_OPTION = 'Invalid option.'

    @staticmethod
    def clear_screen() -> None:
        os.system('cls' if os.name == 'nt' else 'clear')

    @staticmethod
    def press_enter_to_continue() -> None:
        input('Press Enter to continue...')

    @staticmethod
    def get_cpf() -> str:
        while True:
            cpf = input('CPF: ')
            if Cpf.validate(cpf):
                return cpf
            print('Invalid CPF. Try again.\n')
