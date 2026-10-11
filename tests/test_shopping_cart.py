import pytest
from src.product import Product
from src.shopping_cart import ShoppingCart

@pytest.fixture
def catalog():
    return {
        "prod_1": Product("prod_1", "Смартфон", 29999, 10),
        "prod_2": Product("prod_2", "Наушники", 3000, 5),
    }

@pytest.fixture
def cart(catalog):
    return ShoppingCart(catalog)

def test_quantity_stock_not_enough(cart):
    with pytest.raises(ValueError):
        cart.add_prod("prod_1", 11)

def test_add_new_product(cart):
    cart.add_prod("prod_1", 3)
    assert cart.items == {"prod_1": 3}

def test_add_existing_product_sums(cart):
    cart.add_prod("prod_1", 3)
    cart.add_prod("prod_1", 2)
    assert cart.items == {"prod_1": 5}

def test_add_zero_raises(cart):
    with pytest.raises(ValueError):
        cart.add_prod("prod_1", 0)

def test_add_negative_raises(cart):
    with pytest.raises(ValueError):
        cart.add_prod("prod_1", -1)

def test_add_unknown_product_raises(cart):
    with pytest.raises(KeyError):
        cart.add_prod("nonexistent", 1)

def test_add_exceeding_stock_raises(cart):
    with pytest.raises(ValueError):
        cart.add_prod("prod_1", 11)   # stock = 10

def test_add_exceeding_stock_with_existing(cart):
    cart.add_prod("prod_1", 8)
    with pytest.raises(ValueError):
        cart.add_prod("prod_1", 5)   # 8+5 > 10

def test_delete_partial(cart):
    cart.add_prod("prod_1", 5)
    cart.delete_prod("prod_1", 2)
    assert cart.items == {"prod_1": 3}

def test_delete_full(cart):
    cart.add_prod("prod_1", 5)
    cart.delete_prod("prod_1", 5)
    assert "prod_1" not in cart.items

def test_delete_zero_raises(cart):
    cart.add_prod("prod_1", 5)
    with pytest.raises(ValueError):
        cart.delete_prod("prod_1", 0)

def test_delete_unknown_raises(cart):
    with pytest.raises(KeyError):
        cart.delete_prod("prod_1", 1)

def test_delete_too_much_raises(cart):
    cart.add_prod("prod_1", 3)
    with pytest.raises(ValueError):
        cart.delete_prod("prod_1", 5)

def test_total_empty_cart(cart):
    assert cart.total_sum() == 0

def test_total_one_product(cart):
    cart.add_prod("prod_1", 2)     # 2 * 29999 = 59998
    assert cart.total_sum() == 59998

def test_total_multiple_products(cart):
    cart.add_prod("prod_1", 2)     # 2 * 29999 = 59998
    cart.add_prod("prod_2", 3)     # 3 * 3000  = 9000
    assert cart.total_sum() == 68998