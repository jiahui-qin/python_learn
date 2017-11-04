##写一个爬虫试着爬一下琉璃神社

# -*- coding: utf-8 -*-
from urllib import request
from bs4 import BeautifulSoup
import re
import time
url = request.Request('http://www.hacg.cool//wp/')
url.add_header('User-Agent','Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36')
url.add_header('Refer','http://www.hacg.cool//wp/')
with request.urlopen(url) as f:
    data=f.read().decode('utf-8') ##data已经包含了这个网址的所有元素
    soup = BeautifulSoup(data, 'html.parser')
    for thetitle in soup.find_all("h1", class_="entry-title"):
        print(thetitle.get_text(strip=True))
        tags = thetitle.parent.parent.footer
        for tag in tags.find_all("span", class_ = "tag-links"):
           print(tag.get_text(strip=True))
        #print(thetitle.a['href'])##接下来就是进入href然后获取神秘代码
        article = request.Request(thetitle.a['href'])
        article.add_header('User-Agent','Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36')
        article.add_header('Refer',thetitle.a['href'])
        with request.urlopen(article) as art:
            print("以下为下载地址：")
            art_de=art.read().decode('utf-8')
            art_de = BeautifulSoup(art_de, 'html.parser')
            main = art_de.find("div", class_ = "entry-content")
            for tag in main.find_all(text = re.compile(r'[0-9a-zA-Z]{15,60}')):
                print(re.sub(r'[0-9a-zA-Z]{15,60}','',tag), end = '')
                print('magnet:?xt=urn:btih:' + re.search('([0-9a-zA-Z]{15,60})',tag).group())
            print()
            time.sleep(1)