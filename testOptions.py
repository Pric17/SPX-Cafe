from core.utilities.options import MainOptions, OrderOptions

answer = input(f"What is your choice ({MainOptions.getPrompts()}): ")

(choice, message, state) = MainOptions.checkChoice(answer)
# print(f"{message}.  You chose {choice}, the next state is {state}")

match state:

    case 5: # order food
        print(f"{message}")
        answer = input(f"Your Order food options are ({OrderOptions.getPrompts()}): ")
        (choice, message, state) = OrderOptions.checkChoice(answer)
        print(f"{message}.  You chose '{choice}', the next state is {state}")

    case _: # 
        print(f"{message}.  You chose '{choice}', the next state is {state}")