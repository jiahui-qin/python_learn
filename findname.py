import os
#编写一个程序，能在当前目录以及当前目录的所有子目录下查找文件名包含指定字符串的文件，并打印出相对路径。
#搜索每一个文件用递归？
#先写出搜索一个文件的函数
def findname(localfile, keyword):
    #current_filename = [x.split('/')[-1] for x in os.listdir(localfile)]#.split 可以分割一个字符串，变成一个list，最后一项就是文件名
    #current_filename = [os.path.basename(x) for x in os.listdir(localfile)]
    #错误在于os.listdir会显示出所有文件，而文件的basename就是它本身，导致文件夹不断的被调用，陷入第一个.git无法自拔？
    #所以要在这里判断一下当前文件到底是不是文件夹
    try:
        for x in os.listdir(localfile):
            filepath = localfile + os.path.sep + x  #'//' 可以用os.path.sep来代替，表示分隔符，实际上是一个字符串
            if os.path.isdir(filepath):
                findname(filepath, keyword) 
            elif os.path.basename(filepath).find(keyword) != -1: #.find 函数可以寻找一个特定的字符串
                print(filepath)
                continue
    except PermissionError:  ##权限处理，如果对一个文件夹权限不够就不访问了
        pass


print(findname('E://', 'te'))
#     for name in current_filename:
#         if len(name) >= len(findstring):
#             for i in range(len(name) - len(findstring)):
#                 if name[i:i+len(findstring)] == findstring:
#                     print(os.path.abspath(name))

# #上述是在一个文件夹里搜索特定文件，如何打开一个文件夹里的子文件夹？
# #[x for x in os.listdir() if os.path.isdir(x)]
# def findlocal(targetfile, findstring):
#     findname(targetfile, findstring)
#     current_file=[x for x in os.listdir() if os.path.isdir(x)]
#     for file in current_file:
#         if file != '.git' and file != '.vscode':
#             findlocal(file, findstring)
#         else:
#             pass




# def listfile(targetfile):
#     orilocal = os.getcwd()#先把当前的工作环境保存好，结束运行之后再返回
#     try:
#         os.chdir(targetfile)
#     except PermissionError as e:
#         print('target no right')
#     current_file=[x for x in os.listdir() if os.path.isdir(x)]
#     print(current_file)
#     for file in current_file:
#         listfile(file)
#     os.chdir(orilocal)


# listfile('E:\\test')

# import os ##这个是copy的别人的作业

# def findfile(file, keyword):
#     for x in os.listdir(file):
#         x=file + os.path.sep + x
#         if os.path.isdir(x):
#             findfile(x, keyword)
#         elif os.path.basename(x).find(keyword) != -1:
#             print(x)

# findfile('E:\\', 'num')