import sys

# enter folder location and change \ to //
sys.path.insert(1,'D://bi12-year2//advpython//project//python_prj//control')
# access control file
from sql_connection import * #type: ignore

#food market class
class Food_Market:
    def __init__(self):
        self.__Products = get_existing_id("product")
        self.__Users = get_existing_id("user")
        self.__Sellers = []
        self.__Customer = []

        # sort existing users into customers or sellers
        for i in self.__Users:
            if get_user_info(i, "user_type") == 2:
                self.__Sellers.append(i)
            else:
                self.__Customer.append(i)
    

    def getProducts(self):
        return self.__Products 
    
    def getUsers(self):
        return self.__Users
    
    def getSellers(self):
        return self.__Sellers
    
    def getCustomer(self):
        return self.__Customer
    
        
    
# a = Food_Market()

# print(a.sort_product_by('name'))

    