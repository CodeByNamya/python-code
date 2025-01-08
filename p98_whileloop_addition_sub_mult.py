while True:
    print("1 for addition")
    print("2 for subtraction")
    print("3 for multiplication")
    option=int(input("enter value="))
    if option==1:
        no1 = int(input("enter number1="))
        no2 = int(input("enter number2="))
        a=no1+no2
        print("addition of number is=",a)
    elif option==2:
        no1 = int(input("enter number1="))
        no2 = int(input("enter number2="))
        a=no1-no2
        print("subtraction of number is=",a)
    elif option==3:
        no1 = int(input("enter number1="))
        no2 = int(input("enter number2="))
        a = no1*no2
        print("multiplication of number is=", a)
    elif option == 4:
        print("Bye")
        break
    else:
        print("wrong input")


