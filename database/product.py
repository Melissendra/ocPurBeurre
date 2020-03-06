import records
import random
import constants as c
from database import cleaner, client


db = records.Database()


class Product:
    def __init__(self):
        self.db = db

    def get_categories(self):
        cat_name = self.db.query("SELECT name FROM category ORDER BY id ")
        count = 0
        categories = []
        for cat in cat_name:
            category_name = cat.name.lower()
            categories.append(category_name)
        while count < 5:
            print(random.choice(categories))
            count += 1

    def get_products(self):
        pass


if __name__ == '__main__':
    api = client.ProductFetcher()
    cleaner = cleaner.Cleaner()
    product = Product()
    product.get_categories()
