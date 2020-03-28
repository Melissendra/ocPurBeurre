import records

db = records.Database()


class Favorite:
    def __init__(self, db ):
        self.db = db
        # self.origin_prod = origin_prod
        # self.sub_prod = sub_prod

    def save_favorite(self, origin_prod, sub_prod):
        self.db.query("INSERT INTO favorite(product_original_id, product_substitute_id)"
                      "VALUES( :origin_prod, :sub_prod) "
                       , origin_prod=origin_prod.id, sub_prod=sub_prod.id)

    def show_favorite(self):
        rows = self.db.query("SELECT product.id, product.name, product.link, nutriscore.nutriscore_letter, store.store_name "
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
                             "ON favorite.product_original_id = origin_prod_nutriscore.id "
                             "WHERE favorite.product_substitute_id = favorite.product_original_id")
        return rows

    def delete_favorite(self):
        self.db.query("DELETE FROM favorite")
