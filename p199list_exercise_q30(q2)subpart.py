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
    n11 = input("enter first city name=>")
    n22=input("enter second city name=>")
    if n11 in india and n22 in india:
        print("yes both belong to india")
        n1=n1+1
    elif n11 in pakistan and n22 in pakistan:
        print("yes both belong to pakistan")
        n2=n2+1
    elif n11 in bangladesh and n22 in bangladesh:
        print("yes both belong to bangladesh")
        n3=n3+1
    else:
        print("they both belong to different country")
    ans=input("do you want to continue?")







