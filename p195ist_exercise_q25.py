import random

l1=[]
c1=0
c2=0
n=int(input("enter limit=>"))
for i in range(1,n+1):
    l1.append(random.randint(1,10))
print(l1)
for x in l1:
    if x%2==0:
        c1=c1+1
    else:
        c2=c2+1
print("no of odd number=",c2)
print("no of even number=",c1)

