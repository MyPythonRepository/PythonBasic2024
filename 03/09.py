number_b = 100

if number_b < 5:
    number_a = 10
elif number_b == 10:
    number_a = 30
else:
    number_a = 20
print(number_a)
print('-' * 100)


if number_b < 5:
    number_a = 10
else:
    if number_b == 10:
        number_a = 30
    else:
        number_a = 20
print(number_a)
print('-' * 100)


number_a = 10 if number_b < 5 else 30 if number_b == 10 else 20
print(number_a)
