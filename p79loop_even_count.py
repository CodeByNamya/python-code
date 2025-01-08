no=int(input("enter limit="))
c=0
for i in range(1,no+1):
    if i%2==0:
        print(i)
        c=c+1
print("no of even numbers=",c)