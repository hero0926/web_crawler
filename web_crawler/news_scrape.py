from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
from slacker import Slacker
import requests

# IT뉴스에서 IT기사를 크롤링
it_news = urlopen("http://www.itnews.or.kr/")

# okky 게시물을 크롤링
okky = urlopen("https://okky.kr/")

# 제이어쩌고 뉴스를 크롤링

# 공통모듈

## 제목얻기

def get_title_from_bs4(obj) :
    return obj.text


# 사이트별 개별모듈

## IT뉴스에서 지금 트렌드 중인 기사 크롤링 하기

def get_link_from_hot_trending() :
    hot_trending = BeautifulSoup(it_news, "html.parser")
    for thing in hot_trending.find("div", {"class":"td-trending-now-wrapper"}).children:
        for link in thing.find_all("a", href=True) :

            # print("가져온 내용", link)

            hot_url = link["href"]
            if len(hot_url) > 10 :
                hot_title = get_title_from_bs4(link)
                if hot_title:
                    print("가져온 제목", hot_title)
                print("가져온 주소", hot_url)

## okky 에서 좋은 글들을 크롤링 하기

def get_link_from_okky() :
    okky_news = BeautifulSoup(okky, "html.parser")
    for thing in okky_news.find_all("div", {"class":"article-middle-block"}) :
        for h5 in thing.find_all("h5") :
            for link in h5.find_all("a", href=True) :
                
                okky_url = "https://okky.kr"+link["href"]
                okky_title = get_title_from_bs4(link)

                print("가져온 제목", okky_title)
                print("가져온 주소", okky_url)
                
# get_link_from_hot_trending()
get_link_from_okky()

# 봇 할일
# 하루 x회 y시마다 자동 크롤링 하여 투고?
# 아니면 유저가 특정 커맨드 입력시 크롤링 하여 투고?
# 어디 뉴스 어디 기사를 얼만큼?
# 봇커맨드
# 기사사이트 종류 기사 > 입력하면 거기 내용이 나오는 것
# 예를들어 IT뉴스 트렌드 기사 > get_link_from_hot_trending 나옴
# IT뉴스 > IT뉴스 메인 기사

# 쓰는 툴
# 파이썬, Bs4, 슬랙커, heroku 아님 애저(서버용)


# 슬랙에 연결하기

# 포스팅할 슬랙페이지의 API 토큰
slack = Slacker('xoxb-217203473585-3nnxenJ7mIXmhIXLdEHuunIT')

# 보낼 내용
attachments = []

attachments.append({
    "fallback": "알림 메시지",
    
    "title": "제목",
    
    "title_link": "연결할 링크",
    
    "text": """
    보여줄 내용
    와! 내용이다!
    """,

    "color": "#7CD197",
})

# 보내기
# 지금 사내에서는 requests.exceptions.SSLError: ("bad handshake: Error([('SSL routines', 'ssl3_get_server_certificate', 'certificate verify failed')],)",)
# 에러가 뜨는데 다른 컴퓨터에선 어떨지 모르겠네요...

""" conda remove certifi
    conda install certifi
    conda update --all 로 certifi 업데이트 해보시고
    conda config --set ssl_verify false 로 ssl 기능을 꺼보세요...

"""
# requests.get('https://api.sidecar.io', verify = 'mycerts.pem')
# 위 방법으로 할 시 mycerts.pem을 찾지 못했다 나옴

# certificate verify failed (SSLERROR) 발생중
# slack.chat.post_message('#general', '봇 메시징 테스트', attachments=attachments)