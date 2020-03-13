import records
import random
import constants as c
from database import client, cleaner

db = records.Database()


class Category:

    def __init__(self, db):
        self.db = db

    def get_product_by_category(self, cat_name):
        cat = cat_name
        rows = self.db.query("SELECT product.id, product.name, product.link " 
                             "FROM product "
                             "INNER JOIN product_category "
                             "ON product_category.product_id = product.id "
                             "INNER JOIN category "
                             "ON product_category.category_id = category.id "
                             "WHERE category.name = :cat_name", cat_name=cat)

        products = []
        count = 0
        for r in rows:
            product_name = r.name
            product_link = r.link
            products.append(product_name)
            products.append(product_link)

        while count < c.MAX_PROD:
            print(products)
            count += 1


if __name__ == '__main__':
    api = client.ProductFetcher()
    prod = api.fetch_products()
    cleaning = cleaner.Cleaner()
    clean_products = cleaning.clean(prod)
    get_prod_by_cat = Category(db)
    get_prod_by_cat.get_product_by_category("Epicerie")
