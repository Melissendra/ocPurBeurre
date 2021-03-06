import records

db = records.Database()


class Substitute:
    """
        Class to get healthier product based on the category of the original product.
        All products will be with a nutriscore of a or b
        Attributes:
            database: link to the database
            cat_name(str): it's the category by which we select our products
    """
    def __init__(self, database, cat_name):
        """ Initialization of the class substitutes """
        self.db = database
        self.cat_name = cat_name

    def get_substitute(self):
        """ Requests to get 10 random  products to show it in a menu """
        cat_name = self.cat_name
        rows = self.db.query("SELECT product.id, product.name, product.link, "
                             "nutriscore.nutriscore_letter, "
                             "GROUP_CONCAT(store.store_name SEPARATOR ', ') AS store_name "
                             "FROM product "
                             "INNER JOIN nutriscore "
                             "ON product.nutriscore_id = nutriscore.id "
                             "INNER JOIN product_category "
                             "ON product_category.product_id = product.id "
                             "INNER JOIN category "
                             "ON product_category.category_id = category.id "
                             "INNER JOIN product_store "
                             "ON product_store.product_id = product.id "
                             "INNER JOIN store "
                             "ON product_store.store_id = store.store_id "
                             "WHERE category.name = :cat_name "
                             "AND nutriscore.nutriscore_letter < 'c' "
                             "GROUP BY product.id "
                             "ORDER BY RAND() "
                             "LIMIT 10 ", cat_name=cat_name)
        return rows
