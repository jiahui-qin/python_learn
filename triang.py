def triang(n):
    print([1,1])
    a=[1,1]
    b=[1,2,1]
    i=2
    for i in range(2,n):
        yield b
        a=b
        c1=a[0:i]
        c2=a[1:i+1]
        b=c1  
        for n in range(i):
            b[n]=c1[n]+c2[n]
        b.append(1)
        b.insert(0,1)
    return 'done'

for i in triang(8):
    print(i)