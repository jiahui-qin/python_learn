##写一个爬虫试着爬一下琉璃神社

# -*- coding: utf-8 -*-
from urllib import request
from bs4 import BeautifulSoup

url = request.Request('http://www.hacg.cool//wp/')
url.add_header('User-Agent','Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36')
url.add_header('Refer','http://www.hacg.cool//wp/')
with request.urlopen(url) as f:
    data=f.read().decode('utf-8') ##data已经包含了这个网址的所有元素
    soup = BeautifulSoup(data, 'html.parser')
    for i in soup.find_all("h1",class_ = "entry-header"):
        print(i.a.get_text(strip=True))
    