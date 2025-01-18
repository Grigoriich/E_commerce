import pytest

from src.category import Category
from src.product import Product


@pytest.fixture
def category_1():
    return Category("Ноутбуки", "Описание", ["iphone", "xiaomi"])


@pytest.fixture
def category_2():
    return Category("Пылесосы", "Описание", ["Bosch", "Philips"])


@pytest.fixture
def product_1():
    return Product("iphone 15", "Apple Iphone 15 128 Gb", 120000, 4)
