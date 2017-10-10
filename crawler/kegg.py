from urllib import request
##kegg的下载需要几个添加几个响应报头
url=request.Request("http://www.kegg.jp/kegg-bin/download?entry=ec00402&format=kgml")
url.add_header('Connection','keep-alive')
url.add_header('User-Agent','Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36')
url.add_header('Referer','http://www.kegg.jp/kegg-bin/show_pathway?org_name=ec&mapno=00402&mapscale=&show_description=show')
url.add_header('Upgrade-Insecure-Requests','1')

f=request.urlopen(url)
data=f.read().decode('utf-8')
print(data)