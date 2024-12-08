# Напишіть програму, яка запитує у користувача рядок і визначає, чи містить
# він тільки унікальні символи. Якщо всі символи в рядку унікальні, виведіть
# відповідне повідомлення на екран. В іншому випадку виведіть повідомлення
# про те, які символи повторюються. Не використовуйте множини для
# перевірки унікальності символів.
#
# Приклад:
# Введіть рядок: Python
# Усі символи у рядку унікальні.
# Введіть рядок: Hello Konal
# Символи 'l' і 'o' повторюються.

string = input("Введіть рядок: ").lower()
i = 0
symbols = []
while i < len(string):
    if string[i+1:].find(string[i]) != -1 and f"'{string[i]}'" not in symbols:
        symbols.append(f"'{string[i]}'")
    i += 1

if symbols:
    if len(symbols) == 1:
        res = symbols[0]
    else:
        res = ", ".join(symbols[:-1])
        res += f" і {symbols[-1]}"
    print(f"Символи {res} повторюються.")
else:
    print("Усі символи у рядку унікальні.")
