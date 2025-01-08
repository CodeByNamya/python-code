reverse=0
no=int(input("enter number="))
temp=no
while temp!=0:
    reverse=reverse*10+temp%10
    temp=temp//10

print("Reverse no  = ",reverse, "No = ",no)
if reverse==no:
    print("Palindrome number")
else:
    print("Not")