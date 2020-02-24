import records
import client
import cleaner
import constants as c

db = records.Database()


class ProductsManager:
    def __init__(self, db):
        self.db = db

    def create_tables(self):
        with open("tables.sql") as sql_file:
            content = sql_file.read()

        sql_queries = content.split(";")
        for query in sql_queries:
            self.db.query(query)

    def drop_tables(self, name):
        self.db.query(f"DROP TABLE IF EXISTS {name}")

    def insert_nutriscore(self, nutri_data):
        for nutri in nutri_data:
            nutriscore_letter = nutri["nutrition_grades"]

            self.db.query("INSERT IGNORE INTO nutriscore(nutriscore_letter) VALUES (:nutriscore_letter)",
                          nutriscore_letter=nutriscore_letter)

    # def insert_categories(self, category):
    #     for cat in c.CATEGORIES_LIST:
    #         cat_list = category.strip(" ")
    #         name = cat[cat_list]
    #         self.db.query("INSERT IGNORE INTO category(name) VALUES (:name)",
    #                       name=name)

    def insert_products(self, products_data):
        for product in products_data:
            name = product["product_name"]
            id = product["code"]
            link = product["url"]
            nutriscore_id = self.db.query("INSERT INTO product(nutriscore_id) VALUES ((SELECT id FROM nutriscore WHERE id IN (SELECT id FROM nutriscore)))")
            self.db.query("INSERT INTO product(id, name, link, nutriscore_id) "
                          "VALUES (:id, :name, :link, :nutriscore_id)", id=id, name=name,  link=link, nutriscore_id=nutriscore_id)



if __name__ == '__main__':
    api = client.ProductFetcher(3)
    products = api.fetch_products()
    cleaner = cleaner.Cleaner()
    clean_products = cleaner.clean(products)
    manager = ProductsManager(db)
    manager.drop_tables("product_category")
    manager.drop_tables("product_store")
    manager.drop_tables("favorite")
    manager.drop_tables("category")
    manager.drop_tables("product")
    manager.drop_tables("nutriscore")
    manager.drop_tables("store")
    manager.create_tables()
    manager.insert_nutriscore(clean_products)
    manager.insert_products(clean_products)
