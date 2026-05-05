class Menu:
    def __init__(self, menuId=None, menuName=None):
        self._menuId = menuId
        self._menuName = menuName

    @property
    def menuId(self): return self._menuId
    @property
    def menuName(self): return self._menuName




        