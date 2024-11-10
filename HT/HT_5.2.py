# Модифікувати калькулятор таким чином,
# щоб він працював доти, доки користувач цього хоче.
# Тобто, потрібно робити запит до користувача на
# продовження роботи калькулятора після кожного обчислення -
# якщо користувач ввів yes (можна просто y), то нове обчислення,
# інакше - закінчення роботи.

while True:
    number1 = float(input("Please enter the first number: "))
    number2 = float(input("Please enter the second number: "))
    operator = input("Please enter one of the operators: +, -, * or /: ")

    if operator == "+":
        result = number1 + number2
        print("Result: ", result)
    elif operator == "-":
        result = number1 - number2
        print("Result: ", result)
    elif operator == "*":
        result = number1 * number2
        print("Result: ", result)
    elif operator == "/":
        if number2 != 0:
            result = number1 / number2
            print("Result: ", result)
        else:
            print("Error: Division by zero is impossible!")
    else:
        print("Invalid operator!")

    continue_calculation = input("Would you like to perform another calculation? If yes, please enter 'y': ").lower()
    if continue_calculation != "y":
        print("Have a great day!")
        break
