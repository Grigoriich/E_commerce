def test_category_init(category_1, category_2):
    assert category_1.name == "Ноутбуки"
    assert category_1.description == "Описание"
    assert category_1.products == ["iphone", "xiaomi"]
    assert category_1.category_count == 2
    assert category_1.product_count == 4
