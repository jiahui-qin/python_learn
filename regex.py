##本章内容是正则表达式 Regular Expression
import re
m=re.match(r'^(\d{3})\-(\d{3,8})$','010-12345')
if m:
    print('pass')

##re.match方法，如果匹配成功，返回一个match对象，如果失败，返回None
##^\d表示以数字开头， \d$表示以数字结尾
#用()可以定义要提取的分组，如下列所示
print(m.group(0), m.group(1), m.group(2))
print(m.groups())
##在Python中使用正则表达式时，re模块会做：
##1、编译正则表达式
##2、用编译过的正则表达式去匹配字符串
##所以直接用(re.compile()方法)预编译一个正确的正则表达式
re_telephone = re.compile(r'^(\d{3})\-(\d{3,8})$')

print(re_telephone.match('010-123445').groups())


##练习
##写一个可以验证Email地址的正则表达式，版本一可以验证
##someone@gmail.com
##bill.gates@microsoft.com
##r'^([0-9a-zA-Z\_\.]+)@([0-9a-z]+)\.(com|org)$' 此正则表达式可以验证
test=re.match(r'^([0-9a-zA-Z\_\.]+)@([0-9a-z]+)\.(com|org)$', 'someonr@gmail.com')
print(test.groups())
##进阶版：验证 <Tom Paris> tom@voyager.org
##r'^<([a-zA-Z\s+\.]+)>\s([0-9a-zA-Z\_\.]+)@([0-9a-z]+)\.(com|org)$'
test1=re.match(r'^<([a-zA-Z\s+\.]+)>\s([0-9a-zA-Z\_\.]+)@([0-9a-z]+)\.(com|org)$', '<Tom Paris> tom@voyager.org')
print(test1.groups())
