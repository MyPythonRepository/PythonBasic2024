orange_price = 17.5
my_money = 101
tea_price = 14

if my_money > 100:
    print('You are a rich man')
elif my_money > orange_price:
    print("I buy orange")
elif my_money <= 0:
    print('You have no money')
else:
    # Вкладений умовний оператор if зі своїм блоком else
    if my_money > tea_price:
        print("Not orange, just tea")
    else:
        print("I buy apple")
print("The end")
