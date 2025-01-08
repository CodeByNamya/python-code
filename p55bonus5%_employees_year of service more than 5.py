print("basic salary=20000")
service=int(input("enter years of services->"))
if service<=0:
    print('wrong input')
elif service>5:
    print("you get bonus of 5% that is->",0.05*2000)

else:
    print("no bonus")

