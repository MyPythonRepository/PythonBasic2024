# Даний список цілих чисел довжини 1 і більше. Написати функцію, яка повертає список
# довжини 2, що складається з першого та останнього елемента вхідного списку.
# [1, 2, 3] -> [1, 3], [7, 4, 6, 2] -> [7, 2], [5] -> [5, 5]


l = input('Введіть список чисел через пробіл: ').split()


def listik(a):
    return [a[0], a[-1]]


print(listik(l))
