import records
from database import cleaner, client

db = records.Database()


class ProductsManager:
    """
        Class to create the table of the database
        Attribute:
            Database: link to the database
    """
    def __init__(self, database):
        """ Initialization of the class ProductManager"""
        self.db = database

    def create_tables(self):
        """ Method that create all the tables with the help of the table.sql script """
        with open("database/tables.sql") as sql_file:
            content = sql_file.read()

        sql_queries = content.split(";")
        for query in sql_queries:
            self.db.query(query)

    def drop_table(self, name):
        """ Method to delete the table we want by giving the name of the table in the parameters"""
        self.db.query(f"DROP TABLE IF EXISTS {name}")

    def drop_all_tables(self):
        """ Method to delete all the tables at the same time """
        tables_list = ["product_category", "product_store", "favorite", "category", "product", "nutriscore", "store"]
        for table in tables_list:
            self.db.query(f"DROP TABLE IF EXISTS {table}")

    def insert_nutriscore(self, nutri_data):
        """ Method to insert the nutriscore of the products in the table nutriscore """
        for nutri in nutri_data:
            nutriscore_letter = nutri["nutrition_grades"]

            self.db.query("INSERT IGNORE INTO nutriscore(nutriscore_letter) VALUES (:nutriscore_letter)",
                          nutriscore_letter=nutriscore_letter)

    def insert_categories(self, products):
        """ Method to insert all the categories of the product we want in the table category """
        for cat in products:
            category_list = cat["categories"].split(",")
            for category in category_list:
                self.db.query("INSERT IGNORE INTO category(name) VALUES (:name)",
                              name=category.replace("fr:", ""))

    def insert_products(self, products):
        """ Insertion of all the cleaned products in the table product """
        for product in products:
            nutriscore = product["nutrition_grades"]
            name = product["product_name"]
            id = product["code"]
            link = product["url"]

            self.db.query("INSERT IGNORE INTO product(id, name, link, nutriscore_id) "
                          "VALUES (:id, :name, :link, (SELECT id FROM nutriscore "
                          "WHERE nutriscore_letter= :nutri))",
                          id=id, name=name, link=link, nutri=nutriscore)

    def insert_stores(self, products):
        """ Insertion of the products' store in the table store """
        for store in products:
            store_name = store["stores"].split(",")
            for store_list in store_name:
                self.db.query("INSERT IGNORE INTO store(store_name)"
                              "VALUES(:store)", store=store_list)

    def insert_product_cat(self, products):
        """ insertion of the products code sorted by category and id in the association table product_category """
        for product in products:
            product_id = product["code"]
            cat_name = product["categories"].split(",")
            for cat in cat_name:
                # if "de:" not in cat and "en:" not in cat:
                self.db.query("INSERT IGNORE INTO product_category(product_id, category_id) "
                              "VALUES(:product_id, (SELECT id "
                              "FROM category WHERE name=:cat_name))",
                              product_id=product_id, cat_name=cat.replace("fr:", ""))

    def insert_product_store(self, products):
        """ Insertion of the products code sorted by store and product id in the association table product_store """
        for product in products:
            product_id = product["code"]
            store_name = product["stores"].split(",")
            for store in store_name:
                self.db.query("INSERT IGNORE INTO product_store(product_id, store_id) "
                              "VALUES(:product_id, "
                              "(SELECT store_id "
                              "FROM store "
                              "WHERE store_name=:store_name))", product_id=product_id, store_name=store)

    def insert_all_tables(self, products):
        """ Method to do the all the insertions at the same time """
        self.insert_nutriscore(products)
        self.insert_categories(products)
        self.insert_products(products)
        self.insert_stores(products)
        self.insert_product_store(products)
        self.insert_product_cat(products)

    @staticmethod
    def install_database():
        api = client.ProductFetcher()
        products = api.fetch_products()
        cleaning = cleaner.Cleaner()
        clean_products = cleaning.clean(products)
        manager = ProductsManager(db)
        manager.create_tables()
        manager.insert_all_tables(clean_products)




