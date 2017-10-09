#HTTP协议永远都是客户端发起请求，服务器回送响应。
#对于一些需要登录的网站，如果不是从浏览器发出的请求，则得不到响应。所以，我们需要将爬虫程序发出的请求伪装成浏览器正规军。
#具体实现：自定义网页请求报头。
##如何查看请求和响应报头？

#爬虫的实现方式先学习urllib和正则表达式
#熟练之后再学习requests和beautifulSoup
from urllib import request 

with request.urlopen('https://www.liaoxuefeng.com/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/001432688314740a0aed473a39f47b09c8c7274c9ab6aee000/') as f:
    ##用request.urlopen('')来读取网页中的数据
    data=f.read() ## .read()方法可以读取
    print('Status:',f.status, f.reason) ## .status\.reason 是读取之后返回的状态信息
    for k,v in f.getheaders():
        print('%s: %s' % (k, v))

    print('data: ',data.decode('utf-8'))