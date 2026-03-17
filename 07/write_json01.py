import json

f = open("07/test1.json","w")
# json.dump({"11013": {"english":65,"math":77,"japanese":56,"science":65,"social":80}},f)
json.dump({"11013": {"english":65,"math":77,"japanese":56,"science":65,"social":80}},f, indent=4)
f.close()
