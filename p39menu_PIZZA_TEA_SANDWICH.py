print("MENU:")
print("pizza")
print("tea")
print("sandwich")
options=input("enter your choice->").lower()
if options=='pizza':
    print("it is 300 rupees")
elif options=="tea":
    print("it is 20 rupees")
elif options=="sandwich":
    print("it is 150 rupees")
else:
    print("sorry it is not available")