# E_commerce

## Описание:

Проект "E_commerce" это ядро для интернет магазина. В дальнейшем для этого ядра возможно будет реализовать любой интерфейс — от сайта до телеграм-бота.

## Использование:

**1. Основная логика выполняется в модуле main.py**  
В модуле реализован функционал загрузки категорий товаров и продуктов в категориях из json файла.
Категории и продукты реализованы с применением концепции ООП.

**2. Проект содержит функции:**
- read_json: возвращает список словарей категорий товаров. Пример работы функции:
```
#Ввод:
data = read_json("../data/products.json")
print(data)
#Вывод:
[{'name': 'Смартфоны', 
         'description': 'Смартфоны, как средство не только коммуникации, но и получение дополнительных функций для удобства жизни', 
         'products': [{'name': 'Samsung Galaxy C23 Ultra', 'description': '256GB, Серый цвет, 200MP камера', 
                       'price': 180000.0, 
                       'quantity': 5}, 
                      {'name': 'Iphone 15', 
                       'description': '512GB, Gray space', 
                       'price': 210000.0, 'quantity': 8}, 
                      {'name': 'Xiaomi Redmi Note 11', 
                       'description': '1024GB, Синий', 
                       'price': 31000.0, 'quantity': 14}]}, 
        {'name': 'Телевизоры', 
         'description': 
             'Современный телевизор, который позволяет наслаждаться просмотром, станет вашим другом и помощником', 
         'products': [{'name': '55" QLED 4K', 'description': 'Фоновая подсветка', 'price': 123000.0, 'quantity': 7}]}]
```

- create_category_from_json: заполняет список объектами категории и объектами продуктов в данных категориях. Пример работы функции:
```
#Ввод:
data = read_json("../data/products.json")
categories = create_category_from_json(data)
print(categories)
print(categories[0].name)
print(categories[1].name)
print(categories[1].products)
#Вывод:
[<src.category.Category object at 0x000001349EBC23C0>, <src.category.Category object at 0x000001349ED1C410>]
Смартфоны
Телевизоры
[<src.product.Product object at 0x000001349E89BCE0>]
```