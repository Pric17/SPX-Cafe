from subsystems.menuSystem.menuController import MenuController


class MenuFacade:
    def __init__(self):
        self.controller = MenuController()

    def showMenu(self, menu=None):
        if menu:
            self.controller.displayMenu(menu)
        else:
            self.controller.displayAllMenus()



   