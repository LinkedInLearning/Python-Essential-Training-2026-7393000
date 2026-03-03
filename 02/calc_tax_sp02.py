def calc_tax(price, tax_rate):
    tax_inc_price = price * (1 + tax_rate)
    return tax_inc_price


print(calc_tax(1000,0.1))
print(calc_tax(1000,0.08))  