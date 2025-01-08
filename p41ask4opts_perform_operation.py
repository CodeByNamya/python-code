print("press + for addition")
print("press - for subtraction")
print("press * for multiplication")
print("press / for divison")
options=input("enter your operator->")
no1=int(input("enter number1="))
no2=int(input("enter number2="))
if options== "+":
    print("addition of 2 number is", no1+no2)
elif options=="-":
    print("subtraction of 2 number is", no1-no2)
elif options=="*":
    print("multiplication of 2 number is", no1*no2)
elif options=="/":
    print("division of 2 number is", no1/no2)
else:
    print("invalid operator")