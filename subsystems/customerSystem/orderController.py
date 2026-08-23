from subsystems.customerSystem.orderService import OrderService, MIN_DISTINCT_DISHES
from subsystems.customerSystem.views.orderView import OrderView

class OrderController:
    def __init__(self):
        self.service = OrderService()
        self.view = OrderView()

    def startOrder(self, username):
        self.service.startOrder(username)

    def addMeal(self, meal, quantity=1):
        self.service.addMeal(meal, quantity)
        self.view.mealAdded(meal, quantity)

    def showBasket(self):
        self.view.showBasket(self.service.getBasket())

    def canCheckout(self) -> bool:
        return self.service.canCheckout()

    def needMoreDishes(self):
        self.view.needMoreDishes(MIN_DISTINCT_DISHES, self.service.distinctCount())

    def showSummary(self):
        self.view.showSummary(self.service.getBasket())

    def saveOrder(self):
        orderId = self.service.saveCurrentOrder()
        total = self.service.getBasket().total
        self.view.orderSaved(orderId, total)
        return orderId

    def abandonOrder(self):
        self.service.abandonOrder()

    def showHistory(self, username):
        history = self.service.getOrderHistory(username)
        self.view.showHistory(history)
