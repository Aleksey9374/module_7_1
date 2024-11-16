# Задача "Учёт товаров":
# Необходимо реализовать 2 класса Product и Shop,
# с помощью которых будет производиться запись в файл с продуктами.
from collections import namedtuple
from pprint import pprint

class Product:
    def __init__(self, name, weight, category):
        self.name = str(name)  # название продукта
        self.weight = float(weight)  # общий вес товара
        self.category = str(category)  # категория товара

    def __str__(self):
        return '{}, {}, {}'.format(self.name, self.weight, self.category)

class Shop:
    __file_name = 'products.txt'
    def get_products(self):
        file = open(self.__file_name, 'r')
        products = file.read()
        file.close()
        return products

    def add(self, *products):
        file = open(self.__file_name, 'a')
        _products = self.get_products()
        for product in products:
            if product.name in _products:
                print(f'Продукт {product} уже есть в магазине')
            else:
                file.write(f'{product}\n')
        file.close()

s1 = Shop()
p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')

print(p2) # __str__

s1.add(p1, p2, p3)

print(s1.get_products())