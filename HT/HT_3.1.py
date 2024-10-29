# Найпростіший калькулятор
# Програма має виконувати прості математичні дії (+, -, *, /).
# Користувачеві пропонується по черзі ввести числа та дію над цими числами,
# а програма, виходячи з дії, обчислює та друкує результат.
#
# Зробити перевірку на те, що при діленні дільник не дорівнює 0!

number1 = float(input('Please enter the first number: '))

number2 = float(input('Please enter the second number: '))

operator = input('Please enter one of the operators: +, -, * or /: ')

if operator == "+":
    result = number1 + number2
    print('Result: ', result)
elif operator == "-":
    result = number1 - number2
    print('Result: ', result)
elif operator == "*":
    result = number1 * number2
    print('Result: ', result)
elif operator == "/":
    if number2 != 0:
        result = number1 / number2
        print('Result: ', result)
    else:
        print('Error: Division by zero is impossible!')
else:
    operator = input('Invalid operator. Please enter only one of the operators: +, -, * or /, nothing else: ')

    if operator == "+":
        result = number1 + number2
        print('Result: ', result)
    elif operator == "-":
        result = number1 - number2
        print('Result: ', result)
    elif operator == "*":
        result = number1 * number2
        print('Result: ', result)
    elif operator == "/":
        if number2 != 0:
            result = number1 / number2
            print('Result: ', result)
        else:
            print('Error: Division by zero is impossible!')
