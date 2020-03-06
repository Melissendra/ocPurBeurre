from .stateMachine import StateMachine
from .menu import Menu


class App(StateMachine):
    """Class for the creation of a succession of menus"""

    def handle_start(self):
        return(
            Menu("Accueil")
            .add("1", "Quel aliment souhaitez vous remplacer?",
                 self.handle_option1)
            .add("2", "Retrouver mes aliments substitués.", self.handle_option2)
            .add("q", "Quitter", self.handle_quit)
            .render()
        )

    def handle_option1(self):
        return(
            Menu("Quel aliment remplacer?")
            .add("1", "Sélectionner la catégorie", self.handle_category_option)
            .add("2", "Sélectionner un aliment", self.handle_product_option)
            .add("3", "Accueil", self.handle_start)
            .add("q", "Quitter", self.handle_quit)
            .render()
        )

    def handle_category_option(self):
        return(
            Menu("Categories")
            .add("1", "Retour à l'accueil")
        )

    def handle_option2(self):
        Menu("Produits substitués").add("1", "Revenir à l'accueil", self.handle_start).add("2", "Quitter", self.handle_quit)

    def handle_quit(self):
        print("Au revoir")
        self.running = False


if __name__ == "__main__":
    app = App()
    app.start()
