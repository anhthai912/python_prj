from Food_market import *


class Product:
    # auto increment id start from last id in database
    last_id = len(get_existing_id("product"))   #type:ignore
    # using Dependency injection to access the product list from other class
    # here class Product is depended on class Food_Market
    def __init__(self, depended_class):
        # auto increment id
        self.__id = Product.last_id + 1
        Product.last_id += 1

        # user input product and insert into database
        insert_product(self.__id)  #type: ignore

        # input id in to Food_Market's product list
        self.depended_class = depended_class
        self.depended_class.getProducts().append(self.__id)        
    
    # getters
    def get_product_id(self):
        return self.__id
    
    # delete product
    def del_product(self):
        # temp_name to print the deleted product name after deletion
        temp_name = get_product_info(self.get_product_id(), "name")
        # delete product from database
        delete_product(self.get_product_id())
        # delete product from list
        self.depended_class.getProducts().remove(self.get_product_id())
        return f'{temp_name} has been deleted'
    
    
a = Food_Market()
    
test = Product(a)
print(a.getProducts())
test.del_product()
print(a.getProducts())

        