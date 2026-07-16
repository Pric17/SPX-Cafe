from core.utilities.choice import Choice

class Options():
    '''
        Base Options to provide behaviour
    '''
    # Static Variables
    options  = {
        # Options, prompt, synonyms, Message, State

    }

    @classmethod
    def getPrompts(cls):
        return ', '.join([cls.options[o]["prompt"] for o in cls.options])

    @classmethod
    def checkChoice(cls, answer: str):
        option = None
        message = None
        state = None

        for o in cls.options:
            choice = Choice.getChoice(answer, cls.options[o]["syn"])
            # print(f"Check {o} in {cls.options[o]['syn']} - found {choice}")
            if choice:
                option = o
                message = cls.options[o]["message"]
                state = cls.options[o]["state"]
                # print(f"Found {choice} - message: {message} - next state: {state}")
                break
        return (option, message, state)
    
class MainOptions(Options):
    '''
        Main Options extends Base Options to provide prompts for main options
    '''
    options  = {
        # Options, prompt, synonyms, Message, State
        "menu": {
            "prompt"    : "View the Menu" # display
            , "syn"       : {"meals", "food", "menu"} # input synonyms
            , "message" : "Thank you for choosing to see the Menu" 
            ,"state"    : 3
        }
        , "history": {
            "prompt"    : "View Previous Orders" # display
            ,"syn"       : {"previous", "history", "past"} # input synonyms
            , "message" : "You wish to see your previous orders"
            ,"state"    : 4                
        }
        , "order": {
            "prompt"    : "Order Food" # display
            ,"syn"       : {"order", "add", "buy"} # input synonyms
            , "message" : "You wish to order food"
            ,"state"    : 5
        }
        , "exit": {
            "prompt"    : "Exit System" # display
            ,"syn"       : {"goodbye", "exit", "logout", "leave", "finish"}, # input synonyms
            "message": "Thank you for using Italiabot, see you next time"
            ,"state":  9
        }
    }

class OrderOptions(Options):
    '''
        Order food Options extends Base Options to provide prompts for Ordering Food options
    '''

    options  = {
        # Options, prompt, synonyms, Message, State
        "menu": {
            "prompt"    : "View the Menu" # display
            , "syn"       : {"course", "food", "menu"} # input synonyms
            , "message" : "Thank you for choosing to see the Menu" 
            ,"state"    : 51
        }
        , "finish": {
            "prompt"    : "Finish Orders" # display
            ,"syn"       : {"finish", "end", "complete"} # input synonyms
            , "message" : "You wish to finish your order"
            ,"state"    : 52
        }
        , "order": {
            "prompt"    : "Add a Meal" # display
            ,"syn"       : {"order", "add", "buy", "meal"} # input synonyms
            , "message" : "You wish to add a meal to your order"
            ,"state"    : 53
        }
    }
        
