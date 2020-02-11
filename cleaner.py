import client
import json
import constants as c

class Cleaner:
    """Class to filter the data before putting it in the database"""

    def __init__(self):
        self.data = client.ProductFetcher(1)
        self.data_sorted = []

    def cleaner(self):
        data = self.data
        data_products = data.client()
        data_parse = data_products["products"]

        for element in data_parse:
            if all(tags_ok == element["categories"] for tags_ok in c.TAGS):
                products_cleaned = self.data_sorted.append(element)
                print(products_cleaned)


cleaner_class = Cleaner()
cleaner_class.cleaner()
