options=input("do you want to know max of two number or three number?").lower()
if options=="two":
    number1 = int(input("enter number1="))
    number2 = int(input("enter number2="))
    if number1>number2:
        print("number1 is maximum")
    else:
        print("number2 is maximum")
elif options=="three":
    number1 = int(input("enter number1="))
    number2 = int(input("enter number2="))
    number3 = int(input("enter number3="))
    if number1>number2 and number1>number3:
        print("number1 is maximum")
    elif number2>number1 and number2>number3:
        print("number2 is maximum")
    elif number3>number2 and number3>number1:
        print("number3 is maximum")
else:
    print("Wrong opt")




