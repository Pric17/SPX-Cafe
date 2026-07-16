class MenuView:

    def showMenuList(self, allData):
        print("This is a list of Menus:")
        for menu in allData:
            print(f"({menu.menuId}) {menu.menuName}")


    def showMenu(self, allData):
        for entry in allData:
            menuObj = entry["menu"]
            print(f"\n{'='*10} {menuObj.menuName.upper()} {'='*12}")
            for section in entry["content"]:
                courseObj = section["course"]
                mealList = section["meals"]

                print(f"\n  >> {courseObj.courseName}")

                if not mealList:
                   print(" No item available.")
                else:
                    for meal in mealList:
                        print(f" * {meal.mealName:<18} ${meal.mealPrice:6.2f}")


    def displayMsg(self, msg):
        print(f"\n[System]: {msg}")

    