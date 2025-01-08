no=int(input("enter number="))
f=1
for i in range(no,0,-1):
    print(i,end = " X ")
    f=f*i
print("\nfactorial of number is=>",f)
