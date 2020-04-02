import records

db = records.Database()


class Product:
    """
        Class to get all the information of the product to display it when the user choose a product substitute
    """

    def __init__(self, database, product):
        """Initialization of the product class """
        self.db = database
        self.product = product

    def get_product_info(self):
        """ Function to get the information in the purbeurre database """
        prod = self.product
        rows = self.db.query("SELECT product.id, product.name, product.link, store.store_name, "
                             "nutriscore.nutriscore_letter "
                             "FROM product "
                             "INNER JOIN product_store "
                             "ON product_store.product_id = product.id "
                             "INNER JOIN store "
                             "ON product_store.store_id = store.store_id "
                             "INNER JOIN nutriscore "
                             "ON product.nutriscore_id = nutriscore.id "
                             "WHERE product.id = :prod_id ", prod_id=prod.id)
        return rows
