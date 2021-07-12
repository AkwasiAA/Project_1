class Product:
    def __init__(self, product_name, prod_description, quantity, purchase_price, selling_price, supplier, id = None):
        self.product_name = product_name
        self.prod_description = prod_description
        self.quantity = quantity
        self.purchase_price = purchase_price
        self.selling_price = selling_price
        self.supplier = supplier
        self.id = id