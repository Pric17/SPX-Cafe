from subsystems.customerSystem.models.orderItemModel import OrderItem

class Order:
    def __init__(self, username=None):
        self._username = username
        self._items = []
        self._orderId = None
        self._orderDate = None

    @property
    def username(self): return self._username
    @property
    def items(self): return self._items
    @property
    def orderId(self): return self._orderId
    @property
    def orderDate(self): return self._orderDate

    @property
    def distinctCount(self): return len(self._items)

    @property
    def total(self): return sum(item.subtotal for item in self._items)

    def addMeal(self, meal, quantity=1):
        for item in self._items:
            if item.meal.mealId == meal.mealId:
                item.addServings(quantity)
                return
        self._items.append(OrderItem(meal, quantity, meal.mealPrice))

    def setSaved(self, orderId, orderDate):
        self._orderId = orderId
        self._orderDate = orderDate
