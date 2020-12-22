ent1=input()
ent2=input()
ent1 = ent1.lower()
ent2 = ent2.lower()
d1={}
d2={}
for i in ent1:
    if i in d1:
        d1[i]=d1.get(i)+1
    else:
        d1[i]=1

for i in ent2:
    if i in d2:
        d2[i]=d2.get(i)+1
    else:
        d2[i]=1

x1=sorted(d1)
x2=sorted(d2)
y1=sorted(d1.values())
y2=sorted(d2.values())
for i in range(0,len(x1)):
    d1={x1[i]:y1[i]}
for i in range(0,len(x2)):
    d2={x2[i]:y2[i]}
if d1==d2:
    print("Those strings are anagrams")
else:
    print("Those strings are not anagrams")