class Menu:
    '''
    Menu class

    Holds information about that types of menus our Cafe will offer
    '''

    def __init__(self, menuId=None, menuName=None):
        self._menuId = menuId
        self._menuName = menuName

    @property
    def menuId(self):
        return self._menuId
    
    @menuId.setter
    def menuId(self, value):
        self._menuId = value

    @property
    def menuName(self):
        return self._menuName.title()

    @menuName.setter
    def menuName(self, value):
        self._menuName = value






        