import requests
import json
import constants as c


class ProductFetcher:

    def __init__(self, page_size=1000):
        self.categories = c.CATEGORIES_LIST
        self.page_size = page_size
        self.data_list = []

    def client(self):
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
            raw_product_list = self.data_list.append(data)

            return raw_product_list



