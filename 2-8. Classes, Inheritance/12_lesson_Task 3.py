class Product():
    def __init__(self, type, name, price):
        self.type = type
        self.name = name
        self.price = price
                
class ProductStore():
    def __init__(self):
        self.products = []
                
    def add_product(self, product):
        self.products.append(product)       
            
    def get_all_products(self):
        for i in self.products:
            print(i.type, i.name, i.price)
            
    def get_product_info(self, product):
        quantity = 0
        for product in self.products:
            quantity += 1
            print(product.name, quantity)

    def sell_product(self, product):
        if product in self.products:
            self.products.remove(product)

t1 = Product('Clothes', 'Short', 50)
t2 = Product('Clothes', 'Shorts', 70)
t3 = Product('Shoes', 'Snickers', 150)  

p = ProductStore()

p.add_product(t2)
p.add_product(t3)
p.get_all_products()
p.get_product_info(t2)