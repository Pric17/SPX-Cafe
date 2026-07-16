from subsystems.customerSystem.customerService import CustomerService
from subsystems.customerSystem.views.customerView import CustomerView
from subsystems.customerSystem.models.customerModel import Customer

class CustomerController:
    def __init__(self):
        self.service = CustomerService()
        self.view = CustomerView()

    def findCustomer(self, username: str = None) -> Customer:
        return self.service.findCustomer(username)

    def verifyPassword(self, customer: Customer, password: str) -> bool:
        return self.service.checkPassword(customer, password)

    def register(self, username, password, firstName, lastName) -> Customer:
        customer = self.service.registerCustomer(username, password, firstName, lastName)
        return customer

    # View helpers (the controller decides what the view shows)
    def welcomeBack(self, customer):
        self.view.welcomeBack(customer)

    def welcomeNew(self, customer):
        self.view.welcomeNew(customer)

    def askNewCustomer(self, username):
        self.view.askNewCustomer(username)

    def wrongPassword(self):
        self.view.wrongPassword()
