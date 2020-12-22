d = {}
while True:
    entry = input()
    if entry=="STOP":
        break
    else:
        entry = int(entry)
        if entry in d:
            d[entry]=d.get(entry)+1
        else:
            d[entry]=1
        
for i in d:
    print(i,"-",d.get(i),"times")