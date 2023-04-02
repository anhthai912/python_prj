from Food_market import *

class Cart:
    def __init__(self, customer_id: int, depended_class):
        self.__cart_id = customer_id
        self.__products = {}
        self.depended_class = depended_class

    # getters
    def get_Cart_id(self):
        return self.__cart_id
    
    def get_Products(self):
        return self.__products
    
    def get_Product_quantity(self, product_id: int):
        return get_product_info(product_id, 'quantity')

    # add product
    def add_to_cart(self, add_product_id: int, add_product_quantity: int):
        if add_product_id not in self.depended_class.getProducts():
            return print("Product does not exist")
        else:
            self.__products[add_product_id] = add_product_quantity
            return
    
    # remove product 
    def remove_from_cart(self, remove_product_id: int):
        if remove_product_id not in self.__products:
            return print("error product is not in cart")
        else:
            del self.__products[remove_product_id]
            return
        

    # modify product 
    def modify_cart(self, modified_product_id: int, modify_quantity: int):
        if modified_product_id not in self.__products:
            return print("error, product not in cart")
        else:
            self.__products.update({modified_product_id: modify_quantity})
            return 
    
    # calculate total in cart
    def calculate_cart(self):
        total = 0
        for i in self.__products:
            total += self.__products[i] * self.get_Product_quantity(i)
        total = float(total)
        return total        
    
    # print bill
    def bill(self):
        total = self.calculate_cart()
        print("=========================================")
        print("                INVOICE                  ")
        print("=========================================")
        print("Item                                         Price                         Qty    ")
        print("-----------------------------------------")
        for item in self.__products:
            print(f"{get_product_info(item,'name'):20}\
                   {get_product_info(item,'price_per_unit'):10.2f}\
                  {self.get_Product_quantity(item):10}")
        print("-----------------------------------------")
        print(f"Total:                       {total:10.2f}")
        print("=========================================")
    
    # check out
    def check_out(self):
        self.bill()
        for i in self.__products:
            # change quantity in database
            updated_quantity = self.get_Product_quantity(i) - self.__products[i]
            modify_product(i, 'quantity', updated_quantity)
        self.__products = {}
        




# x = Food_Market()
    
# a = Cart(2,x)
# a.add_to_cart(2, 2)
# a.add_to_cart(3, 20)
# a.add_to_cart(6, 10)
# print(a.get_Products())
# a.check_out()
# print(a.get_Products())
# # a.bill()
# a.calculate_cart()