import requests
import json
import constants as c


class ProductFetcher:

    def __init__(self, page_size=1):
        self.categories = c.CATEGORIES_LIST
        self.page_size = page_size

    def get_products(self):
        for category in self.categories:
            parameters = {
                "action": "process",
                "tagtype_0": "categories",
                "tag_contains_0": "contains",
                "tag_0": category,
                "page_size": self.page_size,
                "sort_by": "unique_scan_n",
                "json": 1
            }
            r = requests.get(c.URL, parameters)
            data = r.json()
            with open('data.json', 'w') as f:
                json.dump(data, f, indent=4)

            print(data["tag_0"])


api = ProductFetcher()
api.get_products()
