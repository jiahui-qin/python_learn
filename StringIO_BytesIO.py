from io import StringIO
##.StringIO() and .BytesIO() 都是一个对象，可以通过它们内置的方法进行操作
##面向对象的程序设计

#首先创建一个StringIO对象，然后用var.write写入
#返回值是写入字符的长度
#最后可以用var.getvalue()读出str

f=StringIO('Hello!\nHi!\nGoodbye!')
print(f.getvalue())
while True:
    s=f.readline()##一行一行读取
    if s=='':
        break
    print(s.strip())#.strip(rm)方法删除掉前后的所有rm内容，为空时删除掉空格
    #.lstrip(rm)删除掉位于开头处的，.rstrip(rm)删除掉结尾处的

from io import BytesIO
g=BytesIO()#.bytesIO()可以读写二进制数据
print(g.write('中文'.encode('utf-8')))
print(g.getvalue())


