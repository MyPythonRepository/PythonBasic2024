import string
import keyword

new_punctuation = string.punctuation.replace("_", "")

user_input = input("Please enter a string: ")

result = False

if not user_input[0].isdigit():
    if user_input.islower() or user_input == "_":
        if " " not in user_input and not any(i in new_punctuation for i in user_input):
            if user_input not in keyword.kwlist:
                if user_input.count("_") <= 1:
                    result = True
print(result)
