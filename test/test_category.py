

def test_category_init(first_category):
    assert first_category.name == "Смартфоны"
    assert first_category.description == "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни"
    assert first_category.products == ["Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5]
