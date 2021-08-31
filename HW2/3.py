class ItemDiscount:

    def __init__(self, name, price):
        self.__name = name
        self.__price = price

    @property
    def get_name(self):
        return self.__name

    @property
    def get_price(self):
        return self.__price


class ItemDiscountReport(ItemDiscount):

    def get_parent_data(self):
        print(f"Название товара: {self.get_name}, цена: {self.get_price}")


item = ItemDiscountReport('Lamp', 1000)
item.get_parent_data()
