import records

db = records.Database()


class Product:
    def __init__(self, db, product):
        self.db = db
        self.product = product

    def get_product_info(self):
        prod = self.product
        rows = self.db.query("SELECT product.name, product.link, store.store_name, nutriscore.nutriscore_letter "
                             "FROM product "
                             "INNER JOIN product_store "
                             "ON product_store.product_id = product.id "
                             "INNER JOIN store "
                             "ON product_store.store_id = store.store_id "
                             "INNER JOIN nutriscore "
                             "ON product.nutriscore_id = nutriscore.id "
                             "WHERE product.id = :prod_id ", prod_id=prod.id)
        return rows
