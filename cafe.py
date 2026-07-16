from subsystems.menuSystem.menuFacade import MenuFacade
from subsystems.customerSystem.customerFacade import CustomerFacade
from core.utilities.options import MainOptions, OrderOptions
from core.utilities.choice import Choice

class Cafe:
    def __init__(self, name):
        self.name = name
        self.menuSystem = MenuFacade()
        self.customerSystem = CustomerFacade()
        self.customer = None # the logged-in Customer for this session
        self.__state = 1

    def start(self):
        while True:
            match self.__state:
                case 1: # Identify customer (login is mandatory before the main menu)
                    print(f"Welcome to {self.name}!")
                    username = self.__askNonBlank("Please enter your username: ")
                    customer = self.customerSystem.findCustomer(username)

                    if customer: # existing customer -> ask for password
                        while True:
                            password = input("Please enter your password: ")
                            # Allow giving up on login before checking the password
                            if password.lower() in ("exit", "quit", "leave"):
                                self.__state = 9
                                break
                            if self.customerSystem.verifyPassword(customer, password):
                                self.customer = customer
                                self.customerSystem.welcomeBack(customer)
                                self.__state = 2
                                break
                            # Wrong password: tell them and re-ask
                            self.customerSystem.wrongPassword()
                    else: # new customer -> register them
                        self.customerSystem.askNewCustomer(username)
                        password = self.__askNonBlank("Choose a password: ")
                        firstName = self.__askNonBlank("Enter your first name: ")
                        lastName = self.__askNonBlank("Enter your last name: ")
                        self.customer = self.customerSystem.register(username, password, firstName, lastName)
                        self.customerSystem.welcomeNew(self.customer)
                        self.__state = 2

                case 2: # main menu
                    # Ask using the prompts defined in MainOptions (data-driven)
                    ans = input(f"What would you like to do? ({MainOptions.getPrompts()}): ")

                    # checkChoice returns (matched option, message, next state)
                    (option, message, state) = MainOptions.checkChoice(ans)

                    if state:
                        if message: # some options leave the message to their state (e.g. exit)
                            print(message)
                        self.__state = state
                    else:
                        # Fuzzy match found nothing confident enough
                        print("Sorry, I didn't understand that. Please try again.")

                case 3: # Show Menu
                    self.menuSystem.showMenuList()
                    menuRequest = input("Enter which menu to show or blank for all? ")
                    menu = self.menuSystem.findMenu(menuRequest)
                    self.menuSystem.showMenu(menu)
                    self.__state = 2

                case 4: # View previous orders (to be built in a later step)
                    print("(Order history is not available yet.)")
                    self.__state = 2

                case 5: # Start a new order
                    self.customerSystem.startOrder(self.customer.username)
                    print("\nLet's build your order. You'll need at least 3 different dishes.")
                    self.__state = 50

                case 50: # Ordering menu loop
                    ans = input(f"\nOrdering - what next? ({OrderOptions.getPrompts()}): ")
                    (option, message, state) = OrderOptions.checkChoice(ans)
                    if state:
                        if message:
                            print(message)
                        self.__state = state
                    else:
                        print("Sorry, I didn't understand that. Please try again.")

                case 51: # View the menu while ordering
                    self.menuSystem.showMenuList()
                    menuRequest = input("Enter which menu to show or blank for all? ")
                    menu = self.menuSystem.findMenu(menuRequest)
                    self.menuSystem.showMenu(menu)
                    self.__state = 50

                case 52: # Finish / checkout
                    if not self.customerSystem.canCheckout():
                        self.customerSystem.needMoreDishes()
                        self.__state = 50
                    else:
                        self.customerSystem.showSummary()
                        confirm = input("\nConfirm and place this order? (yes/no): ")
                        if Choice.match(confirm, "yes"):
                            self.customerSystem.saveOrder()
                            self.__state = 2
                        else:
                            print("Okay, your order is still open.")
                            self.__state = 50

                case 53: # Add a meal (navigate menu -> course -> dish)
                    self.menuSystem.showMenuList()
                    menu = self.menuSystem.findMenu(input("Which menu? "))
                    if not menu:
                        print("Sorry, I couldn't find that menu.")
                        self.__state = 50
                    else:
                        self.menuSystem.showCourses(menu)
                        course = self.menuSystem.findCourse(menu, input("Which course? "))
                        if not course:
                            print("Sorry, I couldn't find that course.")
                            self.__state = 50
                        else:
                            self.menuSystem.showMeals(course)
                            meal = self.menuSystem.findMeal(course, input("Which dish? "))
                            if not meal:
                                print("Sorry, I couldn't find that dish.")
                                self.__state = 50
                            else:
                                quantity = self.__askQuantity()
                                self.customerSystem.addMeal(meal, quantity)
                                self.__state = 50

                case 54: # View basket
                    self.customerSystem.showBasket()
                    self.__state = 50

                case 55: # Abandon order
                    confirm = input("\nAre you sure you want to abandon this order? (yes/no): ")
                    if Choice.match(confirm, "yes"):
                        self.customerSystem.abandonOrder()
                        print("Your order has been abandoned.")
                        self.__state = 2
                    else:
                        self.__state = 50

                case 9: # Exit
                    if self.customer: # thank the customer by name (assessment requirement)
                        print(f"Thank you, {self.customer.firstName}! Come back soon.")
                    else:
                        print("Thank you for using Babciabot, see you next time!")
                    break

    def __askNonBlank(self, prompt):
        # Keep asking until the user types something that isn't blank/whitespace
        while True:
            answer = input(prompt).strip()
            if answer:
                return answer
            print("That can't be blank. Please try again.")

    def __askQuantity(self):
        # Keep asking until we get a positive whole number of servings
        while True:
            answer = input("How many servings? ").strip()
            if answer.isdigit() and int(answer) > 0:
                return int(answer)
            print("Please enter a whole number greater than 0.")
