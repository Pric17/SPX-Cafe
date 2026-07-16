from datetime import datetime
from subsystems.customerSystem.repositories.orderRepository import OrderRepository
from subsystems.customerSystem.models.orderModel import Order

# Minimum number of different dishes required before an order can be checked out
MIN_DISTINCT_DISHES = 3

class OrderService:

    def __init__(self):
        self.orderRepo = OrderRepository()
        self.currentOrder = None  # the basket being built this session

    def startOrder(self, username):
        self.currentOrder = Order(username)

    def addMeal(self, meal, quantity=1):
        self.currentOrder.addMeal(meal, quantity)

    def getBasket(self):
        return self.currentOrder

    def distinctCount(self):
        return self.currentOrder.distinctCount

    def orderTotal(self):
        return self.currentOrder.total

    def canCheckout(self):
        return self.currentOrder.distinctCount >= MIN_DISTINCT_DISHES

    def saveCurrentOrder(self):
        # Stamp the date, persist, and record the generated orderId on the model
        orderDate = datetime.now().strftime("%Y-%m-%d")
        self.currentOrder.setSaved(None, orderDate)
        orderId = self.orderRepo.saveOrder(self.currentOrder)
        self.currentOrder.setSaved(orderId, orderDate)
        return orderId

    def abandonOrder(self):
        self.currentOrder = None
