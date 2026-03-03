import datetime


dt = datetime.datetime.now()
print(dt.strftime("%Y/%m/%d"))
print(dt.strftime("%Y/%m/%d(%w)"))  
print(dt.strftime("%Y/%m/%d(%A)"))
print(dt.strftime("%y/%m/%d(%a)"))
print(dt.strftime("%Y/%m/%d %H:%M:%S"))