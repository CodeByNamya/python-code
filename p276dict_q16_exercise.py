
d1={"info":[600,630,620],"ril":[1430,1490,1567],"mtl":[234,180,160]}
print("select a option=:")
print("print")
print("add")
option=input("enter your choice=>")
if option=="print":
    print("stockname\tprice1\tprice2\tprice3")
    for k,v in d1.items():
        a,b,c=v
        avg=a+b+c/3

        print(k,"  =>\t",a,b,c,"  ==>\t",avg)
