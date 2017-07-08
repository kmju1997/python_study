coke=0
juice=0
ed=0
total=0

while total<=10000 :
    choice=input("메뉴를 고르세요. 1.콜라(1500원) 2.주스(1200원) 3.에너지드링크(2000원) ")
    if choice=='1':
        coke+=1
        total+=1500
            
    elif choice=='2':
        juice+=1
        total+=1200
        
    else:
        ed+=1
        total+=2000
        
print("전체 %d원 입니다." %total)        
print("오늘 콜라는 %d개, 주스는 %d개, 에너지 드링크는 %d개 팔았습니다." %(coke,juice,ed))    
