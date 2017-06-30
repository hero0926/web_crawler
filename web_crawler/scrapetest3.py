from urllib.request import urlopen
from urllib.error import HTTPError
from bs4 import BeautifulSoup

def getTitle(url) :
    try :
        html = urlopen(url)
    except HTTPError as e :
        return None

    try :
        bsObj = BeautifulSoup(html.read(), "html.parser")
        title = bsObj.body.h1
    except AttributeError as e :
        return None
    return title

title = getTitle("http://www.naver.com")
if title == None :
    print("타이틀이 없엉!")
else :
    print(title)