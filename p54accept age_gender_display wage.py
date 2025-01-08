age=int(input("enter age="))
gender=input("gender->").lower()
if age>=18 and age<30:
    if gender=="m":
        print("wage=700rs/day")
    elif gender=="f":
        print("wage=750rs/day")
elif age>=30 and age<=40:
    if gender=='m':
        print("wage=800rs/day")
    elif gender=="f":
        print("wage=850rs/day")
else:
     print("cant work")

