
# APi's URL
URL = 'https://fr.openfoodfacts.org/cgi/search.pl'

""" Parameters to get the data from openFoodFacts' API"""

CATEGORIES = ["Epicerie", "Dessert", "Produits laitiers", "Boissons", "Charcuterie"]

PARAMETERS = {
    "action": "process",
    "json": 1,
    "tagtype_0": "categories",
    "tag_contains_0": "contains",
    "tag_0": CATEGORIES,
    "page_size": 20
}

