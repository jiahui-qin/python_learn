from urllib import request
import re
import time
##kegg的下载需要几个添加几个响应报头
def urlset(target):
    ##创建请求
    d_target = re.match(r'(\w{2,3})(\d{3,8})',target)  ##用来匹配 ko 或者 rsa  不同的前缀
    target_url = "http://www.kegg.jp/kegg-bin/download?entry=" + target + "&format=kgml"
    target_Refer = "http://www.kegg.jp/kegg-bin/show_pathway?org_name=" + d_target.group(1) + "&mapno=" + d_target.group(2) + "&mapscale=&show_description=show"
    url = request.Request(target_url)
    url.add_header('Connection', 'keep-alive')
    url.add_header('User-Agent', 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36')
    url.add_header('Referer', target_Refer)
    url.add_header('Upgrade-Insecure-Requests', '1')
    return url

def getfile(target,url):
    #输入请求，从目标网址中得到文件并保存到本地
    f = request.urlopen(url)
    data = f.read().decode('utf-8')#data这时已经可以写入文件
    filename = target + '.txt'
    if data:
        with open(filename, 'w') as savefile:
            savefile.write(data)##这里的文件保存到了当前的工作目录
            print(target + '成功写入')
    else:
        print(target + '连接失败')

def mainpro(target):
    ##这个函数用来连接上边两个函数
    url = urlset(target)
    getfile(target, url)

def readtarget(fileload):
    target_n = []
    with open(fileload, 'r') as thefile:
        while True:
            line = thefile.readline()
            if line:
                t = line.split()
                if len(t)==4:
                    if len(t[3]) > 10:
                        target_s = t[3].split('.')[0]
                        target_n.append(target_s)
            else:
                break
    return(target_n)

def findfile(fileload):
    target_ttt = readtarget(fileload)
    
    for target in target_ttt:
        print("正在下载" + target)
        mainpro(target)
        time.sleep(1)

findfile(r"E:\MyQQ\605975357\FileRecv\all.txt")