import records

db = records.Database()


class Category:

    def __init__(self, db, cat_name):
        self.db = db
        self.cat_name = cat_name
        # self.product_name = ""
        # self.product_link = ""
        # self.nutriscore = ""

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
                             "ORDER BY RAND() "
                             "LIMIT 20", cat_name=cat_name)
        return rows

    # def show_products(self):
    #     rows = self.get_product_by_category()
    #     for i, r in enumerate(rows):
    #         self.product_name = r.name
    #         self.product_link = r.link
    #         self.nutriscore = r.nutriscore_letter
    #         result = f"{i+1}. {self.product_name}, {self.product_link}, {self.nutriscore}"
    #         print(result)


if __name__ == '__main__':
    get_prod_by_cat = Category(db, "Epicerie")
    # get_prod_by_cat.show_products()
