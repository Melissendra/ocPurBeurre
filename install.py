import requests
import json
from constants import URL


class Product_fetcher:
    def __init__(self, category):
        self.category = category

    def get_products(self):
        response = requests.get(URL, self.category)
        print(response)


api = Product_fetcher('volaille')
api.get_products()