import bcrypt


class Auth:

    @staticmethod
    def hash_password(password):
        password_bytes = password.enconde('utf-8')
        return bcrypt.hashpw(password_bytes, bcrypt.gensalt())

    # TODO: def __verify_password(password, password_hash):

    # TODO: def auth(username, password):
