n=int(input("enter limit=>"))
for i in range(1,n+1):
    for j in range(n,i-1,-1):
        print("*",end="")
    print("")

"""
11111
2222 
333
44
5

12345
1234
123
12
1

54321
5432
543
54
5

55555
4444
333
22
1

"""
