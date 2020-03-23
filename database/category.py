import records

db = records.Database()


class Category:

    def __init__(self, db, cat_name):
        self.db = db
        self.cat_name = cat_name

    def get_product_by_category(self):
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
                             "AND nutriscore.nutriscore_letter IN ('c', 'd', 'e') "
                             "ORDER BY RAND() "
                             "LIMIT 20", cat_name=cat_name)
        return rows

