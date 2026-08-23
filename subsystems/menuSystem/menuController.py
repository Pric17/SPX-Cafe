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

    def getCourses(self, menu):
        return self.service.getCourses(menu)

    def showCourses(self, menu):
        courses = self.service.getCourses(menu)
        if not courses:
            self.view.displayMsg("There are no courses on this menu.")
        else:
            self.view.showCourseList(courses)

    def findCourse(self, menu, request:str=None):
        if request:
            courses = self.service.getCourses(menu)
            for course in courses:
                if Choice.match(request, course.courseName):
                    return course
        return None

    def showMeals(self, course):
        meals = self.service.getMeals(course)
        if not meals:
            self.view.displayMsg("There are no dishes in this course.")
        else:
            self.view.showMealList(meals)

    def findMeal(self, course, request:str=None):
        if request:
            meals = self.service.getMeals(course)
            for meal in meals:
                if Choice.match(request, meal.mealName):
                    return meal
        return None

            