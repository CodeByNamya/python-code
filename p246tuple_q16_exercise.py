import random

t1=()
l1=[]
n=int(input("enter limit=>"))
for i in range(1,n+1):
    x=random.randint(1,10)
    l1.append(x)
t1=tuple(l1)
print(t1)
l1=list(t1)
l1.sort()
t1=tuple(l1)
print(t1)