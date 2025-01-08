import random

d1={}
n=int(input("enter limit=>"))
for i in range(1,n+1):
    k=i
    v=random.randint(1,50)
    d1[k]=v
print(d1)
list1=[]
print("sr.no\tmarks")
for k,v in d1.items():
    print(k , "\t\t",v)
    list1.append(v)

m=max(list1)
print("max marks=",m)

for k,v in d1.items():
    if v==m:
        print("Max marks : ",k , "=>",v)
