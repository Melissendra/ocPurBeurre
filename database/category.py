import records
from database import client, cleaner


class Category:
    db = records.Database()

    def __init__(self, db, cat_name):
        self.db = db
        self.cat_name = cat_name

    def get_product_by_category(self, name):
        products = self.db.query(f"SELECT name, nutriscore_id, link FROM product WHERE name={name}")
        return products
