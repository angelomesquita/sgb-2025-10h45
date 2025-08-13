
class Person:

    def __init__(self, name: str, cpf: str, password_hash: str, deleted: bool = False):
        self._name = name
        self._cpf = cpf
        self._password_hash = password_hash
        self._deleted = deleted

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value: str):
        self._name = value

    @property
    def cpf(self):
        return self._cpf

    @cpf.setter
    def cpf(self, value: str):
        self._cpf = value

    @property
    def password_hash(self):
        return self._password_hash

    @password_hash.setter
    def password_hash(self, value: str):
        self._password_hash = value

    @property
    def deleted(self):
        return self._deleted

    @deleted.setter
    def deleted(self, value: bool):
        self._deleted = value
