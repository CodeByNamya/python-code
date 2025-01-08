import random
t1=()
l1=[]
n=int(input("enter limit=>"))
for i in range(1,n+1):
    x=random.randint(1,100)
    if l1.count(x)==0:
        l1.append(x)
#print(l1)
t1=tuple(l1)
print(t1)
x=int(input("enter value to be removed=>"))
l1.remove(x)
t1=tuple(l1)
print(t1)

