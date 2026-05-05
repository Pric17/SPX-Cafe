class MenuView:
    def showMenu(self, allData):
        for entry in allData:
            menuObj = entry["menu"]
            print(f"\n{'='*12} {menuObj.menuName.upper()} {'='*12}")
            for section in entry["content"]:
                courseObj = section["course"]
                mealList = section["meals"]
                print(f"\n  >> {courseObj.courseName}")
                for meal in mealList:
                    print(f"     * {meal.mealName:<18} ${meal.mealPrice:6.2f}")

    def displayMsg(self, msg):
        print(f"\n[System]: {msg}")