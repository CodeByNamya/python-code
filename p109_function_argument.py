def add(no1,no2):
    print("ADDITION-:")
    print("addition of 2 numbers is=",no1+no2)
def sub(no1,no2):
    print("SUBTRACTION-:")
    print("SUBTRACTION of 2 numbers is=", no1-no2)
def mult(no1,no2):
    print("MULTIPLICATION-:")
    print("multiplication of 2 numbers is=", no1*no2)
def division(no1,no2):
    print("DIVISION-:")
    print("multiplication of 2 numbers is=", no1/no2)

while True:
    no1 = int(input("enter number1->"))
    no2 = int(input("enter number2->"))
    add(no1,no2)
    sub(no1,no2)
    mult(no1,no2)
    division(no1,no2)
    again=input("Do u want to continue?(yes/no)").lower()
    if again=="no":
        break


"""
square(no)
cube(no)

add(a,b,c,d,e)
"""