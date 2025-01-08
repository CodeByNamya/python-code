n=int(input("enter limit="))
div=int(input("divisible by="))
s=0
c=0
for i in range(1,n+1):
    if i%div==0:
        print(i)
        c=c+1
        s=s+i
print("count=",c,"sum=",s)

