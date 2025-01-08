import random
d1={}
n=int(input("enter limit=>"))
for i in range(1,n+1):
    k=i
    v=random.randint(1,50)
    d1[k]=v
print(d1)
print("no\tmarks\tresult")
n1=0
n2=0
for k,v in d1.items():
    if v>18:
        print(k,"\t",v,"\t","pass")
        n1=n1+1
    else:
        print(k,"\t",v,"\t ","fail")
        n2=n2+1
print("total students pass=",n1)
print("total students failed=",n2)