import functools
#在函数的开头打印begin calls和结尾打印end calls
# def log(func): 
#     @functools.wraps(func) ##相当于赋值func.__name__=now.__name__,防止函数名字改变
#     def wrapper(*args,**kw):
#         print('begin calls')
#         ee=func(*args,**kw)  ##把ee赋值给func(*args,**kw)，
#         print('end calls') ##最后返回的也只调用ee，不会再调用func，在最后再打印一行出来
#         return ee
#     return wrapper
# @log
# def now():
#     print('dasd-1dsad-12')

# now()

#写一个@log既支持 @log，也支持@log('excute') 
#可选参数
# def log(text='call'):
#     def decorator(func):
#         @functools.wraps(func)
#         def wrapper(*args,**kw):
#             print('%s %s()' %(text,func.__name__))
#             return func(*args,**kw)
#         return wrapper
#     return decorator

def log(arg='call'):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kw):
            print('%s %s()' % (arg, func.__name__))
            return func(*args, **kw)
        return wrapper
    return decorator
@log
def ttt():
    print('asdas')


ttt()