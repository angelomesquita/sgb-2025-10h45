import os
from typing import List
from model.customer import Customer


class CustomerDao:
    __FILE_PATH = 'customers.txt'

    @staticmethod
    def save_all(customers: List[Customer]) -> None:
        with open(CustomerDao.__FILE_PATH, "w", encoding="utf-8") as file:
            for c in customers:
                line = f"{c.name}|{c.cpf}|{c.contact}|{c.category}|{c.password_hash}|{c.deleted}\n"
                file.write(line)

    @staticmethod
    def load_all() -> List[Customer]:
        if not os.path.exists(CustomerDao.__FILE_PATH):
            return []

        customers = []
        with open(CustomerDao.__FILE_PATH, "r", encoding="utf-8") as file:
            for line in file:
                name, cpf, contact, category, password_hash, deleted = line.strip().split("|")
                customer = Customer(name, cpf, contact, category, password_hash, deleted)
                customer.deleted = deleted.lower() == "true"
                customers.append(customer)

        return customers
