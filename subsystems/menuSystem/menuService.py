from subsystems.menuSystem.repositories.menuRepository import MenuRepository
from subsystems.menuSystem.repositories.courseRepository import CourseRepository
from subsystems.menuSystem.repositories.mealRepository import MealRepository

class MenuService:

    def __init__(self):
        self.menuRepo = MenuRepository()
        self.courseRepo = CourseRepository()
        self.mealRepo = MealRepository()

    def getMenuData(self, menu):
        fullStructure = []

        if menu:
            courseData = []
            courses = self.courseRepo.getCoursesByMenu(menu)
            for c in courses:
                meals = self.mealRepo.getMealsByCourse(c)
                courseData.append({"course": c, "meals": meals})
            fullStructure.append({"menu": menu, "content": courseData})
        return fullStructure

    def getFullMenuData(self):
        fullStructure = []
        menus = self.menuRepo.getAllMenus()

        for m in menus:
            courseData = []
            courses = self.courseRepo.getCoursesByMenu(m)
            for c in courses:
                meals = self.mealRepo.getMealsByCourse(c)
                courseData.append({"course": c, "meals": meals})
            fullStructure.append({"menu": m, "content": courseData})
        return fullStructure
    