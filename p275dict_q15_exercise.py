
d1={"china":143,"india":136,"usa":32,"uk":21}
print(d1)
print("chose from below option=:")
print("add")
print("remove")
print("print")
print("query")
options=input("enter your choice=>")
if options == "add":
    name = input("enter country name=>")
    if name in d1:
        print("country already exist")
    else:
        population = int(input("enter country population=>"))
        d1[name] = population
        print(d1)
if options=="remove":
    k=input("enter country you want to remove=>")
    if k in d1:
        del d1[k]
        print("country\t\tpopulation")
        for k,v in d1.items():
            print(k,"\t\t=>",v)
    else:
        print("that value is not found")
if options=="print":
    print("country\t\tpopulation")
    for k,v in d1.items():
        print(k," \t\t=>",v)
if options=="query":
    c=input("enter country for which you want to query=>")
    if options == "query":
        c = input("enter country for which you want to query=>")
        if c in d1:
            print(d1[c], "\t\t", c)
        else:
            print("that value is not found")


