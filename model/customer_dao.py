from model.file_dao import FileDao
from model.customer import Customer


class CustomerDao(FileDao[Customer]):
    _FILE_PATH = 'customers.txt'

    @staticmethod
    def _serialize(c: Customer) -> str:
        return f"{c.name}|{c.cpf}|{c.contact}|{c.category}|{c.password_hash}|{c.deleted}"

    @staticmethod
    def _deserialize(data: str) -> Customer:
        name, cpf, contact, category, password_hash, deleted = data.split("|")
        customer = Customer(name, cpf, contact, category, password_hash, deleted)
        customer.deleted = deleted.lower() == "true"

        return customer
