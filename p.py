def calc(p, d):
    if d > 0:
        return p - (p * d / 100)
    else:
        return p

price = 100000
discount = 20

print(calc(price, discount))