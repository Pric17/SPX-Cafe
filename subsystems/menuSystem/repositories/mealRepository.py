from core.databaseUtility import Database
from subsystems.menuSystem.models.mealModel import Meal

class MealRepository:

    def getMealsByCourse(self, course):
        sql = "SELECT mealId, mealName, mealPrice FROM meals WHERE courseId = ?"
        rows = Database.dbGet(sql, (course.courseId,))
        return [Meal(row[0], row[1], row[2], course) for row in rows]