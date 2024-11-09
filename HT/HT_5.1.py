# Користувач вводить рядок.
# Ваше завдання - перевірити, чи може цей рядок бути ім'ям змінної.
# Змінна не може:
# починатися з цифри
# містити великі літери,
# пробіл і знаки пунктуації (взяти можна тут string.punctuation),
# окрім нижнього підкреслення "_".
# бути жодним із зареєстрованих слів.
# При цьому повне ім'я змінної повинно складатись
# не більш чим з одного нижнього підкреслення "_".
# Список зареєстрованих слів можна взяти із keyword.kwlist.
# У результаті перевірки на друк виводиться або True,
# якщо таке ім'я змінної допустимо, або False - якщо ні.
# Приклади імен змінних та результат перевірки
# (=> на друк виводити не потрібно :))

import string
import keyword

new_punctuation = string.punctuation.replace("_", "")

user_input = input("Please enter a string: ")

if not user_input[0].isdigit():
    if user_input.islower() or user_input == "_":
        if " " not in user_input and not any(i in new_punctuation for i in user_input):
            if user_input not in keyword.kwlist:
                if user_input.count("_") <= 1:
                    print(True)
                else:
                    print(False)
            else:
                print(False)
        else:
            print(False)
    else:
        print(False)
else:
    print(False)
