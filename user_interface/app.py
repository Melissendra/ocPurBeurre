from .stateMachine import StateMachine
from .menu import Menu
from database.category import Category
from database.substitutes import Substitute
import records
import constants as c
import logging

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

db = records.Database()


class App(StateMachine):
    """Class for the creation of a succession of menus"""

    def handle_start(self, entry=None, history=[]):
        logger.debug("entry vaut %s", entry)
        return(
            Menu("Accueil")
            .add("1", "Quel aliment souhaitez-vous remplacer?",
                 self.handle_category_option)
            .add("2", "Retrouver mes aliments substitués.",
                 self.handle_option2)
            .add("q", "Quitter", self.handle_quit)
            .render()
        )

    # def handle_option1(self, entry, history):
    #     logger.debug("entry vaut %s", entry)
    #     return(
    #         Menu("Quel aliment remplacer?")
    #         .add("1", "Sélectionner la catégorie", self.handle_category_option)
    #         .add("a", "Accueil", self.handle_start)
    #         .add("q", "Quitter", self.handle_quit)
    #         .render()
    #     )

    def handle_category_option(self, entry, history):
        logger.debug("entry vaut %s", entry)
        cat_menu = Menu("Catégories")
        for i, category in enumerate(c.CATEGORIES_LIST):
            cat_menu.add(f"{i+1}", f"{category}",
                         self.show_products_by_category)
        cat_menu.add("a", "Retour", self.handle_start).add("q", "Quitter", self.handle_quit)
        return cat_menu.render()

    def show_products_by_category(self, entry, history):
        logger.debug("entry vaut %s", entry)
        cat = Category(db, f"{entry}")
        rows = cat.get_product_by_category()
        products_menu = Menu(f"{entry} >>> Veuillez choisir le produit que vous souhaitez substituer ")
        for n, r in enumerate(rows):
            product_name = r.name
            # product_link = r.link
            nutriscore = r.nutriscore_letter
            products_menu.add(f"{n+1}", f"{product_name}, {nutriscore}", self.handle_product_substitutes)
        products_menu.add("a", "Retour à l'acceuil", self.handle_start)\
            .add("q", "Quitter", self.handle_quit)
        return products_menu.render()

    def handle_product_substitutes(self, entry, history):
        logger.debug("entry vaut %s", entry)
        entry = history[-2]
        prod_substitute = Substitute(db, f"{entry}")
        rows = prod_substitute.get_substitute()
        substitute_menu = Menu(f"Produits ayant un meilleur nutriscore que {entry}")
        for n, r in enumerate(rows):
            product_name = r.name
            nutriscore = r.nutriscore_letter
            substitute_menu.add(f"{n+1}", f"{product_name}, {nutriscore}", self.save_product)
        substitute_menu.add("a", "Retour à l'accueil", self.handle_start)\
            .add("q", "Quitter", self.handle_quit)
        return substitute_menu.render()

    def save_product(self, entry, history):
        pass

    def handle_option2(self, entry, history):
        Menu("Produits substitués").add("1", "Revenir à l'accueil", self.handle_start).add("2", "Quitter", self.handle_quit)

    def handle_quit(self, entry, history):
        print("Au revoir")
        self.running = False
