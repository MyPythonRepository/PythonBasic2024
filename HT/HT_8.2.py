# Ваше завдання – написати функцію is_palindrome, яка перевірятиме, чи є рядок
# паліндромом. Паліндромом - це такий рядок, який читається однаково зліва
# направо і зправа наліво без урахування знаків пунктуації та розмірності букв.
# Функція приймає на вхід рядок, та повертає булеве значення True або False


def is_palindrome(text):
    new_text = "".join(i.lower() for i in text if i.isalnum())
    return new_text == new_text[::-1]


assert is_palindrome('A man, a plan, a canal: Panama') == True, 'Test1'
assert is_palindrome('0P') == False, 'Test2'
assert is_palindrome('a.') == True, 'Test3'
assert is_palindrome('aurora') == False, 'Test4'
print("ОК")
