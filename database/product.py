import records
from database import cleaner, client

db = records.Database()


class Product:
    def __init__(self):
        self.db = db

    def get_categories(self):
        cat_name = self.db.query("SELECT name FROM category ORDER BY id ")
        for cat in cat_name:
            category_name = cat.name.lower()
            print(category_name)
            # return categories_name

    def get_products(self):
        pass


if __name__ == '__main__':
    api = client.ProductFetcher(10)
    cleaner = cleaner.Cleaner()
    product = Product()
    product.get_categories()
