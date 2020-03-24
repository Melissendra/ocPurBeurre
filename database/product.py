import records

db = records.Database()


class Product:
    def __init__(self, db, product_name):
        self.db = db
        self.product_name = product_name

    def get_product_info(self):
        prod_name = self.product_name
        rows = self.db.query("SELECT product.name, product.link, store.store_name "
                             "FROM product "
                             "INNER JOIN product_store "
                             "ON product_store.product_id = product.id "
                             "INNER JOIN store "
                             "ON product_store.store_id = store.store_id "
                             "WHERE product.name = :prod_name ", prod_name=prod_name)
        return rows
