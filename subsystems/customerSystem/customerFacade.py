from subsystems.customerSystem.customerController import CustomerController
from subsystems.customerSystem.orderController import OrderController
from subsystems.customerSystem.models.customerModel import Customer

class CustomerFacade:
    def __init__(self):
        self.controller = CustomerController()
        self.orderController = OrderController()

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

    def startOrder(self, username):
        self.orderController.startOrder(username)

    def addMeal(self, meal, quantity=1):
        self.orderController.addMeal(meal, quantity)

    def showBasket(self):
        self.orderController.showBasket()

    def canCheckout(self) -> bool:
        return self.orderController.canCheckout()

    def needMoreDishes(self):
        self.orderController.needMoreDishes()

    def showSummary(self):
        self.orderController.showSummary()

    def saveOrder(self):
        return self.orderController.saveOrder()

    def abandonOrder(self):
        self.orderController.abandonOrder()

    def showOrderHistory(self, username):
        self.orderController.showHistory(username)
