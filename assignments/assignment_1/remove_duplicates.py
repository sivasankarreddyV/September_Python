#to print the removing duplicates in the list
l=[10,20,30,40,50,10,20,30]
l2=[]
for x in l:
    if x not in l2:
        l2.append(x)
print(l2)
