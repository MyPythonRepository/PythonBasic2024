# Створіть клас для опису товару
# (припустимо, це заділ для інтернет-магазину).
# Як поля товару можете використовувати значення ціни, опис,
# габарити товару. Створіть пару екземплярів вашого класу
# та протестуйте їхню роботу.
# Створіть клас "Покупець". Як поля можна використовувати
# прізвище, ім'я, по батькові, мобільний телефон і т.д.
# Створіть клас "Замовлення".
# Замовлення може містити кілька товарів,
# причому кількість кожного з товарів може бути різною.
# Замовлення має бути "підв'язане" до користувача, який його здійснив.
# Реалізуйте метод обчислення сумарної вартості замовлення.
# Визначте метод str() для коректного
# виведення інформації про це замовлення.


class Item:

    def __init__(self, product_name, price, description, dimensions):
        self.product_name = product_name
        self.price = price
        self.description = description
        self.dimensions = dimensions

    def __str__(self):
        return f"{self.product_name}: ${self.price}, {self.description}, {self.dimensions}"


class User:

    def __init__(self, name, surname, phone_number):
        self.name = name
        self.surname = surname
        self.phone_number = phone_number

    def __str__(self):
        return f"{self.name} {self.surname}, Phone: {self.phone_number}"

class Purchase:
    def __init__(self, user):
        self.user = user
        self.products = {}
        self.total = 0

    def add_item(self, item, count):
        self.products[item] = count
        self.total += item.price * count

    def __str__(self):
        itm = "\n".join(f"{i.product_name}: {count} pcs." for i, count in self.products.items())
        return f"User: {self.user}\nItems:\n{itm}\nTotal: ${self.total}"

    def get_total(self):
        return self.total

lemon = Item('lemon', 5, "yellow", "small", )
apple = Item('apple', 2, "red", "middle", )
print(lemon)  # lemon, price: 5

buyer = User("Ivan", "Ivanov", "02628162")
print(buyer)  # Ivan Ivanov

cart = Purchase(buyer)
cart.add_item(lemon, 4)
cart.add_item(apple, 20)
print(cart)
"""
User: Ivan Ivanov
Items:
lemon: 4 pcs.
apple: 20 pcs.
"""
assert isinstance(cart.user, User) is True, 'Екземпляр класу User'
assert cart.get_total() == 60, "Всього 60"
assert cart.get_total() == 60, 'Повинно залишатися 60!'

cart = Purchase(buyer)
cart.add_item(lemon, 4)
cart.add_item(apple, 10)
print(cart)
"""
User: Ivan Ivanov
Items:
lemon: 4 pcs.
apple: 10 pcs.
"""

assert cart.get_total() == 40
