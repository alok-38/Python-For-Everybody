def calculate_price_after_tax(base_price, tax_rate):
    total_price = base_price + (base_price * (tax_rate / 100))
    return total_price

print(calculate_price_after_tax(50, 15))

def calculate_price_after_tax_clean(base_price, tax_rate):
    return base_price * (1 + tax_rate / 100)

print(calculate_price_after_tax_clean(50, 15))