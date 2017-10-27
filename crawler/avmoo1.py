from urllib import request
from bs4 import BeautifulSoup
data = request.urlopen("file:///C:/Users/saber/Desktop/avmp1.html")
data=data.read().decode('utf-8')
soup = BeautifulSoup(data, 'html.parser')
tags = soup.find('div', class_ = "col-md-3 info")
print(soup.find('div',id="avatar-waterfall").get_text(strip=True))
for tag in tags.stripped_strings:
    ##这里可以通过匹配':'来识别属性
    if list(tag).pop()==':':
        print(tag,end=' ')
    else:
        print(tag)
        print(tag)