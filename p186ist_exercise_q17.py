import random
l1=[]
n=int(input("enter limit=>"))
for x in range(1,n+1):
    l1.append(random.randint(1,10))
print(l1)
x=int(input('enter position=>'))
y=int(input("enter value=>"))
l1.insert(x,y)
print(l1)