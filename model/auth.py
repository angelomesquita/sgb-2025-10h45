import bcrypt


class Auth:

    @staticmethod
    def hash_password(password):
        password_bytes = password.encode('utf-8')
        return bcrypt.hashpw(password_bytes, bcrypt.gensalt())

    @staticmethod
    def verify_password(password, password_hash):
        return bcrypt.checkpw(password.encode('utf-8'), password_hash)

    @staticmethod
    def auth(employee, username, password):
        if employee.username == username and Auth.verify_password(password, employee.password_hash):
            return True
        return False
