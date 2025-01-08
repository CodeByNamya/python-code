import random

n=int(input("Enter limit =>"))
d1={}
for i in range(1,n+1):
    k=i
    v=random.randint(1,50)
    d1[k]=v

print("no\tmarks")
print("*"*20)
for k,v in d1.items():
    print(k,"\t|\t ",v)
print("*"*20)