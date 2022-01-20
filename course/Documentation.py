
### ERROR #1 (logic)

# In this first error I mixed up my first argument, which is the type of function with "pygame.K_DOWN" which is a constant value for the down arrow.
# this caused the program to error silently, the erroneous code is as follows:

window.registerEvent(Event(pygame.K_DOWN, lambda:
    print("Event executed")
).attach())

# The Event class:

class Event():
    """This is used to create an event that can be added to the window.    

    Args:
        event: The event to be added to the window. e.g. pygame.KEYDOWN
        callback (Callable): The code that is executed when the event is executed.
        key (optional): If the event involves a key, you can specify the key here.
    """

    def __init__(self, event, callback, key=None):
        self.type = event
        if key:
            self.key = key
        self.callback = callback
        self.enabled = False
        
    def execute(self):
        self.callback()
            
    def isEnabled(self):
        return self.enabled
    
    def attach(self, enabled=True):
        self.enabled = enabled
        return self

# The registerEvent method on Window:

def registerEvent(self, handler):
    """This adds a handler to the window
    Args:
        handler (Event): The event handler to register
    """
    self.events.append(handler)

# I fixed my code, by replaceing the first parameter of Event()
# to "pygame.KEYDOWN" which is the event that we need to listen for when it is raised.
# After this, i added another parameter to specify which key we want to listen for when the event is raised.
# This fixed the error, and the event worked as expected and outputed "Event Executed" as expected.

window.registerEvent(Event(pygame.KEYDOWN, lambda:
    print("Event executed"), pygame.K_DOWN
).attach())