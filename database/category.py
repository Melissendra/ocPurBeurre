import records

db = records.Database()


class Category:

    def __init__(self, db):
        self.db = db

    def get_product_by_category(self, cat_name):
        cat = cat_name
        rows = self.db.query("SELECT product.id, product.name, product.link, nutriscore.nutriscore_letter " 
                             "FROM product "
                             "INNER JOIN nutriscore "
                             "ON product.nutriscore_id = nutriscore.id "
                             "INNER JOIN product_category "
                             "ON product_category.product_id = product.id "
                             "INNER JOIN category "
                             "ON product_category.category_id = category.id "
                             "WHERE category.name = :cat_name "
                             "ORDER BY RAND() "
                             "LIMIT 2", cat_name=cat)

        for r in rows:
            product_name = r.name
            product_link = r.link
            nutri = r.nutriscore_letter
            print(product_name, product_link, nutri)


if __name__ == '__main__':
    get_prod_by_cat = Category(db)
    get_prod_by_cat.get_product_by_category("Epicerie")
