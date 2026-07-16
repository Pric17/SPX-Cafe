from subsystems.menuSystem.menuController import MenuController
from subsystems.menuSystem.models.menuModel import Menu
class MenuFacade:
    def __init__(self):
        self.controller = MenuController()

    def showMenu(self, menu=None):
            self.controller.displayMenu(menu)
    
    def showMenuList(self):
        self.controller.displayMenuList()
        
    def findMenu(self, menuRequest=None) -> Menu:
         
         menu = self.controller.findMenu(menuRequest)
         return menu
         
         


   