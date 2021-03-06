#模拟浏览器发送get请求，需要使用request对象
#往request对象添加http头，就可以把请求伪装成浏览器
##查看报头(header)？
##使用更加先进的 beautifulsoup果然十分强大，完美避免正则表达式的困扰
##http://beautifulsoup.readthedocs.io/zh_CN/latest/#find-all
##http://cuiqingcai.com/1319.html

##爬糗事百科前十页的内容
# -*- coding: utf-8 -*-
from urllib import request
from bs4 import BeautifulSoup
for i in range(1,2):
    url=request.Request("http://www.qiushibaike.com/hot/page/"+str(i)+"/")
    url.add_header('User-Agent', 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.')
    with request.urlopen(url) as f:
        data=f.read().decode('utf-8')    
        #pattern = re.compile(r'class="text"([\s\S]*)sapn?',re.S)
        #items = re.findall(pattern,data) #失败的正则表达式尝试
        soup = BeautifulSoup(data, 'html.parser')
        #print(soup.prettify())
        for i in soup.find_all("div",class_="article block untagged mb15 typs_hot"):
            with open('E:/code/python_learn/crawler/test.txt','a') as file_p:
                for j in i.find_all('a',class_="contentHerf"):
                    file_p.write(j.get_text(strip=True))
                    file_p.write('\n')
                for k in i.find_all('img',class_="illustration"):
                    file_p.write('![](')
                    file_p.write(k['src'])
                    file_p.write(')')
                    file_p.write('\n')
                file_p.write('\n')