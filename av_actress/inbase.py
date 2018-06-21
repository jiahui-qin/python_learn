from urllib import request
from bs4 import BeautifulSoup
from time import sleep
import re
import gzip
import  sys
import ssl
import json

def gettoken():
    # client_id 为官网获取的AK， client_secret 为官网获取的SK
    host = 'https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id=q2EhUO96UgQC1oGScjqsrNW5&client_secret=LN0fCK4We06hyjcdpeogUp0erq7GQc4z'
    data = request.Request(host)
    data.add_header('Content-Type', 'application/json; charset=UTF-8')
    with request.urlopen(data) as f:
        content = f.read()
        if (content):
            p = json.loads(content)
            print(p['access_token'])
            return(content)


request_url = "https://aip.baidubce.com/rest/2.0/face/v3/faceset/user/add"
id = 'kaori3'
params = [ { 'image' : 'https://jp.netcdn.space/mono/actjpgs/kaori3.jpg', 'image_type' : 'URL', 'group_id' : 'actor',  'user_id' : 'kaori3','quality_control' : 'LOW' ,'liveness_control':'NONE'} ]
params = json.dumps(params)
access_token = '24.c730d358b20be8063324b95c91a00c68.2592000.1532180467.282335-11422493'
request_url = request_url + "?access_token=" + access_token
data = request.Request(url=request_url, data=params.encode(encoding='UTF8'))
data.add_header('Content-Type', 'application/json')
data = request.urlopen(data)
content = data.read()
if content:
    print(content)


