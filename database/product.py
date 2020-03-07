import records
import random
from database import cleaner, client


db = records.Database()


class Product:
    def __init__(self):
        self.db = db


if __name__ == '__main__':
    api = client.ProductFetcher()
    cleaner = cleaner.Cleaner()
    product = Product()
    product.get_categories()
