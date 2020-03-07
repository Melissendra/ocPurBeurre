import constants as c


class Cleaner:
    """Class to filter the data before putting it in the database"""

    def __init__(self):
        self.data_sorted = []

    def clean(self, products):
        products_cleaned = self.data_sorted
        for element in products:
            if self.is_valid(element):
                products_cleaned.append(element)
        return products_cleaned

    @staticmethod
    def is_valid(product):
        for tag in c.TAGS:

            if tag not in product:
                return False
            else:
                if not product[tag]:
                    return False
        return True

