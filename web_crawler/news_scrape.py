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

# 봇커맨드
# 기사사이트 종류 기사 > 입력하면 거기 내용이 나오는 것
# 예를들어 IT뉴스 트렌드 기사 > get_link_from_hot_trending 나옴
# IT뉴스 > IT뉴스 메인 기사

# 봇 할일
# 하루 x회 y시마다 자동 크롤링 하여 투고
# 어디 뉴스 어디 기사를 얼만큼?

# 쓰는 툴
# 파이썬, Bs4, 슬랙API, heroku 아님 애저(서버용)
