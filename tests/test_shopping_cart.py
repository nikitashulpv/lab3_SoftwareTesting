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


def test_apply_promo(cart):
    cart.add_prod("prod_1", 1)
    cart.apply_promo(10)
    assert cart.total_sum() == pytest.approx(26999.1)

def test_promo_no_discount(cart):
    cart.add_prod("prod_1", 1)
    cart.apply_promo(0)
    assert cart.total_sum() == pytest.approx(29999)

def test_promo_discount_less0(cart):
    cart.add_prod("prod_1", 1)
    with pytest.raises(ValueError):
        cart.apply_promo(-1)

def test_promo_discount_over100(cart):
    cart.add_prod("prod_1", 1)
    with pytest.raises(ValueError):
        cart.apply_promo(101)

def test_promo_full_discount(cart):
    cart.add_prod("prod_1", 1)
    cart.apply_promo(100)
    assert cart.total_sum() == pytest.approx(0)

def test_promo_on_empty_cart(cart):
    cart.apply_promo(10)
    assert cart.total_sum() == 0

def test_promo_multiple_products(cart):
    cart.add_prod("prod_1", 2)
    cart.add_prod("prod_2", 3)
    cart.apply_promo(10)
    assert cart.total_sum() == pytest.approx((59998 + 9000) * 0.9)

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
        cart.add_prod("prod_1", 11)

def test_add_exceeding_stock_with_existing(cart):
    cart.add_prod("prod_1", 8)
    with pytest.raises(ValueError):
        cart.add_prod("prod_1", 5)

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
    cart.add_prod("prod_1", 2)
    assert cart.total_sum() == 59998

def test_total_multiple_products(cart):
    cart.add_prod("prod_1", 2)
    cart.add_prod("prod_2", 3)
    assert cart.total_sum() == 68998