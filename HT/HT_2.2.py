"""На запит від програми, користувач вводить 5-ти значне ціле, позитивне число.
Вам необхідно "перевернути" цє число задом наперед, тобто щоб у результаті
вийшло теж 5-ти значне число, але із зворотною послідовністю цифр.

Вам не потрібно перевіряти, що користувач ввів правильне число -
зробіть вигляд, що користувач завжди вводить 5 значне число.
Тобто введене користувачем число завжди складатиметься з 5 цифр.

Якщо користувач ввів інше число, це проблема користувача,
а не вашої програми. Використовуються лише цілі числа.

Для розв'язання задачі потрібно використовувати лише той зріз даних,
який було пройдено. Тобто використовувати строки не можна.

Приклади:

Користувач ввів: 12345 - на екрані відображається: 54321

Користувач ввів: 37568 - на екран відображається: 86573"""

user_input = int(input('Please enter a 5-digit number: '))

digit1 = user_input % 10
digit2 = user_input // 10 % 10
digit3 = user_input // 100 % 10
digit4 = user_input // 1000 % 10
digit5 = user_input // 10000

print(digit1)
print(digit2)
print(digit3)
print(digit4)
print(digit5)
print()

reversed_user_input = digit1 * 10000 + digit2 * 1000 + digit3 * 100 + digit4 * 10 + digit5

print(reversed_user_input)