# -*- coding: utf-8 -*-
from urllib import request
from bs4 import BeautifulSoup
import re
import time

url = request.Request('http://www.acfun.cn/a/ac4272476')
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
    for article in articles:
        print(article.get_text(strip=True))
