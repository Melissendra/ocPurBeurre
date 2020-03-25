import records
from database.category import Category
from database.substitutes import Substitute

db = records.Database()


class Favorite:

    def __init__(self, db):
        self.db = db

    def save_substitute(self,  product_original_name, product_substitute_name):

        self.db.query("INSERT INTO favorite(product_original_id, product_substitute_id) "
                      "VALUES((SELECT id FROM product WHERE name=product_original_name),"
                      "(SELECT id FROM product WHERE name=product_substitute_name))"