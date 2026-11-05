def calculate_discounted_price(price, discount_percent):
    if discount_percent > 0:
        return price - (price * discount_percent / 100)
    else:
        return price

price = 100000
discount = 20

print(calculate_discounted_price(price, discount))