# order.py
from Fruit import Fruit

class Order:
    def __init__(self, fruit, number):
        self.__fruit = fruit
        self.__number = number
    def getOrderCost(self):
        return (self.__fruit.get_cost()*self.__number)
    def getOrderRevenue(self):
        return (self.__fruit.get_price() * self.__number)