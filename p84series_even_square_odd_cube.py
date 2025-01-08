no=int(input("enter limit="))
s=1
for i in range(1,no+1):
    if i%2==0:
        print(i*i,end="+")
        s=s+i*i
    else:
        print(i*i*i,end="+")
        s=s+i*i*i
print("\nsum is=",s)