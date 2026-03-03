str = "a long time ago in a galaxy far far away"

str1 = str.replace("galaxy","island")
print(str1)
str2 = str1.replace("far","near")
print(str2)

str3 = str1.replace("far","near", 1)
print(str3)

str1 = str.replace("island","Japan")
print(str1)

str1 = str.replace("galaxy","ギャラクシー")
print(str1)

str2 = str1.replace("ギャラクシー","銀河")
print(str2)
