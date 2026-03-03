str1 = "みかん"
print("好きな食べ物は{}です".format(str1))
str2 = "りんご"
print("好きな食べ物は{0}と{1}です".format(str1,str2))
print("好きな食べ物は{1}と{0}です".format(str1,str2))

print("今月の売上は{:,}円です".format(1560000))
print("今月の売上は{:>12,}円です".format(1560000))

quantity = 125
price = 13600
print("りんごは{0:,}個売れました。売上は{1:,}円です".format(quantity,price)) 

print("10進数{0:d}は、2進法では{0:b}、8進法では{0:o}、１６進法では{0:x}です".format(128))