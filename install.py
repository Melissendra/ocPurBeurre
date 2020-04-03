import records
from database.database_manager import ProductsManager

db = records.Database()

if __name__ == '__main__':
    manager = ProductsManager(db)
    manager.install_database()
