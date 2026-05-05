from core.databaseUtility import Database
from subsystems.menuSystem.models.menuModel import Menu

class MenuRepository:

    def getAllMenus(self):
        sql = "SELECT menuId, menuName FROM menus"
        rows = Database.dbGet(sql)
        return [Menu(row[0], row[1]) for row in rows]