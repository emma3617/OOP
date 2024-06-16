# shop.py
from OrderList import OrderList
from Order import Order

class Shop:
    def __init__(self):
        #如果只是使用列表来存储订单，代码会比较简单，但是缺乏封装和管理的逻辑，所以這邊不是用self.orderlist =[]
        self.orderlist = OrderList()

    def addOrder(self,fruit,number):
        order = Order(fruit,number)
        self.orderlist.addOrder(order)

    def getReport(self):
        total_cost = self.orderlist.getTotalCost()
        total_revenue = self.orderlist.getTotalRevenue()
        total_profit = total_revenue-total_cost
        report = (
            f"total cost:{total_cost}\n"
            f"total revenue:{total_revenue}\n"
            f"total profit:{total_profit}"
        )
        return report
