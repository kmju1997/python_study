def getaverage (lines):
    num=0
    whole=0
    for line in lines:
        line=int(line)
        num+=1
        whole+=line
    average=int(whole/num)
    return average
        
        
    
f1=open("C:/Users/강민주/Desktop/대학/동아리/포리프/파이썬 스터디/sample.txt",'r')
lines=f1.readlines()
average=getaverage(lines)
print("평균은 %d입니다."%average)

f2=open("C:/Users/강민주/Desktop/대학/동아리/포리프/파이썬 스터디/result.txt",'w')
data="평균은 %d입니다."%average
f2.write(data)
f1.close()
f2.close()
       


    
