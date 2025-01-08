age=int(input("enter age="))
gender=input("enter gender->").lower()
if gender=='m':
    if age<=40 and age>=20:
        print("he may work anywhere")
    elif age>40 and age<=60:
        print("he will only work in urban areas")
elif gender=="f":
    print("she will work only in urban areas")






