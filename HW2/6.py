class ItemDiscount:

    def __init__(self, name, price):
        self.__name = name
        self.__price = price

    def set_info(self, name, price):
        self.__name = name
        self.__price = price

    @property
    def get_name(self):
        return self.__name

    @property
    def get_price(self):
        return self.__price


class ItemDiscountNameReport(ItemDiscount):

    def get_info(self):
        print(
            f"Название товара: {self.get_name}")


class ItemDiscountPriceReport(ItemDiscount):
    def get_info(self):
        print(
            f"Цена: {self.get_price}")


name = ItemDiscountNameReport('Table', 999)
name.get_info()

price = ItemDiscountPriceReport('Table', 999)
price.get_info()
