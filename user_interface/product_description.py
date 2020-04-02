from .product_model import ProductModel


class ProductDescription(ProductModel):
    """ class to display more information than the name of the product and its nutriscore grade """
    def __init__(self, id, name, link, store, nutriscore):
        super().__init__(id, name, link, nutriscore)
        self.store = store

    def __str__(self):
        """ How we format the information's display"""
        return f"{self.name}. \n\t" \
               f" {self.link}. \n\t  " \
               f" Magasin: {self.store}. \n\t" \
               f" Nutriscore: {self.nutriscore}"
