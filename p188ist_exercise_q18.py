import _random
import random

l1=[]
l2=[]
n=int(input("enter limit=>"))
for i in range(1,n+1):
        l1.append(random.randint(1,10))
        l2.append(random.randint(1,10))
print(l1)
print(l2)
l1.extend(l2)
print("combined list",l1)

