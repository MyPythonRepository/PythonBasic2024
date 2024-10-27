user_input = int(input('Please enter a 4-digit number: '))

print(user_input // 1000)
print(user_input % 1000 // 100)
print(user_input % 100 // 10)
print(user_input % 10)

'''digit1, rest = divmod(user_input, 1000)

print(digit1)

digit2, rest = divmod(rest, 100)

print(digit2)

digit3, digit4 = divmod(rest, 10)

print(digit3)
print(digit4)'''