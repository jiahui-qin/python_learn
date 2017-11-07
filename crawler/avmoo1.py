from urllib import request
from bs4 import BeautifulSoup
import re
data = request.Request("https://avmo.club/cn/movie/6b0g")
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
    print(Idcode.get_text())