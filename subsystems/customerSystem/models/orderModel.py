from subsystems.customerSystem.models.orderItemModel import OrderItem

class Order:
    def __init__(self, username=None):
        self._username = username
        self._items = []          # list of OrderItem (the basket)
        self._orderId = None      # set when saved to the database
        self._orderDate = None    # set when saved

    @property
    def username(self): return self._username
    @property
    def items(self): return self._items
    @property
    def orderId(self): return self._orderId
    @property
    def orderDate(self): return self._orderDate

    # Number of DIFFERENT dishes (used for the 3-dish minimum rule)
    @property
    def distinctCount(self): return len(self._items)

    # Total cost of the whole order
    @property
    def total(self): return sum(item.subtotal for item in self._items)

    def addMeal(self, meal, quantity=1):
        # If this meal is already in the basket, just add servings to it;
        # otherwise add a new line item. This keeps "distinct dishes" accurate.
        for item in self._items:
            if item.meal.mealId == meal.mealId:
                item.addServings(quantity)
                return
        self._items.append(OrderItem(meal, quantity, meal.mealPrice))

    # Called by the repository/service at save time
    def setSaved(self, orderId, orderDate):
        self._orderId = orderId
        self._orderDate = orderDate
