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

        # product's condition(available or not)
        self.__condition = 1        
    
    # getters
    def get_product_id(self):
        return self.__id
    def get_condition(self):
        return self.__condition
    
    # delete product
    def del_product(self):
        # temp_name to print the deleted product name after deletion
        temp_name = get_product_info(self.__id, "name")
        # delete product from database
        delete_product(self.__id)
        # delete product from list
        self.depended_class.getProducts().remove(self.__id)
        return f'{temp_name} has been deleted'
    
    # check product condition
    def condition_check(self):
        if get_product_info(self.__id, 'quantity') > 0:
            self.__condition = 1
            return self.__condition
        else:
            self.__condition = 0
            return self.__condition
    
a = Food_Market()
    
test = Product(a)
print(a.getProducts())
test.del_product()
print(a.getProducts())

        