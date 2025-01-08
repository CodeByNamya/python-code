import random

l1=[]
l2=[]
l3=[]
n=int(input("enter limit=>"))
for i in range(1,n+1):
    l1.append(random.randint(1,10))
print(l1)
for x in l1:
    if x%2==0:
        l2.append(x)
    else:
        l3.append(x)

l1=l2
print("even values=>",l1)
print("data=",l3)