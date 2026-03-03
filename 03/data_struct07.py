data1 = [1,2,3]
data2 = data1
data2[0]  = 10
print(data1)
print(data2)
print(id(data1))
print(id(data2))

data1 = [1,2,3]
data2 = data1.copy()
data2[0]  = 10
print(data1)
print(data2)
print(id(data1))
print(id(data2))