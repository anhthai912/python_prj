import sys

# enter folder location and change \ to //
sys.path.insert(1,'D://bi12-year2//advpython//project//python_prj//control')
# access control file
from sql_connection import * #type: ignore

#food market class
class Food_Market:
    def __init__(self):
        self.__Products = [1, 2, 3, 4, 5, 6,7 ,8, 9, 10]
        self.__Users = [1, 2, 3, 4, 5, 6,7 ,8, 9, 10]

    def getProducts(self):
        return self.__Products 
    
    def getUsers(self):
        return self.__Users
    
    