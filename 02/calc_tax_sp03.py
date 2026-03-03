"""
    calc_tax関数は本体価格と消費税率を引数として受け取り、
    税込み価格を計算して返します。
    消費税率は0.1や0.08という小数で指定してください。
    なお、消費税率を省略した場合は10%で計算します。
"""
def calc_tax(price, tax_rate = 0.1):    #tax_rateのデフォルト値は10%
    #消費税が省略された場合は10%で計算する
    tax_inc_price = price * (1 + tax_rate) 
    return tax_inc_price


print(calc_tax(1000))
print(calc_tax(1000,0.08))
