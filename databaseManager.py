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
            f'CREATE TABLE IF NOT EXISTS {name_tab}({name_id} SMALLINT NOT NULL AUTO_INCREMENT, {name_col} VARCHAR(50) NOT NULL UNIQUE, PRIMARY KEY({name_id}))'
            )

    def create_big_table(self, name_tab, name_id, name_col1, name_col2, name_col3, name_col4, name_col5):
        """Method to create the database's big tables"""
        self;db.query(
            f'CREATE TABLE IF NOT EXISTS {name_tab}({name_id} SMALLINT NOT NULL AUTO_INCREMENT, {name_col1} VARCHAR(50) NOT NULL UNIQUE, {name_col2} VARCHAR(50) NOT NULL UNIQUE, {name_col3} CHAR(1) NOT NULL, {name_col4} VARCHAR(50) NOT NULL UNIQUE, {name_col5} VARCHAR(100) NOT NULL)'
        ) 

    def drop_table(self, name_tab):
        """Method to delete table when necessary"""
        self.db.query(
            f'DROP TABLE IF EXISTS {name_tab}'
        )

    def insert_data(self, products, tab_name):
        """Method to insert datas in database's tables"""
        api = client.ProductFetcher()
        data = api.fetch_products()
        products_cleaner = cleaner.Cleaner()
        clean_products = products_cleaner.clean(data)

        for product in clean_products['products']:
            

if __name__ == '__main__':
    manager = ProductsManager(db)
    manager.drop_table("categories")
    manager.create_table("categories", "category_id", "category_name")
