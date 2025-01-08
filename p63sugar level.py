sugar=int(input("enter sugar level="))
if sugar<=0:
    print("not possible")
elif sugar<=80:
    print("low sugar levels")
elif sugar>100:
    print("high sugar levels")
else:
    print("normal sugar level")