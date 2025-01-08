l1=[23,34,12,190,57,34,56,80]
print(l1)
l2=[]
n=int(input("enter value=>"))
for x in l1:
    if x>n:
        l2.append(x)
print(l2)