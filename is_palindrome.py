# def is_palindrome():
#     yield 1
#     it=isch()
#     while True:
#         n=next(it)
#         yield(n)
#         filter(checkpa(n),it)


# def isch():
#     n=1
#     while True:
#         n=n+1
#         yield n

# def checkpa(n):
#     a=str(n)
#     num=0
#     for i in range(len(a)//2):
#         if a[i]==a[len(a)-i-1]:
#             num=num+1
#     if num==len(a)//2:
#         return(n)
#     else:
#         return False

# for n in is_palindrome():
#     if n<1000:
#         print(n)
#     else:
#         break
        
def checkpa(n):
    a=str(n)
    num=0
    for i in range(len(a)//2):
        if a[i]==a[len(a)-i-1]:
            num=num+1
    if num==len(a)//2:
        return(n)

n=filter(checkpa,range(1000))
print(list(n))