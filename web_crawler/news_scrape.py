from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

# IT뉴스에서 IT기사를 크롤링
html = urlopen("http://www.itnews.or.kr/")

# 공통모듈

## 제목얻기

def get_title_from_bs4(obj) :
    return obj.text

# 사이트별 개별모듈

## IT뉴스에서 지금 트렌드 중인 기사 크롤링 하기

def get_link_from_hot_trending() :
    hot_trending = BeautifulSoup(html, "html.parser")
    for thing in hot_trending.find("div", {"class":"td-trending-now-wrapper"}).children:
        for link in thing.find_all("a", href=True) :

            #print("가져온 내용", link)

            hot_url = link["href"]
            if len(hot_url) > 10 :
                hot_title = get_title_from_bs4(link)
                if hot_title:
                    print("가져온 제목", hot_title)
                print("가져온 주소", hot_url)


get_link_from_hot_trending()