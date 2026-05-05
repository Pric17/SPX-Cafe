class Meal:
    def __init__(self, mealId=None, mealName=None, mealPrice=0.0, course=None):
        self._mealId = mealId
        self._mealName = mealName
        self._mealPrice = mealPrice
        self._course = course # Reference to Course object

    @property
    def mealId(self): return self._mealId
    @property
    def mealName(self): return self._mealName
    @property
    def mealPrice(self): return self._mealPrice
    
