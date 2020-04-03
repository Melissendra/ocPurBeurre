from .menu_choice import MenuChoice


class Menu:
    """
        Class for showing one or several choices to the user
        title(str): title to display up to the menu
        choices(dict): dictionary having the choices options for the user
    """

    def __init__(self, name, title):
        """ Initialization of the class Menu """
        self.name = name
        self.title = title
        self.choices = {}

    def add(self, key, choice, next):
        """
            We add new option for the user
            key(str) key that allow the user to choose his option
            choice(object): option to offer to the user
            next(function): method to execute if the choice is made by the user
        """
        key = key.lower().strip()
        if key:
            self.choices[key] = MenuChoice(choice, next_state=next, menu=self)
        return self

    def __str__(self):
        """ Format the menu for its display to the user """
        lines = [f"{self.title}", ""]
        for key, value in self.choices.items():
            lines.append(f"{key}. {value}")
        lines.append("")
        lines.append(">>> ")
        return "\n".join(lines)

    def render(self):
        """
            Displays the menu to the user and waits an answer
            The menu is display again until the user doesn't make a valid 
            choice
        """

        while True:
            answer = input(self).lower().strip()
            if answer in self.choices:
                return self.choices[answer]
