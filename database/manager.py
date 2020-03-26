import records

db = records.Database()


class Manager:

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
                             "AND nutriscore.nutriscore_letter >= 'c' "
                             "ORDER BY RAND() "
                             "LIMIT 20", cat_name=cat_name)
        return rows

    def get_substitute(self):
        cat_name = self.cat_name
        rows = self.db.query("SELECT product.id, product.name, product.link, "
                             "nutriscore.nutriscore_letter, store.store_name "
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
                             "ORDER BY RAND() "
                             "LIMIT 10 ", cat_name=cat_name)
        return rows

    def save_favorite(self, origin_prod, sub_prod):
        self.db.query("INSERT INTO favorite(product_original_id, product_substitute_id)"
                      "VALUES((SELECT id "
                      "FROM product "
                      "WHERE name=:origin_prod ), "
                      "(SELECT id "
                      "FROM product "
                      "WHERE name=:sub_prod))", origin_prod=origin_prod, sub_prod=sub_prod)



