import random

l1=[]
n=int(input("enter limit=>"))
for i in range(1,n+1):
    y=random.randint(1,30)
    if y not in l1:
        l1.append(y)
print(l1)
l1.remove(max(l1))
print(max(l1))