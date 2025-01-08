import random
x=random.randint(1,100)
y=random.randint(1,100)
option=random.randint(1,3)
print("no1=",x, "no2=",y)
print("option from 1-3 is=",option)
if option==1:
    print("addition of numbers is=",x+y)
elif option==2:
    print("subtraction of numbers is=",x-y)
elif option==3:
    print("multiplication of number is=",x*y)
else:
    print("wrong option")