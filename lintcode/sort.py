## 463 整数排序
def sorlt(a):
    for i in range(len(a)):
        print(len(a)-i)
    for i in range(len(a),0):
        print(i+'ok')
        for j in range(1, i):
            if a[j - 1] > a[j]:
                a[j], a[j - 1] = a[j - 1], a[j]
                print(a)
    return a 

print(sorlt([4,3,2,1]))
                