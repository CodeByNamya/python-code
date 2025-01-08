while True:
    print("+ for addition")
    print('- for subtraction')
    print("* for multiplication")
    option=input("enter choice->")
    if option=="+":
        no1=int(input("enter no1="))
        no2=int(input("enter no2="))
        print("addition of two numbers is=",no1+no2)
    elif option=="-":
        no1 = int(input("enter no1="))
        no2 = int(input("enter no2="))
        print("subtraction of two number is=",no1-no2)
    elif option=="*":
        no1 = int(input("enter no1="))
        no2 = int(input("enter no2="))
        print("multiplication of two number is=",no1*no2)
    elif option=="e":
        print("exit")
        break
    else:
        print('wrong input')



