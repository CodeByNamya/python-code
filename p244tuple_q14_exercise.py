import random

t1=()
l1=[]
n=int(input("enter limit=>"))
for i in range(1,n+1):
    l1.append(random.randint(1,10))
t1=tuple(l1)
print(t1)
x=int(input("Enter value to count =>"))
v=l1.count(x)
print(v)

