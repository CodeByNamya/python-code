import random
right=0
wrong=0
q=1
while True:
    print("Your Question no",q)
    q=q+1
    print("+ for addition")
    print('- for subtraction')
    print("* for multiplication")
    option = input("enter choice->")
    if option=="+":
        x = random.randint(1, 100)
        y = random.randint(1, 100)
        print("No1=", x, "No2=", y)

        ans=int(input("enter ans="))
        if ans==x+y:
            right=right+1
            print("Your answer is right")
        else:
            wrong=wrong+1
            print("Your answer is wrong")
    elif option=="*":
        x = random.randint(1, 100)
        y = random.randint(1, 100)
        print("No1=", x, "No2=", y)

        ans = int(input("enter ans="))
        if ans==x*y:
            right=right+1
            print("your ans is right")
        else:
            wrong=wrong+1
            print("your ans is wrong")
    elif option=="-":
        x = random.randint(1, 100)
        y = random.randint(1, 100)
        print("No1=", x, "No2=", y)

        ans = int(input("enter ans="))
        if ans==x-y:
            right = right + 1
            print("your ans is right")
        else:
            wrong=wrong+1
            print("your ans is wrong")
    elif option=="e":
        print('Bye!!! ,total right ans =',right," total wrong ans=",wrong)
        break
    else:
        print("invalid input")


#palindrome no