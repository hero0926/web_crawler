from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

#regex

html = urlopen("http://www.pythonscraping.com/pages/page3.html")
bsObj = BeautifulSoup(html,"html.parser")

images = bsObj.findAll("img", {"src":re.compile("\.\.\/img\/gifts/img.*\.jpg")})

# .. /img/gifts/img 로 시작해서 .jpg로 끝남

for image in images :
    print(image["src"])