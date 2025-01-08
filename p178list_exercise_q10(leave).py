import random
l1=[]
l2=[]
n=int(input("Enter limit =>"))
for i in range(1,n+1):
    l1.append(random.randint(1,30))
    l2.append(random.randint(1, 30))

print(l1)
print(l2)

for x in l1:
    if x in l2:
        print(x)