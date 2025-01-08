"""
no=int(input("enter limit="))
div=int(input("divisible by="))
c=0
s=0
for i in range(1,no+1):
    if i%div==0:
        print(i)
        c=c+1
        s=s+i
print("Count = ",c," Sum = ",s)
"""

no=int(input("enter limit="))
div=int(input("divisible by="))
c=0
s=0
i=1
while i<=no:
    if i%div==0:
        c = c + 1
        s = s + i
        print(i)
    i=i+1
print("count=",c,"sum=",s)






