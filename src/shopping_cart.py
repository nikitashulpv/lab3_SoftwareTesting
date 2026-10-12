class ShoppingCart:
    def __init__(self, catalog):
        self.catalog = catalog
        self.items = {}
        self.discount = 0

    def add_prod(self, product_id, quantity):
        if quantity <= 0:
            raise ValueError("Количество товара должно быть положительным")
        if product_id not in self.catalog:
            raise KeyError(f"Товар '{product_id}' не найден в каталоге")

        product = self.catalog[product_id]
        current_in_cart = self.items.get(product_id, 0)

        if current_in_cart + quantity > product.stock:
            raise ValueError(
                f"Недостаточно товара '{product_id}' на складе: "
                f"доступно {product.stock}, "
                f"в корзине уже {current_in_cart}, "
                f"запрошено ещё {quantity}"
            )

        self.items[product_id] = current_in_cart + quantity

    def delete_prod(self, product_id, quantity):
        if quantity <= 0:
            raise ValueError("Количество товара должно быть положительным")

        if product_id not in self.items:
            raise KeyError(f"Товар '{product_id}' не найден в корзине")

        if quantity > self.items[product_id]:
            raise ValueError("Недостаточно товара в корзине")

        if quantity == self.items[product_id]:
            del self.items[product_id]
        else:
            self.items[product_id] -= quantity

    def apply_promo(self, percent):
        if not 0 <= percent <= 100:
            raise ValueError("Скидка должна быть в диапазоне 0..100")
        self.discount = percent

    def total_sum(self):
        total = 0
        for product_id, quantity in self.items.items():
            product = self.catalog[product_id]
            total += product.price * quantity
        return total * (1 - self.discount / 100)
