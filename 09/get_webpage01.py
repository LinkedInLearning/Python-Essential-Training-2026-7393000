import urllib.request


res = urllib.request.urlopen("https://docs.python.org/ja/3/")
print(res.getcode())
print(res.info())   
html = res.read()
str = html.decode('utf-8')
print(str)