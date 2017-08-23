#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'a hello py program'

__author__='saber lily'

import sys

def test():
    args = sys.argv
    if len(args) == 1:
        print('Hello,world!')
    elif len(args) == 2:
        print('Hello,%s!' % args[1])
    else:
        print('Too many arguments!')

    if __name__ == '__main__':
        test()

#显然，当我运行anothertestmodule.py后第一句并不是调用者所需要的，为了解决这一问题，Python提供了一个系统变量：__name__

#注：name两边各有2个下划线__name__有2个取值：当模块是被调用执行的，取值为模块的名字；当模块是直接执行的，则该变量取值为：__main__