
n1=0
n2=0
n3=0
india = ["mumbai", "banglore", "chennai", "delhi"]
pakistan = ["lahore","karachi","islamabad"]
bangladesh = ["dhaka", "khulna", "rangpur"]
print(india)
print(pakistan)
print(bangladesh)

ans="yes"
while ans=="yes":
    n = input("enter first city name=>")
    if n in india:
        print("yes", n, "is in india")
        n1=n1+1
    elif n in pakistan:
        print("yes", n, "is in pakistan")
        n2=n2+1
    elif n in bangladesh:
        print("yes", n, "is in bangladesh")
        n3=n3+1
    else:
        print("wrong city")
    ans=input("do you want to continue?")

print(n1," cities selected in india")
print(n2,"cities selected in pakistan")
print(n3,"cities  selected in bangladesh")






