a=['abc','xyz','aba','1221']
num=0
for k in a:
    if len(k)>=2 and k[0]==k[len(k)-1]:
        num+=1
print("a 리스트 중에서 조건에 만족하는 문자열은 %d개 입니다." %num)        
        
