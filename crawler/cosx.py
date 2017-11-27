#cosx.org 爬虫 https://github.com/cosname/cosx.org/tree/master/content/post
from urllib import request
import time
from bs4 import BeautifulSoup
import re

def opencosx():
    cosx_artcle = []
    for page in range(41):
        cosx_url = request.Request('https://cosx.org/page' + str(page) + '/')
        cosx_url.add_header('Refer','https://coxs.org/')
        cosx_url.add_header('User-Agent','Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36')
        with request.urlopen(cosx_url) as cosx:
            cosx = cosx.read().decode('utf-8')
            cosx_soup = BeautifulSoup(cosx, 'html.parser')
            cosx_li = cosx_soup.find_all('li')
            for li in cosx_li:
                #if hasattr(li.a, 'href'):
                cosx_artcle.append(li.a['href'])
    return cosx_artcle



def openli(artcles):
    for artcle in artcles:
        if re.match(r'\d\d\d\d',artcle):
            art_url = request.Request('https://cosx.org' + artcle)
            print(art_url)
            art_url.add_header('Refer','https://cosx.org' + artcle)
            art_url.add_header('User-Agent','Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36')
            art_u = request.urlopen(art_url)
            art_u = art_u.read().decode('utf-8')
            print(art_u)
    
openli('/2017/09/interview-sanzhen-liu/')

