s=0
n=int(input("enter your limit="))
for i in range(1,n+1):
    if i==n:
        print(i)
    else:
        print(i,end="+")

    s=s+i
print('\nsum of all numbers=',s)