import requests
import json
from constants import URL, PARAMETERS


class ProductFetcher:
    def __init__(self):
        self.parameters = PARAMETERS

    def get_products(self):
        r = requests.get(URL, self.parameters)
        data = r.json()
        with open('data.json', 'w') as f:
            json.dump(data, f)
        print(data)


api = ProductFetcher()
api.get_products()
