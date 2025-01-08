import random

t1=()
l1=[]
n=int(input("enter limit=>"))
for i in range(1,n+1):
    l1.append(random.randint(1,n+1))
t1=tuple(l1)
print(t1)
l1=list(t1)
a=l1[2:5]
t1=tuple(a)
print(t1)