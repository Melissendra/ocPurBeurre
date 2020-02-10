import client
import constants as c

class Cleaner:
    """Class to filter the data before putting it in the database"""

    def __init__(self):
        self.data = client.ProductFetcher()
        self.cleaned_products = []

    def cleaner(self):
        data = self.data
        data_products = data.client()
        for element in data_products:
            for category in c.CATEGORIES_LIST:
                category_split = element["categories"].split(",")


