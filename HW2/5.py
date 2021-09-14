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


class ItemDiscountReport(ItemDiscount):

    def __init__(self, name, price, discount):
        self.discount = discount
        super().__init__(name, price)

    def get_parent_data(self):
        print(
            f"Название товара: {self.get_name}, цена: {self.get_price}, цена со скидкой: {self.get_price * (1 - self.discount / 100)}  ")


item = ItemDiscountReport('Lamp', 1000, 20)
item.get_parent_data()
