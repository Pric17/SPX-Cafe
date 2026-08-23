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

    def getCourses(self, menu):
        return self.controller.getCourses(menu)

    def showCourses(self, menu):
        self.controller.showCourses(menu)

    def findCourse(self, menu, request=None):
        return self.controller.findCourse(menu, request)

    def showMeals(self, course):
        self.controller.showMeals(course)

    def findMeal(self, course, request=None):
        return self.controller.findMeal(course, request)
         
         


   