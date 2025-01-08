while True:
    print("1 for square")
    print("2 for cube")
    print("3 for exit")
    option=int(input("enter option =>"))
    if option==1:
        no = int(input("enter number="))
        print("square of number=",no*no)
    elif option==2:
        no = int(input("enter number="))
        print("cube of number=",no*no*no)
    elif option==3:
        print("Bye")
        break
    else:
        print("wrong input")


