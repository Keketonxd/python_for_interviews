class ItemDiscount:

    def __init__(self, name, price):
        self.__name = name
        self.__price = price


class ItemDiscountReport(ItemDiscount):

    @property
    def get_parent_data(self):
        print(f"Название товара: {self.__name}, цена: {self.__price}")


item = ItemDiscountReport('Lamp', 1000)
item.get_parent_data()
