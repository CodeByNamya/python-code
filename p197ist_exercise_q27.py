import random
from operator import index

l1=[]
n=int(input("enter limit=>"))
for i in range(1,n+1):
    l1.append(random.randint(1,10))
print(l1)
print(max(l1))
a=l1.index(max(l1))
print("index of max number is=",a)

