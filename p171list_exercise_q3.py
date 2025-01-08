l1=[11,23,24,32,35,46,67,90,97,95]
print(l1)
list.sort(l1)
print(l1)
for x in l1:
    if x%2==0:
        print(x,"is even")
    else:
        print(x,"is odd")