from .product_model import ProductModel


class ProductDescription(ProductModel):
    def __init__(self, id, name, link, store, nutriscore):
        super().__init__(id, name, link, nutriscore)
        self.store = store

    def __str__(self):
        return f"{self.name}. {self.link}. Magasin: {self.store}. Nutriscore: {self.nutriscore}"
