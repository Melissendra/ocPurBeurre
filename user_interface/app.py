from .stateMachine import StateMachine
from .menu import Menu
from database.manager import Manager
from database.product import Product
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
        cat = Manager(db, f"{entry}")
        rows = cat.get_product_by_category()
        products_menu = Menu(f"{entry} >>> Produits ayant un nutriscore de c à e. Pour plus d'infos sélectionnez le produit qui vous interesse.")
        for n, r in enumerate(rows):
            product_name = r.name
            # product_link = r.link
            # nutriscore = r.nutriscore_letter
            products_menu.add(f"{n+1}", f"{product_name}", self.show_description)
        products_menu.add("a", "Retour à l'acceuil", self.handle_start)\
            .add("q", "Quitter", self.handle_quit)
        return products_menu.render()

    def handle_product_substitutes(self, entry, history):
        logger.debug("entry vaut %s", entry)
        entry = history[-3]
        prod_substitute = Manager(db, f"{entry}")
        rows = prod_substitute.get_substitute()
        substitute_menu = Menu(f"Produits ayant un meilleur nutriscore que {entry}")
        for n, r in enumerate(rows):
            product_name = r.name
            nutriscore = r.nutriscore_letter
            link = r.link
            store = r.store_name
            substitute_menu.add(f"{n+1}", f"{product_name}", self.show_description)
        substitute_menu.add("a", "Retour à l'accueil", self.handle_start)\
            .add("q", "Quitter", self.handle_quit)
        return substitute_menu.render()

    def show_description(self, entry, history):
        prod_sub = Product(db, f"{entry}")
        rows = prod_sub.get_product_info()
        prod_menu = Menu(f"{entry}")
        for r in rows:
            prod_name = r.name
            prod_link = r.link
            prod_store = r.store_name
            prod_nutriscore = r.nutriscore_letter
            prod_menu.add("1", f"{prod_name}. {prod_link}. {prod_store}. {prod_nutriscore}", self.save_product)\
                .add("2", "Retour à la liste des produits", self.handle_product_substitutes)\
                .add("3", "Menu categorie", self.handle_category_option)
        prod_menu.add("a", "Accueil", self.handle_start).add("q", "Quitter", self.handle_quit)
        return prod_menu.render()

    def save_product(self, entry, history):
        pass
        # manager = Manager(db, f"{entry}")
        # origin_prod =
        # saver = manager.save_favorite()

    def handle_option2(self, entry, history):
        Menu("Produits substitués").add("1", "Revenir à l'accueil", self.handle_start).add("2", "Quitter", self.handle_quit)

    def handle_quit(self, entry, history):
        print("Au revoir")
        self.running = False
