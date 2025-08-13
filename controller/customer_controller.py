from model.category import Category
from model.customer import Customer
from model.customer_dao import CustomerDao
from model.auth import Auth
from model.cpf import Cpf
from typing import Optional


class CustomerController:
    def __init__(self):
        self.customers = CustomerDao.load_all()

    def register(self, name: str, cpf: str, contact: str, category: str, password: str) -> None:
        if self.find(cpf):
            print('An Customer with this CPF is already registered!\n')
            return
        if self.find_deleted(cpf):
            print('An Customer with this CPF was previously deleted.\n')
            return
        if not Cpf.validate(cpf):
            print('Invalid CPF. Try again.\n')
            return
        if not Category.validate(category):
            print('Invalid category. Try again.\n')
            return
        password_hash = Auth.hash_password(password)
        customer = Customer(name, cpf, contact, category, password_hash)
        self.customers.append(customer)
        CustomerDao.save_all(self.customers)
        print('✅ Customer successfully registered!\n')

    def list(self) -> None:
        if not self.customers:
            print("No customers registered yet.")
            return
        active_customers = [cust for cust in self.customers if not getattr(cust, 'deleted', False)]
        if not active_customers:
            print("No active customers found.")
            return
        for customer in active_customers:
            print(customer)

    def find(self, cpf: str) -> Optional[Customer]:
        for customer in self.customers:
            if customer.cpf == cpf and customer.deleted is not True:
                return customer
        return None

    def find_deleted(self, cpf: str) -> Optional[Customer]:
        for customer in self.customers:
            if customer.cpf == cpf and getattr(customer, 'deleted', False) is True:
                return customer
        return None

    def update(self, name: str, cpf: str, contact: str, category: str, password: str) -> None:
        for customer in self.customers:
            if customer.cpf == cpf and customer.deleted is not True:
                if name is not None:
                    customer.name = name
                if contact is not None:
                    customer.contact = contact
                if category is not None:
                    customer.category = category
                if password is not None:
                    customer.password_hash = Auth.hash_password(password)
                print('Customer successfully updated!\n')
                CustomerDao.save_all(self.customers)
                return
        print('Customer not found!\n')

    def delete(self, cpf: str) -> None:
        for customer in self.customers:
            if customer.cpf == cpf and customer.deleted is not True:
                customer.deleted = True
                print('Customer successfully deleted!\n')
                CustomerDao.save_all(self.customers)
                return
        print('Customer not found!\n')
