import json

f = open("07/test.json","r")
data = json.load(f)
print(data)
print(data["11012"])
print(data["11012"]["social"])

f.close()
