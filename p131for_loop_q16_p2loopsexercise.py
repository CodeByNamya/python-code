f=1
s=0
no=int(input("enter number="))
for i in range(no,0,-1):
    print(i,end="*")
    f=f*i
    s=s+i
print("\nfactorial is=",f)
print("\nsum is",s)
