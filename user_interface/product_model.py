class ProductModel:
    def __init__(self, id, name, link, nutriscore):
        self.id = id
        self.name = name
        self.link = link
        self.nutriscore = nutriscore

    def __str__(self):
        return f"{self.name}. {self.nutriscore}."
