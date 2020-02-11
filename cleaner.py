import client
import json
import constants as c

class Cleaner:
    """Class to filter the data before putting it in the database"""

    def __init__(self):
        self.data = client.ProductFetcher()
        self.data_sorted = []

    def clean(self, products):
        data = self.data
        data_products = data.client()
        products_cleaned = self.data_sorted
        
        for element in products_cleaned:
            if self.is_valid(element):
                products_cleaned.append(element)

        return products_cleaned
            
    def is_valid(self, product):
        for tag in c.TAGS:
            if tag not in product:
                return False
            else:
                if not product[tag]:
                    return False
        return True

if __name__ == "__main__":
    pass
