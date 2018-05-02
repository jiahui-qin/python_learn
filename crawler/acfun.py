# -*- coding: utf-8 -*-
from urllib import request
from bs4 import BeautifulSoup
import re
import time
import os
def saveacfun(turl):
    url = request.Request(turl)
    url.add_header('User-Agent','Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36')
    url.add_header('Refer','http://www.acfun.cn/')
    # Host: www.acfun.cn
    # Connection: keep-alive
    # Upgrade-Insecure-Requests: 1
    # Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8
    # Accept-Encoding: gzip, deflate
    # Accept-Language: zh-CN,zh;q=0.9
    with request.urlopen(url) as f:
        data=f.read().decode('utf-8')
        soup = BeautifulSoup(data, 'html.parser')
        articles = soup.find_all('div', class_ = "article-content")
        #for article in articles:
        #    print(article.get_text(strip=True))
        url = 'http://www.acfun.cn/a/ac4272476'
        acno = url.split('/')[4]
        acname = acno + '.txt'
        for article in articles:
            if article:
                with open(acname, 'w') as savefile:
                    savefile.write(article.get_text(strip=True))##这里的文件保存到了当前的工作目录
        print(acno + '成功写入')

def checkacfun(turl):
    url = request.Request(turl)
    url.add_header('User-Agent','Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36')
    url.add_header('Refer','http://www.acfun.cn/')
    with request.urlopen(url) as f:
        data=f.read().decode('utf-8')
        soup = BeautifulSoup(data, 'html.parser')
        articles = soup.find('div', class_ = "article-content")
        #for article in articles:
        #    print(article.get_text(strip=True))
        acno = turl.split('/')[4]
        acname = acno + '.txt'
        with open(acname, 'r') as savefile:
            print(savefile.read())
            print(articles.get_text(strip=True))
            if savefile.read() == articles.get_text(strip=True):
                return('TRUE')
            else:
                return('FALSE')

print(checkacfun('http://www.acfun.cn/a/ac4272476'))
