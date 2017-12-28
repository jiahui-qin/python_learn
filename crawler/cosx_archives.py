# -*- coding: utf-8 -*-
from urllib import request
import time
from bs4 import BeautifulSoup
import re
import pymysql

def create_table():
    #创建了一个table用来储存信息
    db= pymysql.connect(host="localhost",user="root", password="1234", db = 'cosx')
    cursor = db.cursor()
    cursor.execute("create table article(\
        id int unsigned not null auto_increment primary key,\
        time char(8) not null, \
        title char(50) not null, \
        keyword char(100) not null, \
        author char(30) not null, \
        address char(70) not null);")  
    db.commit()
    db.close()
    print('数据库创建成功！')

def get_article(url):
    url = 'https://cosx.org' + url
    url = request.Request(url)
    url.add_header('Refer','https://coxs.org/')
    url.add_header('User-Agent','Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36')
    with request.urlopen(url) as article:
        article = article.read().decode('utf-8')
        article_soup = BeautifulSoup(article, 'lxml')
        target = article_soup.find('div', class_ = 'article-meta')
        title = article_soup.find('span', class_ = 'title').get_text()
        author = article_soup.find('h3', class_ = 'author').get_text()
        keyword = target.p.get_text()
        return [title,author, keyword]

def main():
    create_table()
    cosx_url = request.Request('https://cosx.org/archives/')
    cosx_url.add_header('Refer','https://coxs.org/')
    cosx_url.add_header('User-Agent','Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36')
    db= pymysql.connect(host="localhost",user="root", password="1234", db = 'cosx')
    cursor = db.cursor()
    with request.urlopen(cosx_url) as f:
        f = f.read().decode('UTF-8')
        fsoup = BeautifulSoup(f, 'lxml')
        cosx = fsoup.find('main')
        articles = cosx.find_all('li')
        for article in articles:
            print(article)
            url = article.a['href']
            get_a = get_article(url)
            title = get_a[0]
            author = get_a[1][0:-1]
            keyword = get_a[2][4,-1]
            time = article.span.get_text()
            address = article.a['href']
            cursor.execute("insert into article values[NULL, time, title, keyword, author, address];")
            db.commit()
            time.sleep(1)
    db.close()



main()






