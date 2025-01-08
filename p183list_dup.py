import random
l1=[]
l2=[]
l3=[]
n=int(input("Enter limit =>"))
for i in range(1,n+1):
    l1.append(random.randint(1,10))
print(l1)
for x in l1:
    if l1.count(x)>1:
        l2.append(x)
    else:
        l3.append(x)
print("\nduplicate values are -:",l2,end=" ")
print("\ndata -:",l3,end=" ")
