from urllib import request
from bs4 import BeautifulSoup
from time import sleep
import re
import gzip
def movieinfo():
    for i in range(1,207):
        url = 'https://javlog.com/cn/actresses/page/' + str(i)
        data = request.Request(url)
        data.add_header('User-Agent','Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36')
        data.add_header('Upgrade-Insecure-Requests',1)
        with request.urlopen(data) as f:
            data=f.read().decode('utf-8')
            soup = BeautifulSoup(data, 'html.parser')
            actors = soup.find_all('div', class_ = 'item')
            for actor in actors:
                link = actor.find('img')['src']
                actor = actor.find('div', class_ = "photo-info").get_text("|", strip=True)
                filename = 'av_actress/photo/' + actor + '.jpg'
                download(link, filename)


def download(url, name):
    if(url==None):
        pass
    photourl = request.Request(url)
    photourl.add_header('User-Agent','Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36')
    photourl.add_header('Upgrade-Insecure-Requests',1)
    result=request.urlopen(photourl)#打开链接  
    #print result.getcode()  
    if(result.getcode()!=200):#如果链接不正常，则跳过这个链接  
        pass  
    else:  
        data=result.read()#否则开始下载到本地  
        with open(name, "wb") as code:  
            code.write(data)  
            code.close()  

movieinfo()
