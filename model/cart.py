class Cart:
    def __init__(self, customer_id: int):
        self.__cart_id = customer_id
        self.__products = {}

    # getters
    def get_Cart_id(self):
        return self.__cart_id
    
    def get_Products(self):
        return self.__products

    # add product
    def add_Product(self, add_product_id: int, add_product_quantity: int):
        self.__products[add_product_id] = add_product_quantity
        return
    
    # remove product 
    def remove_Product(self, remove_product_id: int):
        del self.__products[remove_product_id]
        return
        

    # modify product 
    def modify_Product(self, modified_product_id: int, modify_quantity: int):
        self.__products.update({modified_product_id: modify_quantity})
        return 




    
    