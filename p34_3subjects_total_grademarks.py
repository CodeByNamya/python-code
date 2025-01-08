print("0-50-> C grade")
print("50-100->B grade")
print("100 or above->A garde")
math=int(input("enter math marks="))
eng=int(input("enter eng marks="))
phy=int(input("enter phy marks="))
total=math+eng+phy
print("total is",total)
if total<50 and total>0:
    print("c grade")
elif total>=50 and total<100:
    print("b grade")
elif total>=100:
    print("a grade")
else:
    print("invalid input")