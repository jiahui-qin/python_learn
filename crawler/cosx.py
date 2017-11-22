#cosx.org 爬虫 https://github.com/cosname/cosx.org/tree/master/content/post
from urllib import request
import time
from bs4 import BeautifulSoup
import re

def opencosx():
    cosx_artcle = []
    for page in range(1, 42):##应该是42
        cosx_url = request.Request('https://cosx.org/page' + str(page) + '/')
        cosx_url.add_header('Refer','https://coxs.org/')
        cosx_url.add_header('User-Agent','Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36')
        with request.urlopen(cosx_url) as cosx:
            print('正在读取第' + str(page) + '页')
            cosx = cosx.read().decode('utf-8')
            cosx_soup = BeautifulSoup(cosx, 'html.parser')
            cosx_li = cosx_soup.find_all('li')
            for li in cosx_li:
                #if hasattr(li.a, 'href'):
                cosx_artcle.append(li.a['href'])
            time.sleep(1)
    with open('cosx_file.txt', 'w') as savefile:
        savefile.write(str(cosx_artcle))##这里的文件保存到了当前的工作目录
        print('成功写入')
    return cosx_artcle

#opencosx()

def openli(data):
    result = []
    with open('cosx_file.txt', 'r') as data:
        for line in data:
            result.append(list(map(str,line.split(','))))
        results = result[0]

    for article in results:
        if re.match(r'.\d\d\d\d', article[2:-1]):
            article_url = 'https://cosx.org'+article[2:-1]
            cosx_url = request.Request(article_url)
            cosx_url.add_header('Refer',article_url)
            cosx_url.add_header('User-Agent','Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36')
            with request.urlopen(cosx_url) as cosx:
                cosx = cosx.read().decode('utf-8')
                cosx_soup = BeautifulSoup(cosx, 'html.parser')
                cosx_main = cosx_soup.find_all('main')
                print(cosx_main)

