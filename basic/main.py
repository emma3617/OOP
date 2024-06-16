# main.py
from Fruit import Fruit
from Shop import Shop




apple = Fruit("Apple",10,15)
banana = Fruit("Banana",5,10)
orange =Fruit ("Orange",20,35)
shop = Shop()
# 读取文件并解析内容
with open("salesData.txt", "r") as file:
    lines = file.readlines()  # 读取所有行
print("File lines:", lines)

fruit_names = lines[0].strip().split()  # 第一行为水果名称，去除换行符并分割成列表


# 创建水果名称到 Fruit 对象的映射
fruit_dict = {
    "apple": apple,
    "banana": banana,
    "orange": orange
}

for line in lines[1:]:
    quantities = [int(q) for q in line.strip().split()]  # 解析数量
    for fruit_name, quantity in zip(fruit_names, quantities):
        fruit = fruit_dict.get(fruit_name)
        if fruit:
            shop.addOrder(fruit, quantity)
        else:
            print(f"Error: {fruit_name} not found in fruit_dict")

report = shop.getReport()
print(report)
with open("shop_report.txt", "w") as file:
    file.write(report)
print("Report has been written to shop_report.txt")