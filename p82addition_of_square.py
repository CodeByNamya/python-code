no=int(input("enter limit="))
s=0
for i in range(1,no+1):
    print(i*i, end ="+")
    s=s+i*i
print("\nsum of squares=",s)