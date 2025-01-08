no=int(input("enter limit="))
s=0
for i in range(2,no+1,10):
    print(i,end="+")
    s=s+i
print("\naddition of even numbers is=",s)