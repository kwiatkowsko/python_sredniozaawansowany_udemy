price = 123
bonus = 23
bonus_granted = True

if bonus_granted:
    price -= bonus

print(price)

if bonus_granted: price -= bonus, print(price)



rating = 5
print('very good' if rating == 5 else 'good' if rating == 4 else 'weak')
