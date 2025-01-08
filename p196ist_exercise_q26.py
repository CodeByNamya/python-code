import random
from traceback import print_tb

l2=[]
l1=[]
n=int(input("enter limit=>"))
for i in range(1,n+1):
    l1.append(random.randint(1,10))
print(l1)
l1[0],l1[-1]=l1[-1],l1[0]
l2.append(l1)
print(l1)
