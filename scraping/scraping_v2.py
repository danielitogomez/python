from urllib.request import urlopen
from urllib.error import HTTPError
from bs4 import BeautifulSoup


def getURL(url):
    try:
        html = urlopen(url)
    except HTTPError as e:
        return None
    try:
        obj = BeautifulSoup(html.read(), "lxml")
        text = obj.body.h1
    except AttributeError as e:
        return None
    return text


text = getURL("https://docs.python.org/3/library/sys.html")
if text == None:
    print("Text could not be found")
else:
    print(text)