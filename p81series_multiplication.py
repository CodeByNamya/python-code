no=int(input("enter limit="))
s=1
for i in range(1,no+1):
    if i ==no:
        print(i, end=" ")
    else:
        print(i, end="*")
    s=s*i
print("\nproduct =", s)