from src.product import Product
from src.shopping_cart import ShoppingCart

catalog = {
    "prod_102": Product("prod_102", "Смартфон", 29999, 10),
    "prod_205": Product("prod_205", "Наушники", 3000, 5),
}
cart = ShoppingCart(catalog)

cart.add_prod("prod_102", 2)
cart.add_prod("prod_205", 3)
print(cart.items)              # {'prod_102': 2, 'prod_205': 3}
print(cart.total_sum())        # 2*29999 + 3*3000 = 68998

cart.add_prod("prod_102", 3)   # в корзине 5, ок (склад 10)
print(cart.items)              # {'prod_102': 5, 'prod_205': 3}

try:
    cart.add_prod("prod_102", 10)   # 5+10=15 > 10 → ValueError
except ValueError as e:
    print(e)

cart.delete_prod("prod_102", 2)
print(cart.items)              # {'prod_102': 3, 'prod_205': 3}

cart.delete_prod("prod_205", 3)
print(cart.items)              # {'prod_102': 3}