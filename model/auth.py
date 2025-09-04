import bcrypt
from model.employee import Employee


class Auth:

    @staticmethod
    def hash_password(password: str) -> str:
        password_bytes = password.encode('utf-8')
        return bcrypt.hashpw(password_bytes, bcrypt.gensalt()).decode('utf-8')

    @staticmethod
    def verify_password(password: str, password_hash: str) -> bool:
        return bcrypt.checkpw(password.encode('utf-8'), password_hash.encode('utf-8'))

    @staticmethod
    def auth(employee: Employee, username: str, password: str) -> bool:
        if employee.username == username and Auth.verify_password(password, employee.password_hash):
            return True
        return False
