class Customer:
    def __init__(self, username=None, password=None, firstName=None, lastName=None):
        self._username = username
        self._password = password
        self._firstName = firstName
        self._lastName = lastName

    @property
    def username(self): return self._username
    @property
    def password(self): return self._password
    @property
    def firstName(self): return self._firstName
    @property
    def lastName(self): return self._lastName

    @property
    def fullName(self): return f"{self._firstName} {self._lastName}"
