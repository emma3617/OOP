# Fruit, Order, OrderList, Shop, and main

class Fruit:
    def __init__(self, name,  cost,  price):
        self.__name = name
        self.__cost = cost
        self.__price = price
    def get_cost(self):
        return self.__cost  # 提供访问私有属性的方法

    def set_cost(self, cost):
        self.__cost = cost  # 提供修改私有属性的方法

    def get_price(self):
        return self.__price
    
    def set_price(self,price):
        self.__price = price

    def info(self):
        return f" {self.__name} and  {self.__cost} ,and {self.__price}"
        