# Користувач вводить рядок, Ваше завдання –
# перетворити рядок на hashtag.
# Декілька правил:
# 1. ніяких символів з набору string.punctuation не повинно бути,
# у тому числі й пробілів;
# 2. підсумкова довжина hashtag має бути не більше 140 символів.
# 3. кожне слово починається з великої літери.
# 4. якщо довжина фінішного хештегу більше 140 символів -
# обрізати підсумковий рядок до 140 символів.
# Приклади:
# 'Python Community' -> #PythonCommunity
# 'i like python community!' -> #ILikePythonCommunity
# 'Should, I. subscribe? Yes!' -> #ShouldISubscribeYes


import string

user_input = input("Please enter a string: ")

cleaned_input = "".join(i for i in user_input if i not in string.punctuation).split()

hashtag = "#" + "".join(i.capitalize() for i in cleaned_input)

final_hashtag = hashtag[:140]

print(final_hashtag)
