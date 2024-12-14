# Напишіть програму, яка запитує у користувача рядок і визначає, чи є вiн
# панграмою. Панграма - це фраза, що містить усі літери алфавіту. Програма
# повинна ігнорувати регістр літер та пробіли під час перевірки панграми.
# Виведіть відповідне повідомлення на екран за допомогою команди print.
# Розв'язати задачу для латиниці.
#
# Приклад:
# Введіть рядок: The quick brown fox jumps over the lazy dog
# Рядок є панграмою.


alphabet = "ABCDEFGIJHKLMNOPQRSTUVWXYZ"
s = input("Введіть рядок:")
i = 0
while i < len(alphabet):
    if alphabet[i] in s.upper():
        i += 1
    else:
        print("Рядок не є панграмою")
        break
else:
    print("Рядок є панграмою")
