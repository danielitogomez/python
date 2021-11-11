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
        text = obj.body.div
    except AttributeError as e:
        return None
    return text


text = getURL("https://www.sii.cl/valores_y_fechas/dolar/dolar2021.htm")
if text == None:
    print("Text could not be found")
else:
    print(text)
