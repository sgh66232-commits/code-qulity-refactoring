def calculate_discounted_price(price, d):
    if d > 0:
        return price - (price * d / 100)
    else:
        return price

price = 100000
discount = 20

print(calculate_discounted_price(price, discount))