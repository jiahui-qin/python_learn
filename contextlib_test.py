##2017/8/31 
##contextlib内置模块
##with语句的用法

# ##正确读写文件资源：如果成功打开文件之后要关闭文件
# try:
#     f = open('/path/to/file', 'r')
#     f.read()
# finally:
#     if f:
#         f.close()
# ##用with来简化上述语句
# with open('path/to/file', 'r') as f:
#     f.read()

##任何对象只要实现了上下文管理器就可以用于with语句
##上下文管理器通过 __enter__(), __exit__()来实现

##with context_expression [as target(s)]:
##    with_body
##context_expression返回一个上下文管理器对象，如果指定了as子句，/
##将__enter__方法的返回值赋值给target(s)
##执行完with_body之后执行__exit__()方法
# class Querry(object):
#     def __init__(self, name):
#         self.name = name

#     def __enter__(self):
#         print('begin')
#         return self

#     def __exit__(self, exc_type, exc_value, traceback):
#         if exc_type:
#             print('error')
#         else:
#             print('End')
    
#     def querry(self):
#         print('Querry info about %s...' % self.name)

# with Querry('bob') as q:
#     q.querry()
# #input:
# #begin
# #Querry info about bob...
# #End

from contextlib import contextmanager
class Querry(object):

    def __init__(self, name):
        self.name = name
    def querry(self):
        print('Querry info about %s...' % self.name)
    
@contextmanager ##这是一个decorator，可以接受一个generator
def creat_querry(name):
    print('Begin')
    q = Querry(name)
    yield q ##yield语句把 with ... as var 输入进去
    print('End')

with creat_querry('bob') as q:
    q.querry()
#############################################
##yield调用会执行with语句内部的所有语句
@contextmanager
def tag(name):
    print('<%s>' % name)
    yield
    print('</%s>' % name)

with tag('h1'):
    print('hello')
    print('world')

##如果一个对象没有实现上下文，可以用closing() 把这个对象变为上下文对象
##closing也是一个经过@contextmanager修饰过得generator
@contextmanager
def closing(thing):
    try:
        yield thing
    finally:
        thing.close()