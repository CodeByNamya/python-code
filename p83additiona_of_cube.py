no=int(input("enter limit="))
s=1
for i in range(1,no+1):
    if i==no:
        print(i*i*i,end='')
    else:
        print(i * i * i, end="+")
    s=s+i*i*i
print("\nsum of cube is=",s)

