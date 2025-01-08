print("xerox")
print("typing")
print("both")
service=input('what do you want?').lower()
if service=="xerox":
    qty=int(input("how many pgs"))
    if qty<0:
          print("wrong option")
    elif qty<50:
        print("it is 5rs/pg")
        print("total bill is", qty*5)
    elif qty>50:
        print("it is 3rs/pg")
        print("total bill is", qty*3 )
elif service=="typing":
    typingqty=int(input("how many pgs"))
    if typingqty<0:
        print("wrong option")
    elif typingqty<50:
        print("it is 15rs/pg")
        b1=typingqty*15
        print("total bill is", b1)
    elif typingqty>50:
        print("it is 20rs/pg")
        b1 = typingqty*20
        print("total bill is", b1)
elif service=="both":
    qty=int(input("how many pgs of xerox=" ))
    typingqty = int(input("how many pgs of typing="))
    if qty<0:
        print("wrong option")
    elif qty<50:
        print("it is 5rs/pg")
        b1=qty*5
        print("total bill is", qty*5)
    elif qty>50:
        print("it is 3rs/pg")
        b1=qty*3
        print("total bill is", qty*3)

    if typingqty<0:
        print("wrong option")
    elif typingqty<50:
         print("it is 15rs/pg")
         b2=typingqty*15
         print("total bill is", typingqty*15)
    elif typingqty>50:
        print("it is 20rs/pg")
        b2=typingqty*20
        print("total bill is", typingqty*20)

    print("final is=",b1+b2)
else:
    print("Wrong opt")


