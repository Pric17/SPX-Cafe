from subsystems.menuSystem.menuFacade import MenuFacade

class Cafe:
    def __init__(self, name):
        self.name = name
        self.menuSystem = MenuFacade()

    def start(self):
        print(f"Welcome to {self.name}")
        choice = input("View Menu? (y/n): ").lower()
        if choice == 'y':
            self.menuSystem.showMenu()

            