amount=int(input("enter amount->"))
if amount<7000:
    print("total bill is",amount)
if amount>10000:
    print("total bill is",amount-0.2*amount)
elif amount>7000 and amount<=10000:
    print("total bill is",amount-0.15*amount)
elif amount>=7000:
    print("total bill is",amount-0.1*amount)
else:
    print("enter amount correctly")