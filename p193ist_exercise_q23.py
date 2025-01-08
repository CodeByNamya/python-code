import random
l2=[]
l1=[]
m=1
n=int(input("enter limit=>"))
for i in range(1,n+1):
    l1.append(random.randint(1,10))
print(l1)
for x in l1:
    m=m*x
print(m)