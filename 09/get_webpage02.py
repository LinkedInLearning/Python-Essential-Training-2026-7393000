import urllib.request


try:
    res = urllib.request.urlopen("https://docs.python.org/ja/31/")
except urllib.error.HTTPError as e:
    print(f"HTTPError: {e.code}")
except urllib.error.URLError as e:
    print(f"URLError: {e.reason}")
else:
    print(res.status)
    html = res.read()
    str = html.decode('utf-8')
    print(str)
    res.close()