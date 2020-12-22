Dic = {} 
data = input() 
temp = data.split(', ')
for i in range(len(temp)):
    temp2=temp[i].split(':')
    Dic[temp2[0]] = int(temp2[1])

m_x=[]
for i in Dic:
    m_x.append(Dic[i])
    
for i in range(len(m_x)):
    for j in range(i+1,len(m_x)):
        if m_x[i]>m_x[j]:
            temp = m_x[i]
            m_x[i] = m_x[j]
            m_x[j] = temp

for i in Dic:
    if Dic[i]==m_x[-1]:
        print("Maximum: "+i)    
    elif Dic[i]==m_x[0]:
        print("Minimum: "+i)