from subsystems.menuSystem.menuService import MenuService
from subsystems.menuSystem.views.menuView import MenuView

class MenuController:
    def __init__(self):
        self.service = MenuService()
        self.view = MenuView()

    def displayMenu(self, menu):
        data = self.service.getMenuData(menu)
        if not data:
            self.view.displayMsg("The menu is currently empty.")
        else:
            self.view.showMenu(data)




    def displayAllMenus(self):
        data = self.service.getFullMenuData()
        if not data:
            self.view.displayMsg("The menu is currently empty.")
        else:
            self.view.showAllMenus(data)
            