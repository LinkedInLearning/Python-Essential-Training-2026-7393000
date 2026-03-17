import json
try:
    f = open("07/test.json","r")
    data = json.load(f)
    print(data)
    print(data["11012"])
    print(data["11012"]["scalar"])
    f.close()
except FileNotFoundError as ex1:
    print(ex1)
    print(ex1.errno)
    print(ex1.filename)
except KeyError as ex2:
    print(ex2)
except:
    print("例外が発生しました")
