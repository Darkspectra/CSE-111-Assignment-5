#CALCULATION PART

Dic = {} 
data = input() 
temp = data.split(', ')
for i in range(len(temp)):
    temp2=temp[i].split(':')
    Dic[temp2[0]] = int(temp2[1])
    L1=len(Dic)
    
Dic2 = {} 
data1 = input() 
temp = data1.split(', ')
for i in range(len(temp)):
    temp2=temp[i].split(':')
    Dic2[temp2[0]] = int(temp2[1])
    L2=len(Dic2)

N_Dic = {}
for i in Dic:
    for j in Dic2:
        if j==i:
            m=Dic2[j]+Dic[i]
            N_Dic[j]=m
print(N_Dic)
           
for i in Dic:
    C=0
    for j in Dic2:
        if i!=j:
            C+=1
    if C==len(Dic2):
        m=Dic[i]
        N_Dic[i]=int(m)

#ANSWER PART

for i in Dic2:
    C=0
    for j in Dic:
        if i!=j:
            C+=1
    if C==len(Dic):
        N_Dic[i]=Dic2[i]

x=sorted(N_Dic)
W_Dic = {}
for i in x:
    W_Dic[i]=N_Dic[i]
print(W_Dic)

T=[]
for i in W_Dic:
    T.append(W_Dic[i])
T.sort()
M=set(T)
D=list(M)

lst = len(D)
for i in range(0, lst):
    for j in range(0, lst-i-1):
        if (D[j] > D[j + 1]):
            temp = D[j]
            D[j]= D[j + 1]
            D[j + 1]= temp
print(tuple(D))