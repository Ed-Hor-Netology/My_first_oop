class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __eq__(self, other):
        return self.price == other.price

    def __lt__(self, other):
        return self.price < other.price

class Customer:
    def __init__(self, name):
        self.name = name
        self.orders = []

class Order:
    def __init__(self):
        self.products = []

    def add_product(self, product):
        self.products.append(product)

class Discount:
    @staticmethod
    def apply_discount(price, discount_percent):
        return price * (1 - discount_percent / 100)
# Создание продуктов
product1 = Product("Товар1", 100)
product2 = Product("Товар2", 200)

# Создание клиентов
customer1 = Customer("Клиент1")
customer2 = Customer("Клиент2")

# Создание заказов
order1 = Order()
order1.add_product(product1)
order1.add_product(product2)

# Применение скидки
discounted_price = Discount.apply_discount(product1.price, 10)

# Дополнительная логика для подсчета заказов и суммы заказов

# Вывод информации с использованием дандер методов
print(customer1)
print(order1)
print(product1)