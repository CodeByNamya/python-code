import random

t1=()
l1=[]
n=int(input('enter limit=>'))
for i in range(1,n+1):
    l1.append(random.randint(1,50))
    v=l1.reverse()
t1=tuple(l1)
print(t1)
print(v)