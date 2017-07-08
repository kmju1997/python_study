degree= input("섭씨온도는 끝에 C, 화씨온도는 끝에 F를 뒤에 붙여 온도를 입력하세요. ")
num=int(degree[0:len(degree)-1])
if degree[len(degree)-1]=='C' :
    change=num/5*9+32
    print("화씨온도는 %d도 입니다."%change)
else :    
    change=(num-32)/9*5
    print("섭씨온도는 %d도 입니다."%change)
    
