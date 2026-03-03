data1 = 10
def func1():
    global data1
    data1 += 10
    print(data1)


func1()
print(data1)