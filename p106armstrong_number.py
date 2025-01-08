sum=0
no=int(input("enter number="))
temp=no
while temp>0:
    digits = temp % 10
    sum = sum + digits ** 3
    temp = temp // 10
    #print(digits,sum,temp)

if no==sum:
    print("armstrong number")
else:
    print("Not a armstrong number")
