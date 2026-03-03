i = 0
while i < 5:
    print(i)
    i += 1

print("loop end:" + str(i))

j = 1
while True:
    print(j)
    if j % 7 == 0:
        break
    j += 1
    
print("loop exit" + str(j))