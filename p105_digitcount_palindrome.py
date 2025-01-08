reverse=0
no=int(input("enter number="))
temp=no
c=0
s=0
while temp!=0:
    s=s+temp%10
    temp=temp//10
    c+=1


print("Sum = ",s, "No = ",no,"Count = ",c)

