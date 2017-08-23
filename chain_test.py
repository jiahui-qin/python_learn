class Chain(object): ##定制类
##定制类中的方法，鸭子属性使得只要编译器可以调用到名称相同的就可以使用
##因此可以按照自己的要求定制类中不同的属性
##子类的方法不会影响父类的方法
##因此按照编译器需要引用的方法即可定义类的方法
    def __init__ (self, path=''):
        self._path=path
    
    def __getattr__(self, path):##Chain是什么方法？
        return Chain('%s/%s' % (self._path,path))
    
    def __str__(self):
        return self._path

    __repr__ = __str__


print(Chain().users('michael').repos)