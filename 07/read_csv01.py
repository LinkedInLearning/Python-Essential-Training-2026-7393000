import csv

f = open("07/fruits.csv","r")
reader = csv.reader(f)
for row in reader:
    for col in row:
        print(col,end=",")

f.close()
