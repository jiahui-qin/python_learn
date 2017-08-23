class Student(object):

    def __init__(self, name, score):
        #self.name = name
        #self.score = score
        self.__name = name #类的内部属性加 ‘__’使其成为私有变量
        self.__score = score #私有变量外部不能直接访问

    def get_name(self): #如果想要外部变量访问的话
        return self.__name
    def get_score(self): #定义一个内部方法来访问private变量
        return self.__score

    def set_score(self, score): #定义一个修改score的方法
        if 0<=score<=100: #可以通过此函数检查外部传入数据的准确性
            self.__score = score
        else:
            raise ValueError('Bad score')

    def print_score(std):
        print('%s: %s' % (std.__name, std.__score))

    def get_grade(self):
        if self.__score>=90:
            return 'A'
        else:
            return 'B'

bart = Student('Bart Simpson', 59) #数据传入之后不能随意修改
                                    #只能通过内部的函数修改
bart.print_score()
print(bart.get_grade())
##print(get_grade(bart)) 为什么此处显示get_grade方法找不到？
bart.set_score(71)
bart.print_score()