from urllib import request
from bs4 import BeautifulSoup
from time import sleep
import re

def movieinfo(url):
    data = request.Request(url)
    data.add_header('User-Agent','Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36')
    data.add_header('Upgrade-Insecure-Requests',1)
    with request.urlopen(data) as f:
        data=f.read().decode('utf-8')
        soup = BeautifulSoup(data, 'html.parser')
        actors = soup.find_all('a', class_ = 'avatar-box')
        print('actors:', end=' ')
        for actor in actors:
            print(actor.get_text(strip=True), end=' ')
        print('\n',end='')
        tags = soup.find_all('span', class_ = 'genre')
        print('tags:', end=' ')
        for tag in tags:
            print(tag.get_text(strip = True),end=' ')
        print('\n',end='')
        factory = soup.find('a', href=re.compile("studio"))
        print("producer:" + factory.get_text(strip=True))
        Idcode = soup.find('span', style="color:#CC0000;")
        moviedownload(Idcode.get_text())

def moviedownload(idcode):
    Dowpage = request.Request('https://btso.pw/search/' + idcode)
    Dowpage.add_header('User-Agent','Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36')
    Dowpage.add_header('Refer', 'https://btso.pw/search/' + idcode)
    Dowpage.add_header('Accept-Encoding', 'gzip, deflate, br')
    Dowpage.add_header('Upgrade-Insecure-Requests', '1')
    Dowpage.add_header('Accept-Language', 'zh-CN,zh;q=0.8')

    with request.urlopen(Dowpage) as dpage:
        dpage = dpage.read().decode('utf-8')
        dsoup = BeautifulSoup(dpage, 'html.parser')
        flag = dsoup.find('div', text = "Torrent Description")
        if flag:
            print("Dowland page: "+'https://btso.pw/search/' + idcode)
        else:
            print("btso暂无" + idcode + '下载地址')

        
data = request.Request("https://avmo.club/cn/search/VENUS/page/3")
data.add_header('User-Agent','Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36')
data.add_header('Referer','https://avmo.club/cn')
data.add_header('Upgrade-Insecure-Requests',1)
with request.urlopen(data) as f:
    data=f.read().decode('utf-8')
    soup = BeautifulSoup(data, 'html.parser')
    for movie in soup.find_all('div', class_="photo-info"):
        for text in movie.stripped_strings:
            if text != '/':
                print(text)
        #print(movie.parent.parent.a['href'])
        movieinfo(movie.parent.parent.a['href'])
        print()

