from subsystems.customerSystem.customerController import CustomerController
from subsystems.customerSystem.models.customerModel import Customer

class CustomerFacade:
    def __init__(self):
        self.controller = CustomerController()

    def findCustomer(self, username=None) -> Customer:
        return self.controller.findCustomer(username)

    def verifyPassword(self, customer, password) -> bool:
        return self.controller.verifyPassword(customer, password)

    def register(self, username, password, firstName, lastName) -> Customer:
        return self.controller.register(username, password, firstName, lastName)

    def welcomeBack(self, customer):
        self.controller.welcomeBack(customer)

    def welcomeNew(self, customer):
        self.controller.welcomeNew(customer)

    def askNewCustomer(self, username):
        self.controller.askNewCustomer(username)

    def wrongPassword(self):
        self.controller.wrongPassword()
