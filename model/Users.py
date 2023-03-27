from Food_market import *
from sql_connection import *

class Users:
    # auto increment id start from last id in database
    last_id = 10
    # using Dependency injection to access the Users list from other class
    # here class Users is depended on class Food_Market
    def __init__(self, depended_class):
        # auto increment id
        self.id = Users.last_id + 1
        Users.last_id += 1

        # user input Users and insert into database
        insert_user(self.id)

        # input id in to Food_Market's Users list
        self.depended_class = depended_class
        self.depended_class.getUsers().append(self.id)        
    
    # getters
    def get_users_id(self):
        return self.id
    
a = Food_Market()
test = Users(a)

print(a.getUsers())