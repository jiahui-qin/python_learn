#使用assert方法检测错误
# def foo(s):
#     n=int(s)
#     #可以用assert来检查，会抛出AssertionError错误
#     #程序调试完成后可以用如下语句来关闭assert警告
#     #  $python3 -0 err.py  '-0'参数关闭assert，将其视为pass
#     assert n != 0, 'n is zero!' 
#     return 10 / n

# def main():
#     foo('0')

# main()


#使用logging方法检测错误
import logging
logging.basicConfig(level=logging.INFO)
#输出错误到文件，可以用level制定输出哪一级别的错误
s='0'
n=int(s)
logging.info('n = %d' % n) 
print(10 / n)

##还可以使用IDE的设置断点、单步执行等功能，VScode有此功能