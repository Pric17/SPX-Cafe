from subsystems.menuSystem.menuFacade import MenuFacade
from subsystems.customerSystem.customerFacade import CustomerFacade
from core.utilities.options import MainOptions

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
                    username = input("Please enter your username: ")
                    customer = self.customerSystem.findCustomer(username)

                    if customer: # existing customer -> ask for password
                        while True:
                            password = input("Please enter your password: ")
                            if self.customerSystem.verifyPassword(customer, password):
                                self.customer = customer
                                self.customerSystem.welcomeBack(customer)
                                self.__state = 2
                                break
                            # Allow giving up on login before re-prompting
                            if password.lower() in ("exit", "quit", "leave"):
                                self.__state = 9
                                break
                            # Wrong password: tell them and re-ask
                            self.customerSystem.wrongPassword()
                    else: # new customer -> register them
                        self.customerSystem.askNewCustomer(username)
                        password = input("Choose a password: ")
                        firstName = input("Enter your first name: ")
                        lastName = input("Enter your last name: ")
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

                case 5: # Order food (to be built in a later step)
                    print("(Ordering is not available yet.)")
                    self.__state = 2

                case 9: # Exit
                    if self.customer: # thank the customer by name (assessment requirement)
                        print(f"Thank you, {self.customer.firstName}! Come back soon.")
                    else:
                        print("Thank you for using Babciabot, see you next time!")
                    break
