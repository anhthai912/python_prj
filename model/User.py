from Food_market import *
from Seller import *

class Users:
    # auto increment id start from last id in database
    last_id = len(get_existing_id("user"))
    # using Dependency injection to access the Users list from other class
    # here class Users is depended on class Food_Market
    def __init__(self, depended_class):
        # auto increment id
        self.__id = Users.last_id + 1
        Users.last_id += 1

        # user input Users and insert into database
        insert_user(self.__id) #type: ignore

        # input id in to Food_Market's Users list
        self.depended_class = depended_class
        self.depended_class.getUsers().append(self.__id)       


        # sort user into seller or customer
        if get_user_info(self.__id, "user_type") == 2:
            self.depended_class.getSellers().append(self.__id)
            

        else: 
            self.depended_class.getCustomers().append(self.__id)
 
    
    # getters
    def get_user_id(self):
        return self.__id

a = Food_Market()
test = Users(a)

print(a.getUsers())
print(a.getSellers())
print(a.getCustomer())
print(get_user_info(test.get_user_id(), "user_type"))