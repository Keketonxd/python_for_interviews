from typing import ItemsView


class ItemDiscount:

    def __init__(self, name, price):
        self.name = name
        self.price = price


class ItemDiscountReport(ItemDiscount):

    def get_parent_data(self):
        print(f"Название товара: {self.name}, цена: {self.price}")


item = ItemDiscountReport('Lamp', 1000)
item.get_parent_data()
