# try: ##保证最后能关闭文件
#     f=open('E:/VSprogram/ccc.txt','r')
#     print(f.read())
# finally:
#     if f:
#         f.close()

# with open('E:/VSprogram/ccc.txt','r') as f:
#     print(f.read()) ##与try...fianlly...功能相同


##readlines()用循环反复读取，防止文件过大
##也可以使用read(size)设置一次读取的文件大小
with open('E:/VSprogram/ccc.txt', 'w', encoding='gbk', errors='ignore') as f:
    ##open('E:/VSprogram/ccc.txt','r') 读取文本文件用'r'模式打开
    ##读取二进制文件如视频或图片用'rb'打开
    for line in f.readlines():
        f.write(line.replace('apple','hi'))