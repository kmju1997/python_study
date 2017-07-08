f = open("gk.csv","r")
lines = f.readlines()

print(len(lines))
n=[]
int_s=[]
length = len(lines)+1
for  i in range(1,len(lines)+1):
    n.append(i)

for i in lines :
    s = i.split()
    s_int = int(s[0])
    int_s.append(s_int)
   
    
for i in range(1000) :
    if n[i] != int_s[i]:
        int_s.insert(i,"error")
        n.append(length)
        length+=1
        print(n)


for i in range(len(int_s)):
    if int_s[i] == "error" :
             print(i+1)
    
f.close()
