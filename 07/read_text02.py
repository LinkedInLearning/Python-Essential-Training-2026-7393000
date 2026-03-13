f = open("07/emily.txt","r")
line = f.readline()
while line:
    print(line,end="")
    line = f.readline()
f.close()

