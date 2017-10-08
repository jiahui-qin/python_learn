#HTTP协议永远都是客户端发起请求，服务器回送响应。
#对于一些需要登录的网站，如果不是从浏览器发出的请求，则得不到响应。所以，我们需要将爬虫程序发出的请求伪装成浏览器正规军。
#具体实现：自定义网页请求报头。
##如何查看请求和响应报头？
import urllib.request,socket,re,sys,os  
  
#定义文件保存路径  
targetPath = "E:\\Spider"  
  
def saveFile(path):  
    #检测当前路径的有效性  
    if not os.path.isdir(targetPath):  
        os.mkdir(targetPath)  
  
    #设置每个图片的路径  
    pos = path.rindex('/')  
    t = os.path.join(targetPath,path[pos+1:])  
    return t  
  
#用if __name__ == '__main__'来判断是否是在直接运行该.py文件  
  
  
# 网址  
url = "https://avmo.club/cn"  
headers = {  
              'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) '                            'Chrome/51.0.2704.63 Safari/537.36'  
           }  
  
req = urllib.request.Request(url=url, headers=headers)  
  
res = urllib.request.urlopen(req)  
  
data = res.read()  

print(data)
for link,t in set(re.findall(r'(https:[^s]*?(jpg|png|gif))', str(data))):  
  
    print(link)  
    try:  
        urllib.request.urlretrieve(link,saveFile(link))  
    except:  
        print('失败')  