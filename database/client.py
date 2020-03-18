import requests
import constants as c


class ProductFetcher:
    """Class that fetch a raw products list from OpenFoodFacts"""
    def __init__(self, page_size=1000):
        self.categories = c.CATEGORIES_LIST
        self.page_size = page_size

    def fetch_products(self):
        for category in self.categories:
            parameters = {
                "action": "process",
                "tagtype_0": "categories",
                "tag_contains_0": "contains",
                "tag_0": f"{category}",
                "page_size": self.page_size,
                "sort_by": "unique_scan_n",
                "json": 1
            }
            r = requests.get(c.URL, parameters)
            data = r.json()["products"]
            products = []
            for product in data:
                product["categories"] = f"{category}, {product['categories']}"
                products.append(product)
            return products
