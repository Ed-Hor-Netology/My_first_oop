class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price
    
    def __str__(self):   #Строковое представление товара для пользователя.
        return f"Товар (Наименование = {self.name}, Цена = {self.price})"
    
    def __repr__(self):  #Строковое представление товара для разработчика.
        return f"Товар (Наименование = {self.name}, Цена = {self.price})"
    
    def __eq__(self, other):
        return self.price == other.price

    def __lt__(self, other):
        return self.price < other.price

class Customer:
    def __init__(self, name):
        self.name = name
        self.orders = []
    def add_order(self, order):  #Добавление заказа клиенту.
        self.orders.append(order)

    def __str__(self):     #Строковое представление клиента для пользователя.
        return f"Клиент (Имя = {self.name}, Заказы = {len(self.orders)})"

    def __repr__(self):  #Строковое представление клиента для разработчика.
        return f"Клиент (Имя = {self.name}, Заказы = {len(self.orders)})"

class Order:
    def __init__(self, products):
        self.products = products
        Order._total_orders += 1
    @classmethod
    def total_orders(cls):  #Получение общего количества заказов.:return: Общее количество заказов 
        return cls._total_orders
    @classmethod
    def total_revenue(cls, orders): #Подсчет общей суммы всех заказов.:param orders: Список всех заказов :return: Общая сумма всех заказов
        return sum(order.total_price() for order in orders)

    def total_price(self): #Подсчет общей стоимости товаров в заказе.:return: Общая стоимость товаров
        return sum(product.price for product in self.products)  
    
    def __str__(self): #Строковое представление заказа для пользователя. 
        return f"Заказ (Общая стоимость = {self.total_price()})"
    
    def __repr__(self): #Строковое представление заказа для разработчика.
        return f"Заказ (Общая стоимость = {self.total_price()})"
 
    # def add_product(self, product):
    #     self.products.append(product)

class Discount:
    def __init__(self, description, discount_percent): #Инициализация скидки.
  #:param description: Описание скидки 
  # param discount_percent: Процент скидки 

        self.description = description 
        self.discount_percent = discount_percent
    @staticmethod
    def apply_discount(price, discount_percent):
        """
Применение скидки к цене.
:param price: Оригинальная цена
:param discount_percent: Процент скидки 
:return: Цена с примененной скидкой
"""
        return price * (1 - discount_percent / 100)
    
    def apply_to_order(self, order):
        """
Применение скидки ко всем товарам в заказе.
:param order: Заказ
:return: Общая стоимость заказа после применения скидки """
        return sum(Discount.apply_discount(product.price, self.discount_percent) for product in order.products)

    def __str__(self): #Строковое представление скидки для пользователя.

        return f"Скидка (Описание = {self.description}, Процент скидки={self.discount_percent}%)"
    def __repr__(self): #Строковое представление скидки для разработчика.

        return f"Скидка (Описание = {self.description}, Процент скидки={self.discount_percent}%)"


# Создание продуктов
product1 = Product("Товар1", 100)
product2 = Product("Товар2", 200)
product3 = Product("Товар3", 300)

# Создание клиентов
customer1 = Customer("Клиент1")
customer2 = Customer("Клиент2")

# Создание заказов
order1 = Order([product1, product2])
order2 = Order([product3, product1]) 
customer1.add_order(order1)
customer2.add_order(order2)
# order1 = Order()
# order1.add_product(product1)
# order1.add_product(product2)

# Создаем скидки
seasonal_discount = Discount("Сезонная скидка", 10) 
promo_code_discount = Discount("Скидка по промо коду", 20)


# Применяем скидки к заказам

discounted_price_order1 = seasonal_discount.apply_to_order(order1) 
discounted_price_order2 = promo_code_discount.apply_to_order(order2)

print(f"Первоначальная цена заказа 1: {order1.total_price()}") 
print(f"Сниженная цена заказа 1: {discounted_price_order1}")

#discounted_price = Discount.apply_discount(product1.price, 10)

# Дополнительная логика для подсчета заказов и суммы заказов


# Выводим информацию о клиентах 
print(customer1) 
print(customer2)

# Выводим общее количество заказов
print(f"Общее количество заказов: {Order.total_orders()}")


# Выводим общую сумму всех заказов
all_orders = customer1.orders + customer2.orders 
print(f"Общий доход: {Order.total_revenue(all_orders)}")

# # Вывод информации с использованием дандер методов
# print(customer1)
# print(order1)
# print(product1)