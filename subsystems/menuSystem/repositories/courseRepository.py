from core.databaseUtility import Database
from subsystems.menuSystem.models.courseModel import Course

class CourseRepository:

    def getCoursesByMenu(self, menu):
        sql = "SELECT courseId, courseName FROM courses WHERE menuId = ?"
        rows = Database.dbGet(sql, (menu.menuId,))
        return [Course(row[0], row[1], menu) for row in rows]