import urllib.request
from html.parser import HTMLParser

class Parser(HTMLParser):
    def __init__(self):
        super().__init__()
        #「LI」とは「list item」の略で、リストの項目を表示するために使用するタグです。
        self.li = False
    def handle_starttag(self, tag, attrs):
        if tag == "li":
            self.li = True
    def handle_data(self, data):
        if self.li:
            print("List item:{}".format(data))
            self.li = False


def main():
    res = urllib.request.urlopen("https://docs.python.org/3/whatsnew/changelog.html")
    html = res.read()
    str = html.decode("utf-8")
    parser = Parser()
    parser.feed(str)


if __name__ == '__main__':
    main()