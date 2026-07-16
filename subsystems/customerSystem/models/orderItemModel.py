class OrderItem:
    def __init__(self, meal=None, quantity=1, priceAtTime=0.0):
        self._meal = meal              # Reference to the Meal object ordered
        self._quantity = quantity
        self._priceAtTime = priceAtTime  # Price captured when added (frozen for this order)

    @property
    def meal(self): return self._meal
    @property
    def quantity(self): return self._quantity
    @property
    def priceAtTime(self): return self._priceAtTime

    # Line total for this item, e.g. 2 x soup @ 5.00 = 10.00
    @property
    def subtotal(self): return self._quantity * self._priceAtTime

    def addServings(self, extra):
        # Re-ordering the same meal just increases its quantity
        self._quantity += extra
