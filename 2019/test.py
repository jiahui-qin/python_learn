'''
##函数参数传递

当一个引用传递给函数的时候,函数自动复制一份引用,这个函数里的引用和外边的引用没有半毛关系了.所以第一个例子里函数把引用指向了一个不可变对象,当函数返回的时候,外面的引用没半毛感觉.而第二个例子就不一样了,函数内的引用指向的是可变对象,对它的操作就和定位了指针地址一样,在内存里进行修改.


## @staticmethod和@classmethod

实例方法只能被实例对象调用，静态方法(由@staticmethod装饰的方法)、类方法(由@classmethod装饰的方法)，可以被类或类的实例对象调用。实例方法，第一个参数必须要默认传实例对象，一般习惯用self。
静态方法，参数没有要求。无法访问类属性、实例属性，相当于一个相对独立的方法，跟类其实没什么关系，换个角度来讲，其实就是放在一个类的作用域里的函数而已。
类方法，第一个参数必须要默认传类，一般习惯用cls。可以访问类属性，无法访问实例属性。

## 类变量与实例变量的区别


## python的推导

列表推导，字典推导， 集合推导

    vars = [var for var in range(30) if var % 3 is 0] 

上式是列表，如果编程小括号就是一个生成器

## 下划线

__foo__python内部的名字 _foo_变量私有，不能用import导入 __foo

## *args and **kwargs

第一个是如果不确定要传入多少个参数

第二个是允许使用没有实现定义的参数名

*args必须在**kwargs前面.

## 单例模式

只包含一个被称为单例类的特殊类，可以包装系统中一个类只有一个实例

4种方法：

1. __new__()

    class Singleton(object):
    def __new__(cls, *args, **kw):
        if not hasattr(cls, '_instance'):
            orig = super(Singleton, cls)
            cls._instance = orig.__new__(cls, *args, **kw)
        return cls._instance

2. 共享属性 所有实例的__dict__指向同一个字典，使其具有相同的方法和熟悉
__dict__用来存储对象属性

    class Borg(object):
    _state = {}
    def __new__(cls, *args, **kw):
        ob = super(Borg, cls).__new__(cls, *args, **kw)
        ob.__dict__ = cls._state
        return ob

3. 装饰器 @singleton

    def singleton(cls, *args, **kw):
    instances = {}
    def getinstance():
        if cls not in instances:
            instances[cls] = cls(*args, **kw)
        return instances[cls]
    return getinstance

    @singleton
    class MyClass:

4. import

from mysingleton import my_singleton

### 协程

简单点说协程是进程和线程的升级版,进程和线程都面临着内核态和用户态的切换问题而耗费许多切换时间,而协程就是用户自己控制切换的时机,不再需要陷入系统的内核态.

Python里最常见的yield就是协程的思想!

### 闭包

### lambda 匿名函数 辅助用的短函数

### 函数式编程

filter 函数的功能相当于过滤器。调用一个布尔函数bool_func来迭代遍历每个seq中的元素；返回一个使bool_seq返回值为true的元素的序列。

map函数是对一个序列的每个项依次执行函数
    
    a = map(lambda x: x*2,[1,2,3])
    list(a)

reduce函数是对一个序列的每个项迭代调用函数
'''

def singleton(cls, *args, **kw):
    instances = {}
    def getinstance():
        if cls not in instances:
            instances[cls] = cls(*args, **kw)
        return instances[cls]
    return getinstance

@singleton
class MyClass: