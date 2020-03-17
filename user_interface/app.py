from .stateMachine import StateMachine
from .menu import Menu
from database.category import Category
import records
import constants as c

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
        cat_menu = Menu("Catégories")
        for i, category in enumerate(c.CATEGORIES_LIST):
            cat_menu.add(f"{i+1}", f"{category}", self.show_products_by_category)
        cat_menu.add("a", "Retour", self.handle_start).add("q", "Quitter", self.handle_quit)
        return cat_menu.render()

    def show_products_by_category(self):
        cat = Category(db, "Epicerie")
        rows = cat.get_product_by_category()
        products_menu = Menu("Epicerie >>> Produits ")
        for i, r in enumerate(rows):
            product_name = r.name
            product_link = r.link
            nutriscore = r.nutriscore_letter
            products_menu.add(f"{i+1}", f"{product_name}, {nutriscore}", self.handle_category_option)
        products_menu.add("a", "Retour à l'acceuil", self.handle_start)\
            .add("q", "Quitter", self.handle_quit)

        return products_menu.render

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
