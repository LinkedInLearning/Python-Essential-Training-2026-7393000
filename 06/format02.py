str1 = "みかん"
print(f"好きな食べ物は{str1}です")
str2 = "りんご"
print(f"好きな食べ物は{str2}と{str1}です")
print(f"好きな食べ物は{str1}と{str2}です")

val1 = 1560000
print(f"今月の売上は{val1:,}円です")
print(f"今月の売上は{val1:>12,}円です")

quantity = 125
price = 13600
print(f"りんごは{quantity:,}個売れました。売上は{price:,}円です") 

val2 = 128
print(f"10進数{val2:d}は、2進法では{val2:b}、8進法では{val2:o}、16進法では{val2:x}です")