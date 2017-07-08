a=[1,1,2,3,5,8,13,21,34,55,89]
b=[1,2,3,4,5,6,7,8,9,10,11,12,13]
intersection=[]
for i in a :
    for j in b:
        if i==j:
            intersection.append(i)
for k in intersection:
    if intersection.count(k)!=1:
        intersection.remove(k)

print(intersection)        
        
