f = open("07/emily.txt","r")
lines = f.readlines()
f.close()
for line in lines:

    print(line,end="")
