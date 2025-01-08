

d1={"ram":33,"rahul":15,"dev":45,'kj':32,"devarsh":12}
print(d1)
n=input("enter key to delete=>")
if n in d1:
    del d1[n]

print(d1)
