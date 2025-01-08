age=int(input("enter age="))
if age>0 and age<=12:
    print("child")
elif age>=13 and age<=19:
    print("teenager")
elif age>=20 and age<=64:
    print("adult")
elif age>=65:
    print("senior")
else:
    print('enter age correctly')