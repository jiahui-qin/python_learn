#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#偏函数
#调用functools包的functools.partial，固定一个函数的某些参数
#（设置函数默认值）返回一个新函数，调用这个新函数
import functools
int2=functools.partial(int, base=2)
print(int2('10010'))
#上述函数相当于下列语句
kw={'base': 2}
print(int('10010', **kw))

max2=functools.partial(max, 10)
print(max2(4, 5, 6))
#与下式比较
kww=[10]
print(max(4, 5, 6, *kww))