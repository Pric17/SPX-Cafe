class CustomerView:

    def welcomeBack(self, customer):
        print(f"\nWelcome back, {customer.firstName}! Great to see you again.")

    def welcomeNew(self, customer):
        print(f"\nWelcome, {customer.firstName}! You're now registered with us.")

    def askNewCustomer(self, username):
        print(f"\nWe don't have an account for '{username}' yet. Let's set you up!")

    def wrongPassword(self):
        print("\nSorry, that password is incorrect. Please try again (or type 'exit' to leave).")

    def displayMsg(self, msg):
        print(f"\n[System]: {msg}")
