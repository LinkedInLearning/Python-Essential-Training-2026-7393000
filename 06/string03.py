str = "apple"

str1 = str.upper()
print(str1)
print(str1.lower())
print(str.swapcase())
print(str1.swapcase())

str2 = "i am proGrammer."
print(str2.capitalize()) 
print(str2.title()) 

str3 = " orange "
print(str3)
print(len(str3))
print(str3.strip())
print(len(str3.strip()))

str3 = "#orange#"
print(str3.strip("#"))
print(str3.lstrip("#"))	
print(str3.rstrip("#"))	
'''
str2 = "i am proGrammer."
print(str2.split())

splitStr = str2.split()
for str in splitStr:
    print(str)

longStr = """遠い昔
はるか銀河の
・・・
再び、銀河全体を覆いつつある
"""
print(longStr)
print(longStr.splitlines())

str2 = "i am proGrammer."
splitStr = str2.split()
print(splitStr)

str = " ".join(splitStr) 
print(str)
'''