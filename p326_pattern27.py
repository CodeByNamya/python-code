n=int(input("enter limit=>"))
for i in range(n,0,-1):
    for j in range(1,i+1):
        print(" ",end="")
    for j in range(1,i+1):
        print(i,end="")
    print("")