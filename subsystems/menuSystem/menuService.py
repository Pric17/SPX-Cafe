from subsystems.menuSystem.repositories.menuRepository import MenuRepository
from subsystems.menuSystem.repositories.courseRepository import CourseRepository
from subsystems.menuSystem.repositories.mealRepository import MealRepository
from subsystems.menuSystem.models.menuModel import Menu

class MenuService:

    def __init__(self):
        self.menuRepo = MenuRepository()
        self.courseRepo = CourseRepository()
        self.mealRepo = MealRepository()

    def getMenuList(self):
        return self.menuRepo.getAllMenus()

    def getCourses(self, menu):
        return self.courseRepo.getCoursesByMenu(menu)

    def getMeals(self, course):
        return self.mealRepo.getMealsByCourse(course)


    def getMenuData(self, menu: Menu=None) -> list:
        fullStructure = []

        if menu:
           menus = [menu]
        else:
            menus = self.menuRepo.getAllMenus()
        
        for m in menus:
            courseData = []
            courses = self.courseRepo.getCoursesByMenu(m)
            for c in courses:
                meals = self.mealRepo.getMealsByCourse(c)
                courseData.append({"course": c, "meals": meals})
            fullStructure.append({"menu": m, "content": courseData})
            
        return fullStructure

