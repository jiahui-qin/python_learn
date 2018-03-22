if '0' not in test:
    print(0)

countt = []
for i in range(10):
    countt.append(test.count(str(i)))

j = 1
while 1:
    jj = str(j)
    for jjj in jj:
        p = jj.count(jjj)
        if countt[num(jjj)] < p:
            print(j)
            break