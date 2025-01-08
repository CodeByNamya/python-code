n=int(input("enter number="))
for i in range(1,n+1):
    if n%i==0:
        print("it is not a prime")
    elif n%n==0 and n%1==0:
        print("it is a prime")
else:
    print("neither")


