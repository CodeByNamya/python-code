reverse=0
temp=int(input("enter number="))

while temp!=0:
    reverse=reverse*10+temp%10
    temp=temp//10

print(reverse,end="")