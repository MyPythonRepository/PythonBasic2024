# Користувач вводить через дефіс дві літери, Ваше завдання написати програму,
# яка повертатиме всі символи між ними включно.
# Жодних перевірок на помилку робити не треба, мінімальне значення завжди
# менше або дорівнює максимальному.
# Підказка: Використовуйте модуль string, у якому є string.ascii_letters, з
# усім набором потрібних букв
#
# Приклад:
# "a-c" -> abc
# "a-a" -> a
# "s-H" -> stuvwxyzABCDEFGH
# "a-A" -> abcdefghijklmnopqrstuvwxyzA

import string

all_letters = string.ascii_letters

user_input = input("Please enter two letters separated by a hyphen(e.g., a-c): ")

first_letter, last_letter = user_input.split("-")

first_index = all_letters.index(first_letter)

last_index = all_letters.index(last_letter)

result = all_letters[first_index:last_index + 1]

print(result)
