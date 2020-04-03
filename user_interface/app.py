from .stateMachine import StateMachine
from .menu import Menu
from .product_model import ProductModel
from .product_description import ProductDescription
from database.product_by_cat import ProductByCategory
from database.substitute import Substitute
from database.product import Product
from database.favorite import Favorite
import records
import constants as c

db = records.Database()


class App(StateMachine):
    """Class for the creation of a succession of menus"""

    def handle_start(self, entry=None, history=None):
        """ Method to display the Welcome Menu and ask the first choices """
        return (
            Menu("Accueil", "Accueil")
                .add("1", "Quel aliment souhaitez-vous remplacer?",
                     self.handle_category_option)
                .add("2", "Retrouver mes aliments substitués.",
                     self.show_favorites)
                .add("q", "Quitter", self.handle_quit)
                .render()
        )

    def handle_category_option(self, entry, history):
        """ Method to display the categories' choices
            The user need to enter a number to enter the category's products
        """
        cat_menu = Menu("Categories", "Catégories")
        for i, category in enumerate(c.CATEGORIES_LIST):
            cat_menu.add(f"{i + 1}", f"{category}",
                         self.show_products_by_category)
        cat_menu.add("a", "Retour", self.handle_start).add("q", "Quitter", self.handle_quit)
        return cat_menu.render()

    def show_products_by_category(self, entry, history):
        """Method to display 20 randoms products within the chosen category with a nutriscore between c and e"""
        cat = ProductByCategory(db, entry.item)
        rows = cat.get_product_by_category()
        products_menu = Menu("Products", f"{entry} >>> Produits ayant un nutriscore de c à e.")
        for n, r in enumerate(rows):
            product = ProductModel(r.id, r.name, r.link, r.nutriscore_letter)
            products_menu.add(f"{n + 1}", product, self.handle_product_substitutes)
        products_menu.add("a", "Retour à l'acceuil", self.handle_start) \
            .add("q", "Quitter", self.handle_quit)
        return products_menu.render()

    def handle_product_substitutes(self, entry, history):
        """ Method to suggest healthier products to the user. Their nutriscore will be a or b"""
        category = history.get("Categories")
        product = history.get("Products")
        prod_substitute = Substitute(db, category)
        rows = prod_substitute.get_substitute()
        substitute_menu = Menu("Substitutes", f"Produits ayant un meilleur nutriscore que {product.name}"
                                              f"Pour plus d'infos sélectionnez le produit qui vous interesse "
                                              f"en tapant son chiffre.")
        for n, r in enumerate(rows):
            product = ProductModel(r.id, r.name, r.link, r.nutriscore_letter)
            substitute_menu.add(f"{n + 1}", product, self.show_description)
        substitute_menu.add("a", "Retour à l'accueil", self.handle_start) \
            .add("q", "Quitter", self.handle_quit)
        return substitute_menu.render()

    def show_description(self, entry, history):
        """
            Method to show all the information of the chosen product: name, link, store where the user can find it,
            and its nutriscore.
         """
        product = history.get("Substitutes")
        prod_sub = Product(db, product)
        rows = prod_sub.get_product_info()
        prod_menu = Menu("Description", f"{product.name}. Pour sauvegarder le produit, tapez 1")
        for r in rows:
            product_description = ProductDescription(r.id, r.name, r.link, r.store_name, r.nutriscore_letter)
            prod_menu.add("1", product_description, self.save_product) \
                .add("2", "Retour à la liste des produits", self.last_menu) \
                .add("3", "Menu categorie", self.handle_category_option)
        prod_menu.add("a", "Accueil", self.handle_start).add("q", "Quitter", self.handle_quit)
        return prod_menu.render()

    def last_menu(self, entry, history):
        """Method to authorize the user to return to the substitute products if he wants to chose another one"""
        product = history.get("Substitutes")
        category = history.get("Categories")
        sub_menu = Substitute(db, category)
        rows = sub_menu.get_substitute()
        substitute_menu = Menu("Last", f"Produits ayant un meilleur nutriscore que {product.name}")
        for n, r in enumerate(rows):
            product = ProductModel(r.id, r.name, r.link, r.nutriscore_letter)
            substitute_menu.add(f"{n + 1}", product, self.show_description)
        substitute_menu.add("a", "Retour à l'accueil", self.handle_start) \
            .add("q", "Quitter", self.handle_quit)
        return substitute_menu.render()

    def save_product(self, entry, history):
        """Method that allow the user to save the substitute product he chose"""
        origin_prod = history.get("Products")
        sub_prod = history.get("Substitutes")
        saver_obj = Favorite(db)
        saver_obj.save_favorite(origin_prod, sub_prod)
        save_menu = Menu("Save", f"Vous avez saugardé {sub_prod.name}") \
            .add("1", "Retour à la liste des catégories", self.handle_category_option) \
            .add("2", "Retour à la liste des produits substitutés", self.handle_product_substitutes) \
            .add("a", "Retour à l'accueil", self.handle_start) \
            .add("q", "Quitter", self.handle_quit)
        return save_menu.render()

    def show_favorites(self, entry, history):
        """Method that displays the user's favorites list. """
        fav = Favorite(db)
        show_fav = fav.show_favorite()
        fav_menu = Menu("Favorites", "Produits substitués")
        for n, prod in enumerate(show_fav):
            product = ProductDescription(prod.id, prod.name, prod.link, prod.store_name, prod.nutriscore_letter)
            fav_menu.add(f"{n + 1}", product, self.show_description)
        fav_menu.add("e", "Effacer les favoris", self.delete_favorites) \
            .add("a", "Revenir à l'accueil", self.handle_start) \
            .add("q", "Quitter", self.handle_quit)
        return fav_menu.render()

    def delete_favorites(self, entry, history):
        """Method that allow the user to delete all his favorites to the menu"""
        fav = Favorite(db)
        fav.delete_favorite()
        return (Menu("Effacer", "Vous avez effacé tous vos produits favoris")
                .add("a", "Retour à l'accueil", self.handle_start)
                .add("q", "Quitter", self.handle_quit)
                .render())

    def handle_quit(self, entry, history):
        """Method to quit the application"""
        print("Au revoir")
        self.running = False
