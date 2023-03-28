from User import *

# class seller inherited from class user
class Seller(User): #type: ignore
    # using dependency
    # depended on class Food_Market
    def __init__(self, id: int, depended_class):
        self.__id  = id
    