l1= ["Raj", "", "Rahul", "Mansi", "", "Manav", "Disha"]
l2=[]
print(l1)
for x in l1:
    if len(x)==0:
        pass
    else:
        l2.append(x)
print(l2)