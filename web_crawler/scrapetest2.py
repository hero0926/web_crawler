from urllib.request import urlopen
from bs4 import BeautifulSoup
from urllib.request import HTTPError


try :
    #404, 500 에러처리
    html = urlopen("http://www.pythonscraping.com/pages/page1.html")
except HTTPError as e :
    # null 반환, break문 실행 등, 기타 다른 방법 사용
    print(e)
else :
    #프로그램 계속 실행
    bsObj = BeautifulSoup(html.read(), "html.parser")
    print(bsObj.h1)


# tag가 없는 경우의 에러 처리법

try :
    badContent = bsObj.nonExistingTag.anotherTag

except AttributeError as e :
    if badContent = None : #태그가 없을 때
        print("태그가 없졍")
    else :
        print(badContent)
