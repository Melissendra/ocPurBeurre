import requests
import constants as c


class ProductFetcher:
    """Class that fetch a raw products list from OpenFoodFacts"""
    def __init__(self, page_size=1000):
        self.categories = c.CATEGORIES_LIST
        self.page_size = page_size

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
            # print(data["products"][0]["categories"])
            return data


# api = ProductFetcher(1)
# api.client()
