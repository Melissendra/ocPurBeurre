import records

db = records.Database()


class ProductByCategory:
    """
        Class to get products by category
        Attributes:
            database: link the class to the database
            cat_name: it's a string that designates the category by which we'll find the product
    """
    def __init__(self, database, cat_name):
        """ Initialization of ProductByCategory class """
        self.db = database
        self.cat_name = cat_name

    def get_product_by_category(self):
        """ Request made to get 20 random products with an nutriscore to up or equal at c """
        cat_name = self.cat_name
        rows = self.db.query("SELECT product.id, product.name, product.link, nutriscore.nutriscore_letter " 
                             "FROM product "
                             "INNER JOIN nutriscore "
                             "ON product.nutriscore_id = nutriscore.id "
                             "INNER JOIN product_category "
                             "ON product_category.product_id = product.id "
                             "INNER JOIN category "
                             "ON product_category.category_id = category.id "
                             "WHERE category.name = :cat_name "
                             "AND nutriscore.nutriscore_letter >= 'c' "
                             "ORDER BY RAND() "
                             "LIMIT 20", cat_name=cat_name)
        return rows




