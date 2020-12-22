dict1={0:[" "],1:[".",",","?","!",":"],2:["A","B","C"],3:["D","E","F"],4:["G","H","I"],5:["J","K","L"],6:["M","N","O"],7:["P","Q","R","S"],8:["T","U","V"],9:["W","X","Y","Z"]}
x = input()
x = x.upper()
for i in x:
    for k,v in dict1.items():
        if i in v:
            idx = v.index(i)
            count = 0
            while count <(idx+1):
                print(k,end="")
                count+=1