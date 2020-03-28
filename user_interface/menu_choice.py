class MenuChoice:
    """Class that depict a menu choice define by un object and the next state 
        if a choice is made
        Attributes:
            item(object): object which owns an __str__ method for the display
            next (function): function or method implementing the next menu
    """

    history = {}   # histories of the choices which were maked

    def __init__(self, item, next_state, menu):
        self.item = item
        self.next = next_state
        self.menu = menu

    def __str__(self):
        """Format the choice for its display in the menu"""
        return str(self.item)

    def __call__(self):
        """Put the choice in the history's list and performs the next state"""
        self.history[self.menu.name] = self.item
        return self.next(self, self.history)
