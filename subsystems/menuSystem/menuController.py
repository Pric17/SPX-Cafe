from subsystems.menuSystem.menuService import MenuService
from subsystems.menuSystem.views.menuView import MenuView
from subsystems.menuSystem.models.menuModel import Menu
from core.utilities.choice import Choice

class MenuController:
    def __init__(self):
        self.service = MenuService()
        self.view = MenuView()

    def displayMenuList(self):
        data = self.service.getMenuList()
        if not data:
            self.view.displayMsg("There are no menues.")
        else:
            self.view.showMenuList(data)

    def displayMenu(self,menu:Menu=None):
        data = self.service.getMenuData(menu)
        if not data:
            self.view.displayMsg("The menun is empty.")
        else:
            self.view.showMenu(data)

    def findMenu(self, menuRequest:str=None) -> Menu:

        if menuRequest:
            menus = self.service.getMenuList()
            for menu in menus:
                if Choice.match(menuRequest, menu.menuName):
                    return menu
        return None

            