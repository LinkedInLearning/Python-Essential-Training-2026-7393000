import csv

f = open("test.csv", "w")

writer = csv.writer(f, lineterminator='\n')
writer.writerow([1,"北海道",1000000])
writer.writerows([[2,"秋田",670000],[3,"青森",877000]])

f.close()
