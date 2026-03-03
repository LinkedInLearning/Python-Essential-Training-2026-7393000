f = open("emily.txt","r")
lines = f.readlines()
f.close()
for line in lines:
    print(line,end="")