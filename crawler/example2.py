#模拟浏览器发送get请求，需要使用request对象
#往request对象添加http头，就可以把请求伪装成浏览器
##查看报头(header)？

# from urllib import request

# req = request.Request('http://www.163.com/')
# req.add_header('User-Agent', 'Mozilla/6.0 (iPhone; CPU iPhone OS 8_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/8.0 Mobile/10A5376e Safari/8536.25')
# with request.urlopen(req) as f:
#     data=f.read() ## .read()方法可以读取
#     print('Status:',f.status, f.reason) ## .status\.reason 是读取之后返回的状态信息
#     for k,v in f.getheaders():
#         print('%s: %s' % (k, v))

#     print('data: ',data.decode('utf-8'))


from urllib import request
import re

url=request.Request("http://www.qiushibaike.com/hot/page/1/")
url.add_header('User-Agent', 'Mozilla/6.0 (iPhone; CPU iPhone OS 8_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/8.0 Mobile/10A5376e Safari/8536.25')
with request.urlopen(url) as f:
    #req = request.Request(url)
    #data=request.urlopen(url)
    data=f.read().decode('utf-8')
    print(data)
    pattern = re.compile(r'class="text"([\s\S]*)sapn?',re.S)
    items = re.findall(pattern,data)
    for item in items:
        print(item)


    #<a href="/article/119603372" class="text" onclick="_hmt.push(['_trackEvent', 'list-qiushi-first', 'chick']);">