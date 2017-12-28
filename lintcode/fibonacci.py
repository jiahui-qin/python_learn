
def fibonacci(n):
    # write your code here
    #从低向上
    lll = []
    if n == 1:
        return 0
    if n == 2:
        return 1
    for i in range(n):
        lll.append(0)
    lll[1] = 1
    for i in range(2,n):
        lll[i] = lll[i-1]+lll[i-2]
    return lll[n-1]

print(fibonacci(7))

