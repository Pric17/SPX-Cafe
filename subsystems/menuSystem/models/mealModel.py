from subsystems.menuSystem.models.courseModel import Course

class Meal:
    def __init__(self, mealId=None, mealName=None, course:Course=None):
        self._mealId = mealId
        self._mealName = mealName
        self._course = course

    @property
    def mealId(self):
        return self._mealId
    
    @mealId.setter
    def mealId(self, value):
        self._mealId = value

    @property
    def mealName(self):
        return self._mealName
    
    @mealName
    def mealName(self, value):
        self._mealName = value
    
    @property
    def course(self) -> Course:
        return self._course
    
    @course.setter
    def course(self, value: Course):
        self._course = value

    
