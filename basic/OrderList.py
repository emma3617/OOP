# orderlist.py
from Order import Order

class OrderList:
    def __init__(self):
        self.orders = []  # 初始化一个空列表来存储订单

    def addOrder(self, order):
        self.orders.append(order)  # 将订单对象添加到订单列表

    def getTotalCost(self):
        total_cost = 0
        for order in self.orders:
            total_cost += order.getOrderCost()  # 累加每个订单的总成本
        return total_cost

    def getTotalRevenue(self):
        total_revenue = 0
        for order in self.orders:
            total_revenue += order.getOrderRevenue()  # 累加每个订单的总收入
        return total_revenue