b1=0
b2=0
b3=0
while True:
    print('1 for pizza')
    print("2 for tea")
    print("3 for vadapav")
    print("4 for exit menu")
    option=int(input("enter number="))
    if option==1:
        print("it is 300rs/pizza")
        value=int(input("how many do you want?"))
        b1=value*300
        print("total bill=",b1)
    elif option==2:
        print("it is 20 rupees")
        qty = int(input("how many cups of tea do you want?"))
        b2=qty*20
        print("total bill is", qty*20)
    elif option==3:
        print("it is 150 rupees")
        qty=int(input("how many sandwiches you want?"))
        b3=qty*150
        print("total bill is", qty*150)
    elif option == 4:
        print("exit")
        print("grand total=",b1+b2+b3)
        break
    else:
        print("wrong input")

