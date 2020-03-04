from .stateMachine import AbstractStateMachine
from .menu import Menu
from .menu_choice import MenuChoice


class App(StateMachine):
    """Class for the creation of a succession of menus"""

    def handle_start(self):
        return(
            Menu("Accueil")
                .add("1", "Quel aliment souhaitez vous remplacer?", self.handle_option1)
                .add("2", "Retrouvé mes aliments substitués.", self.handle_option2)
                .add("q", "Quitter", self.handle_quit)
                .render()
        )

if __name__ == "__main__":
    app = App()
    app.start()