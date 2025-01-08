import math
sum=0
no=int(input("enter number="))
temp=no
while temp>0:
    digits = temp % 10
    sum = sum +math.factorial(digits)
    temp = temp // 10
    print(digits,sum,temp)

if no==sum:
    print("krishnamurthy  number")
else:
    print("Not a krishnamurthy number")
