class Data:
    def __init__(self):
        self.products = []

    def add_product(self, name, price, quantity):
        product = {
            'name': name,
            'price': price,
            'quantity': quantity
        }
        self.products.append(product)

    def get_products(self):
        return self.products