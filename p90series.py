no=int(input("enter limit="))
s=0
for i in range(no,0,-1):
    print(i,end="+")
    s=s+i
print("\naddition of even numbers is=",s)