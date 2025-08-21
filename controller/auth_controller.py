from model.auth import Auth
from model.logger import auth_logger


class AuthController:

    @staticmethod
    def auth(employees: list, username: str, password: str) -> bool:
        for employee in employees:
            if Auth.auth(employee, username, password) and employee.deleted is not True:
                print(f'Welcome, {employee.name}')
                auth_logger.debug(f"Login attempt successfully for employee: {employee.username} ({employee.name})")
                return True
        print('Authentication failed.')
        auth_logger.debug(f"Login attempt failed for employee: {employee.username} ({employee.name})")
        return False
