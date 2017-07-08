dup_list=[10,20,30,20,10,50,60,40,80,50,40]
for i in dup_list:
    if dup_list.count(i)!=1:
        dup_list.remove(i)

print(dup_list)        
