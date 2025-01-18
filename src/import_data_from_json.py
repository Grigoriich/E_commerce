import json
import os
from typing import Dict, List

from src.category import Category
from src.product import Product


def read_json(path: str) -> List[Dict]:
    """Функция возвращает список словарей категорий товаров"""
    full_path = os.path.abspath(path)
    with open(full_path, "r", encoding="UTF-8") as file:
        data = json.load(file)
    return data


def create_category_from_json(data: List[Dict]) -> List[Category]:
    """Функция заполняет список объектами категории и объектами продуктов в данных категориях"""
    categories_list = []
    for category in data:
        products_list = []
        for product in category["products"]:
            products_list.append(Product(**product))
        category["products"] = products_list
        categories_list.append(Category(**category))
    return categories_list


if __name__ == "__main__":
    data = read_json("../data/products.json")
    categories = create_category_from_json(data)
    # print(data)
    print(categories)
    # print()
    print(categories[0].name)
    # print(categories[0].description)
    # print(categories[0].products)
    # print(categories[0].category_count)
    # print(categories[0].product_count)
    # print()
    print(categories[1].name)
    # print(categories[1].description)
    print(categories[1].products)
    # print(categories[1].products[0].name,
    #       categories[1].products[0].description,
    #       categories[1].products[0].price,
    #       categories[1].products[0].quantity)
    # print(categories[1].category_count)
    # print(categories[1].product_count)
