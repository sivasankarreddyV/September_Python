#to print the dictionary keys and values
d1={1:"one",2:"two",3:"three"}
d2={}
for x in d1.keys():
    print(x,d1[x])
    d2=(d1[x])=x
l=d1.keys()
print(l)
l2=d1.values()
print(l2)
print(type(l))
print(type(l2))


#dictionary swapping
d={1:"one",2:"two"}
print(d)
for x in d.items():
    print(x)
    k,v=x
    d3={}
    d3[v]=k
    print(d3)
