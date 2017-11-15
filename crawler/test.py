##爬到一个网站现在看起来不是很难，现在先把网站保存到本地然后开始学习吧from urllib import request
from bs4 import BeautifulSoup
from time import sleep
import re
from urllib import request
import gzip
def moviedownload(idcode):
    Dowpage = request.Request('https://btso.pw/search/' + idcode)
    Dowpage.add_header('User-Agent','Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36')
    Dowpage.add_header('Refer', 'https://btso.pw/search/' + idcode)
    Dowpage.add_header('Accept-Encoding', 'gzip, deflate, br')
    Dowpage.add_header('Upgrade-Insecure-Requests', '1')
    Dowpage.add_header('Accept-Language', 'zh-CN,zh;q=0.8')

    with request.urlopen(Dowpage) as dpage:
        dpage = dpage.read()
        dpage = gzip.decompress(dpage)
        #print(dpage)
        dpage = dpage.decode('utf-8')
        #print(dpage)
        dsoup = BeautifulSoup(dpage, 'html.parser')
        flag = dsoup.find('div', text = "Torrent Description")
        if flag:
            print("Dowland page: "+'https://btso.pw/search/' + idcode)
        else:
            print("btso暂无" + idcode + '下载地址')

moviedownload('teens')