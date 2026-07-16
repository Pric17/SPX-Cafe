from subsystems.customerSystem.repositories.customerRepository import CustomerRepository
from subsystems.customerSystem.models.customerModel import Customer

class CustomerService:

    def __init__(self):
        self.customerRepo = CustomerRepository()

    def findCustomer(self, username):
        return self.customerRepo.getByUsername(username)

    def registerCustomer(self, username, password, firstName, lastName):
        customer = Customer(username, password, firstName, lastName)
        self.customerRepo.addCustomer(customer)
        return customer

    def checkPassword(self, customer, password):
        return customer.password == password
