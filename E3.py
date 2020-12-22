Dic = {}
m=int(input())
Dic[0]=m
n=1
while n<10:
    m=int(input())
    C=0
    for j in range(len(Dic)):
        if Dic[j]==m:
            C+=1
    if C>=1:
        print("Duplicate found!!")
    else:
        Dic[n]=m
        n+=1