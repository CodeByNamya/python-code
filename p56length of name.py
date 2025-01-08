name=input("enter name->")
if len(name)<=0:
    print("does not exist")
elif len(name)<6:
    print("length=",len(name))
else:
    print("long name")