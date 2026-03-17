import json
try:
    f = open("07/test.json","r")
    data = json.load(f)
    print(data)
    print(data["11012"])
    print(data["11012"]["socila"])
    f.close()
except FileNotFoundError:
    print("ファイルが存在しません")
except KeyError:
    print("キーが存在しません")
except:
    print("例外が発生しました")
