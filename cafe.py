from subsystems.menuSystem.menuFacade import MenuFacade
from subsystems.customerSystem.customerFacade import CustomerFacade
from core.utilities.options import MainOptions, OrderOptions
from core.utilities.choice import Choice
from core.utilities.voice import Voice

class Cafe:
    def __init__(self, name):
        self.name = name
        self.menuSystem = MenuFacade()
        self.customerSystem = CustomerFacade()
        self.customer = None
        self.voice = None
        self.__state = 1

    def start(self):
        choice = input("Enable voice interaction? (yes/no): ")
        self.voice = Voice(enabled=Choice.match(choice, "yes"))

        while True:
            match self.__state:
                case 1: # Get customer
                    print(f"Welcome to {self.name}!")
                    username = self.__askNonBlank("Please enter your username: ")
                    customer = self.customerSystem.findCustomer(username)

                    if customer:
                        while True:
                            password = input("Please enter your password: ")
                            if password.lower() in ("exit", "quit", "leave"):
                                self.__state = 9
                                break
                            if self.customerSystem.verifyPassword(customer, password):
                                self.customer = customer
                                self.customerSystem.welcomeBack(customer)
                                self.__state = 2
                                break
                            self.customerSystem.wrongPassword()
                    else:
                        self.customerSystem.askNewCustomer(username)
                        password = self.__askNonBlank("Choose a password: ")
                        firstName = self.__askNonBlank("Enter your first name: ")
                        lastName = self.__askNonBlank("Enter your last name: ")
                        self.customer = self.customerSystem.register(username, password, firstName, lastName)
                        self.customerSystem.welcomeNew(self.customer)
                        self.__state = 2

                case 2: # main menu
                    ans = self.voice.listen(f"What would you like to do? ({MainOptions.getPrompts()}): ")

                    (option, message, state) = MainOptions.checkChoice(ans)

                    if state:
                        if message:
                            print(message)
                        self.__state = state
                    else:
                        print("Sorry, I didn't understand that. Please try again.")

                case 3: # Show Menu
                    self.menuSystem.showMenuList()
                    menuRequest = self.voice.listen("Enter which menu to show or blank for all? ")
                    menu = self.menuSystem.findMenu(menuRequest)
                    self.menuSystem.showMenu(menu)
                    self.__state = 2

                case 4:
                    self.customerSystem.showOrderHistory(self.customer.username)
                    self.__state = 2

                case 5:
                    self.customerSystem.startOrder(self.customer.username)
                    print("\nLet's build your order. You'll need at least 3 different dishes.")
                    self.__state = 50

                case 50:
                    ans = self.voice.listen(f"\nOrdering - what next? ({OrderOptions.getPrompts()}): ")
                    (option, message, state) = OrderOptions.checkChoice(ans)
                    if state:
                        if message:
                            print(message)
                        self.__state = state
                    else:
                        print("Sorry, I didn't understand that. Please try again.")

                case 51:
                    self.menuSystem.showMenuList()
                    menuRequest = self.voice.listen("Enter which menu to show or blank for all? ")
                    menu = self.menuSystem.findMenu(menuRequest)
                    self.menuSystem.showMenu(menu)
                    self.__state = 50

                case 52:
                    if not self.customerSystem.canCheckout():
                        self.customerSystem.needMoreDishes()
                        self.__state = 50
                    else:
                        self.customerSystem.showSummary()
                        confirm = self.voice.listen("\nConfirm and place this order? (yes/no): ")
                        if Choice.match(confirm, "yes"):
                            self.customerSystem.saveOrder()
                            self.__state = 2
                        else:
                            print("Okay, your order is still open.")
                            self.__state = 50

                case 53:
                    self.menuSystem.showMenuList()
                    menu = self.menuSystem.findMenu(self.voice.listen("Which menu? "))
                    if not menu:
                        print("Sorry, I couldn't find that menu.")
                        self.__state = 50
                    else:
                        courses = self.menuSystem.getCourses(menu)
                        if len(courses) == 1:
                            course = courses[0]
                        else:
                            self.menuSystem.showCourses(menu)
                            course = self.menuSystem.findCourse(menu, self.voice.listen("Which course? "))
                        if not course:
                            print("Sorry, I couldn't find that course.")
                            self.__state = 50
                        else:
                            self.menuSystem.showMeals(course)
                            meal = self.menuSystem.findMeal(course, self.voice.listen("Which dish? "))
                            if not meal:
                                print("Sorry, I couldn't find that dish.")
                                self.__state = 50
                            else:
                                quantity = self.__askQuantity()
                                self.customerSystem.addMeal(meal, quantity)
                                self.__state = 50

                case 54:
                    self.customerSystem.showBasket()
                    self.__state = 50

                case 55:
                    confirm = self.voice.listen("\nAre you sure you want to abandon this order? (yes/no): ")
                    if Choice.match(confirm, "yes"):
                        self.customerSystem.abandonOrder()
                        print("Your order has been abandoned.")
                        self.__state = 2
                    else:
                        self.__state = 50

                case 9: # Exit
                    if self.customer:
                        print(f"Thank you, {self.customer.firstName}! Come back soon.")
                    else:
                        print("Thank you for using Babciabot, see you next time!")
                    break

    def __askNonBlank(self, prompt):
        while True:
            answer = input(prompt).strip()
            if answer:
                return answer
            print("That can't be blank. Please try again.")

    def __askQuantity(self):
        while True:
            answer = self.voice.listen("How many servings? ")
            if answer.isdigit() and int(answer) > 0:
                return int(answer)
            print("Please enter a whole number greater than 0.")
