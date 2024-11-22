# Для списку цілих чисел потрібно знайти суму елементів із парними індексами
# [0-й, 2-й, 4-й ітд], потім перемножити цю суму на останній елемент вхідного
# масиву. Не забудьте, що перший елемент масиву має індекс 0.
# Для порожнього масиву результат завжди 0.
#
# Пояснення:
# [0, 1, 7, 2, 4, 8] => (0 + 7 + 4) * 8 = 88
# Приклад:
# [1, 3, 5] => 30
# [6] => 36
# [] => 0
#
# Для перевірки коректності роботи Вашого коду використовуйте приклади вище.
# Робити запит на введення даних від користувача не потрібно.


a = [0, 7, 9, 12, -1, 100]

b = 0
for i in range(len(a)):
    if i % 2 == 0:
        b += a[i]
print(b * (a[-1] if len(a) != 0 else 0))
