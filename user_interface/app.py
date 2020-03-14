from .stateMachine import StateMachine
from .menu import Menu
from database.category import Category
import records

db = records.Database()


class App(StateMachine):
    """Class for the creation of a succession of menus"""

    def handle_start(self):
        return(
            Menu("Accueil")
            .add("1", "Quel aliment souhaitez vous remplacer?",
                 self.handle_option1)
            .add("2", "Retrouver mes aliments substitués.",
                 self.handle_option2)
            .add("q", "Quitter", self.handle_quit)
            .render()
        )

    def handle_option1(self):
        return(
            Menu("Quel aliment remplacer?")
            .add("1", "Sélectionner la catégorie", self.handle_category_option)
            .add("3", "Accueil", self.handle_start)
            .add("q", "Quitter", self.handle_quit)
            .render()
        )

    def handle_category_option(self):
        return(
            Menu("Categories")
            .add("1", "Epicerie", self.handle_product)
            .add("2", "Pizza", self.handle_product)
            .add("3", "Produits laitiers", self.handle_product)
            .add("4", "Desserts", self.handle_product)
            .add("5", "Boisson", self.handle_product)
            .add("a", "Retour à l'accueil", self.handle_start)
            .add("q", "Quitter", self.handle_quit)
            .render()
        )

    def handle_product(self):
        cat = Category(db)
        products = cat.get_product_by_category("Epicerie")
        print(products)

    def handle_product_option(self):
        pass

    def handle_option2(self):
        Menu("Produits substitués").add("1", "Revenir à l'accueil", self.handle_start).add("2", "Quitter", self.handle_quit)

    def handle_quit(self):
        print("Au revoir")
        self.running = False


if __name__ == "__main__":

    app = App()
    app.start()
