#writedata.py

f=open("C:/Users/강민주/Desktop/대학/동아리/포리프/파이썬 스터디/새파일.txt",'w')
for i in range(1,11):
    data="%d번째 줄입니다.\n"%i
    f.write(data)
f.close()

f=open("C:/Users/강민주/Desktop/대학/동아리/포리프/파이썬 스터디/안녕하세요.txt",'r')
lines=f.readlines()
for line in lines:
    print(line)
f.close
       
       
