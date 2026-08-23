class OrderItem:
    def __init__(self, meal=None, quantity=1, priceAtTime=0.0):
        self._meal = meal
        self._quantity = quantity
        self._priceAtTime = priceAtTime

    @property
    def meal(self): return self._meal
    @property
    def quantity(self): return self._quantity
    @property
    def priceAtTime(self): return self._priceAtTime

    @property
    def subtotal(self): return self._quantity * self._priceAtTime

    def addServings(self, extra):
        self._quantity += extra
