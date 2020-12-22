class_list = {} 
data = input()
temp = data.split(', ')
for i in range(len(temp)):
    temp2=temp[i].split(':')
    if temp2[0]>='a' and temp2[0]<='z':
        class_list[temp2[0]] = int(temp2[1])
    else:
        print("error! Uppercase found")

while True:
    num=input()
    if num=="STOP":
        break
    else:
        C=0
        for i in class_list:
            if class_list[i]==int(num):
                C+=1
        if C==0:
            print(False)
        else:
            print(True)