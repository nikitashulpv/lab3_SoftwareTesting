import pytest
from src.product import Product

def test_create_valid_product():
    p = Product("prod_1", "Смартфон", 29999, 10)
    assert p.id == "prod_1"
    assert p.name == "Смартфон"
    assert p.price == 29999
    assert p.stock == 10


def test_negative_price_raises():
    with pytest.raises(ValueError):
        Product("prod_1", "X", -1, 10)

def test_negative_stock_raises():
    with pytest.raises(ValueError):
        Product("prod_1", "X", 100, -1)

def test_is_available_true():
    p = Product("prod_1", "X", 100, 5)
    assert p.is_available() is True

def test_is_available_false():
    p = Product("prod_1", "X", 100, 0)
    assert p.is_available() is False

def test_reduce_stock_success():
    p = Product("prod_1", "X", 100, 10)
    p.reduce_stock(3)
    assert p.stock == 7

def test_reduce_stock_too_much_raises():
    p = Product("prod_1", "X", 100, 5)
    with pytest.raises(ValueError):
        p.reduce_stock(10)

def test_repr():
    p = Product("prod_1", "Смартфон", 29999, 10)
    assert "prod_1" in repr(p)
    assert "Смартфон" in repr(p)