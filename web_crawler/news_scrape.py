from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
from slacker import Slacker
import requests

# okky 게시물을 크롤링
okky = urlopen("https://okky.kr/")

# ITWORLD에서 메인기사를 크롤링
it_world = urlopen("http://www.itworld.co.kr/")

# github 트렌딩
github = urlopen("https://github.com/explore")


# 공통모듈

## 제목얻기

def get_title_from_bs4(obj):
    return obj.text


# 사이트별 개별모듈

## okky 에서 좋은 글들을 크롤링 하기

def get_link_from_okky():
    okky_news = BeautifulSoup(okky, "html.parser")
    
    okkynews = {}
    
    for thing in okky_news.find_all("div", {"class": "article-middle-block"}):
        for h5 in thing.find_all("h5"):
            for link in h5.find_all("a", href=True):
                okky_url = "https://okky.kr" + link["href"]
                okky_title = get_title_from_bs4(link)
                
                okkynews[okky_title] = okky_url
    
    return okkynews


## ITNEWS 에서 메인 기사들을 크롤링 하기


def get_link_from_itworld():
    world_news = BeautifulSoup(it_world, "html.parser")
    
    itnews = {}
    
    for thing in world_news.find_all("div", {"class": "headline_news_contents"}):
        for link in thing.find_all("a", href=True):
            world_url = "http://www.itworld.co.kr" + link["href"]
            world_title = get_title_from_bs4(link)
            
            itnews[world_title] = world_url
    
    return itnews


## github에서 최신 오픈소스를 크롤링 하기

def get_link_from_github():
    git_trend = BeautifulSoup(github, "html.parser")
    
    gittrending = {}
    
    for thing in git_trend.find_all("div", {"id": "explore-trending"}):
        
        for link in thing.find_all("a", {"class": "h4"}):
            git_link = "https://github.com" + link["href"]
        
        for title in thing.find_all("p"):
            git_title = title["title"]
            
            gittrending[git_title] = git_link
    
    return gittrending


####################################################

okky = get_link_from_okky()
itworld = get_link_from_itworld()
github = get_link_from_github()

okky_title = random.choice(list(okky.keys()))
okky_link = okky.get(okky_title)

it_title = random.choice(list(itworld.keys()))
it_link = itworld.get(it_title)

git_title = random.choice(list(github.keys()))
git_link = github.get(git_title)

######################################################

attachments = []
attachments.append(
    {
        "pretext": "깃허브 핫 오픈소스",
        "title": git_title,
        "text": git_link,
        
        "mrkdwn_in": [
            "text",
            "pretext"
        ]
    })
attachments.append({
    "pretext": "OKKY 기술 게시물",
    "title": okky_title,
    "text": okky_link,
    
    "mrkdwn_in": [
        "text",
        "pretext"
    ]
})
attachments.append({
    "pretext": "IT NEWS",
    "title": it_title,
    "text": it_link,
    
    "mrkdwn_in": [
        "text",
        "pretext"
    ]
})

######################################################

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
slack.chat.post_message('#general', '봇 메시징 테스트', attachments=attachments)
