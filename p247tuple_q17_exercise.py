import random

t1=()
t2=()
l1=[]
l2=[]
n1=int(input("enter limit1=>"))
n2=int(input("enter limit2=>"))

for i in range(1,n1+1):
    x=random.randint(1,10)
    l1.append(x)
t1=tuple(l1)
print(t1)
for i in range(1,n2+1):
    y=random.randint(1,10)
    l2.append(y)
t2=tuple(l2)59
print(t2)
print(t1+t2)
