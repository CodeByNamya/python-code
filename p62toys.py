print("Toys available-:")
print("battery-based")
print("key-based")
print('electrical charging based')
toys=input("what kind of toy do you want?").lower()
if toys=="battery":
    print("it is 500rs/toy")
    qty=int(input("how many do you want->"))
    amount=qty*500
    if amount>1000:
        print("you got 10% discount, total bill is",amount-0.1*amount)
    else:
        print("total bill is",amount)
elif toys=="key":
    print("it is 20rs/toy")
    qty=int(input("how many do you want"))
    amount=qty*20
    if amount>100:
        print("you got 5% discount, total bill is",amount-0.05*amount)
    else:
        print("total bill is",amount)
elif toys=="electrical":
    print("it is 250rs/toy")
    qty=int(input("how many do you want->"))
    amount=qty*250
    if amount>500:
        print("you got 10% discount, total bill is",amount-0.1*amount)
else:
    print("not available")









