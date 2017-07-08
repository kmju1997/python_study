import random
target_num= random.randint(1,9)
a = input("숫자를 맞춰보세요! ")
a=int(a)

if a!=target_num :
    print("땡! 숫자는 %d이였습니다." %target_num)
else :
    print("맞췄습니다! 대단해요!")
