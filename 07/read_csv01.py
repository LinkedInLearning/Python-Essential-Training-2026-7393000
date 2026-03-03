import csv

f = open("fruits.csv","r")
reader = csv.reader(f)
for row in reader:
    for col in row:
        print(col,end=",")

f.close()