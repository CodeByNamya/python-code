options=input("enter the character->").lower()
if options=="s":
    number = int(input("enter number="))
    print("square of number is", number*number)
elif options=="c":
    number = int(input("enter number="))
    print('cube of number is', number*number*number)
else:
    print("choose the character properly")