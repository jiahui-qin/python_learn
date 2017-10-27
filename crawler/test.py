##爬到一个网站现在看起来不是很难，现在先把网站保存到本地然后开始学习吧
from urllib import request
from bs4 import BeautifulSoup
data = request.urlopen("file:///C:/Users/saber/Desktop/liuli.html")
data=data.read().decode('utf-8')
soup = BeautifulSoup(data, 'html.parser')
#print(soup.article.next_silbing)
for thetitle in soup.find_all("h1", class_="entry-title"):
    print(thetitle.get_text(strip=True))
    tags = thetitle.parent.parent.footer
    for tag in tags.find_all("span", class_ = "tag-links"):
        print(tag.get_text(strip=True)[1])
    print(thetitle.a['href'])##接下来就是进入href然后获取神秘代码
    print()

