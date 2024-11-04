# Написати програму, яка переміщає всі нулі у кінець списку.
#
# Ваше завдання — змінити список так, щоб усі нулі опинилися
# наприкінці списку.
#
# Порядок ненульових чисел має зберегтися!
#
# Приклад:
#
# [0, 1, 0, 12, 3] -> [1, 12, 3, 0, 0]
# [0] -> [0]
# [1, 0, 13, 0, 0, 0, 5] -> [1, 13, 5, 0, 0, 0, 0]
# [9, 0, 7, 31, 0, 45, 0, 45, 0, 45, 0, 0, 96, 0] ->
# -> [9, 7, 31, 45, 45, 45, 96, 0, 0, 0, 0, 0, 0, 0]
#
# Для перевірки коректності роботи Вашого коду використовуйте приклади вище.
# Робити запит на введення даних від користувача не потрібно.

list1 = [0, 1, 0, 12, 3]

non_zero_elements = [i for i in list1 if i != 0]

zero_count = list1.count(0)

list1 = non_zero_elements + [0] * zero_count

print(list1)
