from Food_market import *


class Product:
    # auto increment id start from last id in database
    last_id = 10
    # using Dependency injection to access the product list from other class
    # here class Product is depended on class Food_Market
    def __init__(self, depended_class):
        # auto increment id
        self.id = Product.last_id + 1
        Product.last_id += 1

        # user input product and insert into database
        insert_product(self.id)  #type: ignore

        # input id in to Food_Market's product list
        self.depended_class = depended_class
        self.depended_class.getProducts().append(self.id)        
    
    # getters
    def get_product_id(self):
        return self.id
    
    
a = Food_Market()
    
test = Product(a)
print(a.getProducts())

        