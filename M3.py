d = {}
d1 = {}
data1 = input()
data = data1.split(',')
for x in range(len(data)):
    t = data[x].split(':')
    d[t[0]]=(t[1])

for i in d:
    if d.get(i) in d1:
        x=d1.get(d.get(i))
        x.append(i)
        d1[d.get(i)]=x
    else:
        d1[d.get(i)]=[i]
print(d1)