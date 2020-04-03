class ProductModel:
    """ Class called to display the product's info in the menu """
    def __init__(self, id, name, link, nutriscore):
        """ Initialization of the class """
        self.id = id
        self.name = name
        self.link = link
        self.nutriscore = nutriscore

    def __str__(self):
        """ Method to determine how to display the information we want and what exactly we want """
        return f"{self.name}. Nutriscore: {self.nutriscore}"
