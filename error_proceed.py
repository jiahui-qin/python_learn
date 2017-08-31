# err_logging.py

import logging
##logging.exception可以记录错误同时让程序继续执行
def foo(s):
    return 10 / int(s)

def bar(s):
    return foo(s) * 2

def main():
    try:
        bar('0')
    except Exception as e: #可以有多个except
        logging.exception(e) #https://docs.python.org/3/library/exceptions.html#exception-hierarchy 错误类型概述
    finally: #无论如何都会执行finally，可以不写finally
        print('finally')
main()
print('END')