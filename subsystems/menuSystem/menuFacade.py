from subsystems.menuSystem.menuController import MenuController

class MenuFacade:
    def __init__(self):
        self.controller = MenuController()

    def showMenu(self):
        self.controller.displayMenu()