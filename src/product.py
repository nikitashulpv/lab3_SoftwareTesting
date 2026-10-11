class Product:
    def __init__(self, id, name, price, stock):
        if price < 0:
            raise ValueError("Цена не может быть отрицательной")
        if stock < 0:
            raise ValueError("Количество на складе не может быть отрицательным")
        self.id = id
        self.name = name
        self.price = price
        self.stock = stock

    def is_available(self):
        return self.stock > 0

    def reduce_stock(self, amount):
        if amount > self.stock:
            raise ValueError("Недостаточно товара на складе")
        self.stock -= amount


    def __repr__(self):
        return f"Product(id={self.id!r}, name={self.name!r}, price={self.price}, stock={self.stock})"