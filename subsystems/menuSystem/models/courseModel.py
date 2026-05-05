from subsystems.menuSystem.models.menuModel import Menu

class Course:
    '''
    Course class

    Holds information about the courses that our Cafe will offer
    '''

    def __init__(self, courseId=None, courseName=None, menu:Menu=None):
        self._courseId = courseId
        self._courseName = courseName
        self._menu = menu

    @property
    def courseId(self):
        return self._courseId
    
    @courseId.setter
    def courseId(self, value):
        self._courseId = value

    @property
    def courseName(self):
        return self._courseName.title()

    @courseName.setter
    def courseName(self, value):
        self._courseName = value

    @property
    def menu(self) -> Menu:
        return self._menu
    
    @menu.setter
    def menu(self, value):
        # This allows you to replace the entire Menu object if needed
        self._menu = value

   
    
    