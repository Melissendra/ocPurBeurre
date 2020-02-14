import records

db = records.Database()


class ProductsManager:
    def __init__(self, db):
        self.db = db

    def create_table(self, name, name_id):
        """Method to create the database's tables"""
        self.db.query(f'CREATE TABLE IF NOT EXISTS {name}({name_id} SMALLINT NOT NULL AUTO_INCREMENT, PRIMARY KEY({name_id}))')


if __name__ == '__main__':
    manager = ProductsManager(db)
    manager.create_table("categories", "category_id")
