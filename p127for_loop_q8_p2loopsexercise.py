n=int(input("enter limit="))
div=int(input("divisible by="))
for i in range(1,n+1):
    if i%div==0:
        print(i)

