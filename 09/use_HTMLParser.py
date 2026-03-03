import urllib.request
from html.parser import HTMLParser

class Parser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print("開始タグ :", tag, attrs)
    def handle_endtag(self, tag):
        print("終了タグ :", tag)
    def handle_data(self, data):
        print("データ:", data)
    def handle_comment(self, comment):
        print("コメント:", comment)


res = urllib.request.urlopen("https://docs.python.org/3/whatsnew/changelog.html")
html = res.read()
str = html.decode("utf-8")
parser = Parser()
parser.feed(str)