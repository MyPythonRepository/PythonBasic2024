# Написати на Python програму, яка дізнається погоду у заданому місті.
# В інтернеті велика кількість сервісів, що "віддають" погоду через т.зв.
# REST API. Працюємо із сервісом Weather API. (Цей сервіс безкоштовний, але
# потрібна реєстрація і є обмеження на кількість запитів від одного користувача
# в день). Зайдите за посиланням: https://www.weatherapi.com/  зареєструйтеся,
# та скопіюйте і збережіть згенерований API Key, він стане в нагоді пізніше.
# Інтерактивний експлорер: https://www.weatherapi.com/api-explorer.aspx
# для того, щоб зрозуміти у якому вигляді треба робити запроси і у якому вигляді
# приходе відповідь.
#
# Перш, ніж писати програму, потрібно зареєструватися на сайті та знайти API Key
# який потрібно відправляти з кожним запитом на сервер.
# Для того, щоб робити запити треба використовувати метод get() модуля requests.
# Його треба з початку встановити за допомогою pip install requests
