from subsystems.menuSystem.menuFacade import MenuFacade
from core.utilities.choice import Choice

class Cafe:
    def __init__(self, cafeName):
        self.name = cafeName
        self.menuSystem = MenuFacade()
        self.__state = 1
        self.__menuOptions = ["View Menu", "Exit"]

    def start(self):
        while True:
            match self.__state:
                case 1: # Get customer
                    print(f"Welcome to {self.cafeName}!")
                    self.__state = 2
                case 2: # main menu
                    ans = input(f"Choose a Menu Option:[{', '.join(self.__menuOptions)}]: "). lower()

                    option = Choice.getChoice(ans, self.__menuOptions)
                    match option:
                        case "View Menu":
                            self.__state = 3
                        case "Exit":
                            self.__state = 9

                case 3: # Show Menu
                    self.menuSystem.showMenuList()
                    menuRequest = input("Enter which menu to show or blank for all? ")
                    menu = self.menuSystem.findMenu(menuRequest)
                    self.menuSystem.showMenu(menu)
                    self.__state = 2

                case 9: # Exit
                    print("Thank you for visiting! Goodbye!")
                    break