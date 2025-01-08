b1=0
b2=0
b3=0
while True:
    print("MENU-:")
    print("1)pizza")
    print("2)tea")
    print("3)sandwich")
    choice=input("enter choice->").lower()
    if choice=="pizza":
        print("it is 300rs/pizza")
        value=int(input("how many do you want?"))
        b1=value*300
        print("total bill=",b1)
    elif choice=="tea":
        print("it is 20 rupees")
        qty = int(input("how many cups of tea do you want?"))
        b2=qty*20
        print("total bill is", qty*20)
    elif choice=="sandwich":
        print("it is 150 rupees")
        qty=int(input("how many sandwiches you want?"))
        b3=qty*150
        print("total bill is", qty*150)
    elif choice=="e":
        print("exit")
        print("grand total=",b1+b2+b3)
        break
    else:
        print("wrong input")

