d1={"maggie":25,"biscuit":45,'rice':100,"sushi":500,"momos":120}
t=0
print(d1)
print("item\tprice")
for k,v in d1.items():
    print(k,"=>",v)
for x in d1.values():
   t=t+x

print("total bill is=>",t)
