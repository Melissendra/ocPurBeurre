import records

db = records.Database()


class Favorite:
    def __init__(self, db):
        self.db = db

    def save_favorite(self, origin_prod, sub_prod):
        self.db.query("INSERT INTO favorite(product_original_id, product_substitute_id)"
                      "VALUES( :origin_prod, :sub_prod) "
                       , origin_prod=origin_prod.id, sub_prod=sub_prod.id)

    def show_favorite(self):
        rows = self.db.query("SELECT sub_prod.id, sub_prod.name, sub_prod.link, "
                             "sub_prod_nutriscore.nutriscore_letter, "
                             "GROUP_CONCAT(store.store_name SEPARATOR ', ') AS store_name "
                             "FROM favorite "
                             "INNER JOIN product AS origin_prod "
                             "ON favorite.product_original_id = origin_prod.id "
                             "INNER JOIN product AS sub_prod "
                             "ON favorite.product_substitute_id = sub_prod.id "
                             "INNER JOIN product_store "
                             "ON product_store.product_id = sub_prod.id "
                             "INNER JOIN store "
                             "ON product_store.store_id = store.store_id "
                             "INNER JOIN nutriscore AS origin_prod_nutriscore "
                             "ON origin_prod.nutriscore_id = origin_prod_nutriscore.id "
                             "INNER JOIN nutriscore AS sub_prod_nutriscore "
                             "ON sub_prod.nutriscore_id = sub_prod_nutriscore.id "
                             "GROUP BY sub_prod.id ")
        return rows

    def delete_favorite(self):
        self.db.query("DELETE FROM favorite")

