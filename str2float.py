from functools import reduce
def char2num(s):
    return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[s]

def str2float(s):
    s=s.split('.')
    s1=reduce(lambda x,y:x*10+y,map(char2num,s[0]))
    s2=reduce(lambda x,y:x*10+y,map(char2num,s[1])) ##注意lambda和map、reduce的使用
    return(s1+s2/10**len(s[1]))

print('str2float(\'123.456\') =', str2float('123.456'))