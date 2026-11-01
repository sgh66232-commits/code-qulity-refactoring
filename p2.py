def calculate_discounted_price(price, discount_percent):
    if discount_percent <= 0:
        return price

    discount_amount = price * discount_percent / 100

    return price - discount_amount


product_price = 100000
discount_percent = 20

final_price = calculate_discounted_price(
    product_price,
    discount_percent
)

print(final_price)