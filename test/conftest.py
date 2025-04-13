import pytest

from src.category import Category
from src.product import Product


@pytest.fixture
def first_product():
    return Product(
        "Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5
    )


@pytest.fixture
def first_category():
    return Category(
        "Смартфоны",
        "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни",
        ["Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5]
    )
