print("MENU:")
print("pizza")
print("tea")
print("sandwich")
options=input("enter your choice->").lower()
if options=='pizza':
    print("it is 300 rupees")
    qty=int(input("how many pizza you want?"))
    print("total bill is", qty*300)
elif options=="tea":
    print("it is 20 rupees")
    qty = int(input("how many cups of tea do you want?"))
    print("total bill is", qty*20)

elif options=="sandwich":
    print("it is 150 rupees")
    qty = int(input("how many sandwiches you want?"))
    print("total bill is", qty*150)

else:
    print("sorry it is not available")
