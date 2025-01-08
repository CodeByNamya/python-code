def add():
    print("ADD-:")
    a=int(input("Enter no1 =>"))
    b = int(input("Enter no2 =>"))
    print("Add = ",a+b)

def max2():
    print("MAX2NO-:")
    a = int(input("Enter no1 =>"))
    b = int(input("Enter no2 =>"))
    if a>b:
        print("No1 is greater")
    else:
        print("No2 is greater")

def table():
    print("TABLE-:")
    no=int(input("enter number="))
    i=1
    for i in range(1,11):
        a=no*i
        print(no,"*",i,"=",a)
def oddeven():
    print("ODD/EVEN")
    no=int(input("enter number="))
    if no%2==0:
        print("even")
    else:
        print("odd")

def posneg():
    print("POS/NEG-:")
    no=int(input("enter number="))
    if no>0:
        print("pos")
    elif no==0:
        print("non-pos/neg")
    else:
        print("neg")

def areasquare():
    print("AREA-SQUARE-:")
    no=int(input("enter side length="))
    print("area of square is",no*no)

def areatriangle():
    print("AREA-TRIANGLE-:")
    h=int(input("enter height="))
    b=int(input("enter breadth="))
    print("area of triangle=",0.5*h*b)

def areacircle():
    print("AREA-CIRCLE-:")
    r=int(input("enter radius"))
    print("area of circle=",3.14*r*r)

def max3():
    print("MAX3NO-:")
    no1=int(input("enter no1="))
    no2=int(input("enter no2="))
    no3=int(input("enter no3="))
    if no1>no2 and no1>no3:
        print("no1 is max")
    if no2>no3 and no2>no1:
        print("no2 is max")
    if no3>no1 and no3>no2:
        print("no3 is max")
    else:
        print("wrong input")
def factorial():
    print("FACTORIAL-:")
    no=int(input("enter number="))
    i=no
    f=1
    while i>=1:
        print(i,end="*")
        f=f*i
        i=i-1
    print("\nfactorial=",f)

def palindrome():
    reverse=0
    no=int(input("enter number="))
    temp=no
    while temp>0:
        reverse=reverse*10+temp%10
        temp=temp//10
    print("reverse no=",reverse,"original number=",no)
    if reverse==no:
        print("palindrome number")
    else:
        print("not a palindrome")






factorial()
add()
max2()
table()
oddeven()
areatriangle()
areasquare()
max3()
"""
table()
oddeven()
posneg()
square()
areaoftri()
areaofcricle()
max3()
factorial()
palindromeno()
"""