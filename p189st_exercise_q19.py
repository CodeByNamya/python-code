import random
l1=[]
l2=[]
l3=[]
n=int(input('enter limit=>'))
for i in range(1,n+1):
    l1.append(random.randint(1,5))
    l2.append(random.randint(1,5))
print(l1)
print(l2)
for x in l1:
    if x in l2:
        l3.append(x)
print("common elements are=>",l3)


