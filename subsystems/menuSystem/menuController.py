from subsystems.menuSystem.menuService import MenuService
from subsystems.menuSystem.views.menuView import MenuView

class MenuController:
    def __init__(self):
        self.service = MenuService()
        self.view = MenuView()

    def displayMenu(self):
        data = self.service.getFullMenuData()
        if not data:
            self.view.displayMsg("No menu data found.")
        else:
            self.view.showMenu(data)