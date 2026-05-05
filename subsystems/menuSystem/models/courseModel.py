class Course:
    def __init__(self, courseId=None, courseName=None, menu=None):
        self._courseId = courseId
        self._courseName = courseName
        self._menu = menu # Reference to Menu object

    @property
    def courseId(self): return self._courseId
    @property
    def courseName(self): return self._courseName
   
    
    