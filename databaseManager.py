import records
import client
import cleaner

db = records.Database()


class ProductsManager:
    def __init__(self, db):
        self.db = db

    def create_little_table(self, name_tab, name_id, name_col):
        """Method to create the database's small tables """
        self.db.query(
            f'CREATE TABLE IF NOT EXISTS {name_tab}({name_id} INT NOT NULL AUTO_INCREMENT, {name_col} VARCHAR(150) NOT NULL UNIQUE, PRIMARY KEY({name_id}))'
            )

    def create_big_table(self, name_tab, name_id, name_col1, name_col2, name_col3, name_col4, name_col5):
        """Method to create the database's big tables"""
        self.db.query(
            f'CREATE TABLE IF NOT EXISTS {name_tab}({name_id} BIGINT NOT NULL, {name_col1} VARCHAR(255) NOT NULL UNIQUE, {name_col2} VARCHAR(150) NOT NULL UNIQUE, {name_col3} CHAR(1) NOT NULL, {name_col4} VARCHAR(150) NOT NULL UNIQUE, {name_col5} VARCHAR(150) NOT NULL, PRIMARY KEY({name_id}))'
        ) 

    def drop_table(self, name_tab):
        """Method to delete table when necessary"""
        self.db.query(
            f'DROP TABLE IF EXISTS {name_tab}'
        )

    def insert_data(self, products, tab_name):
        """Method to insert datas in database's tables"""

        for product in products:
            product_data = product["products"]
            product_id = product_data["id"]
            cat_name = product_data["categories"]
            product_name = product_data["brands"]
            product_score = product_data["nutrition_score_fr"]
            product_store = product_data["stores"]
            product_link = product_data["url"]

            self.db.query(f'INSERT INTO {tab_name}(product_id, cat_name) VALUES(:product_id, :cat_name)', product_id=product_id, cat_name=cat_name)


if __name__ == '__main__':
    api = client.ProductFetcher()
    products = api.fetch_products()
    cleaner = cleaner.Cleaner()
    clean_products = cleaner.clean(products)
    manager = ProductsManager(db)

    manager.drop_table("categories")
    manager.create_little_table("categories", "category_id", "category_name")
    manager.create_big_table("products", " product_id", "category_name", "product_brand", "nutriscore", "stores", "product_links")
    manager.insert_data(clean_products, "categories")
